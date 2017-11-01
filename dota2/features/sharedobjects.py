"""Essentially a :class:`dict` containing shared object caches.
The objects are read-only, so don't change any values.
The instance reference of individual objects will remain the same thought their lifetime.
Individual objects can be accessed via their key, if they have one.

.. note::
    Some cache types don't have a key and only hold one object instance.
    Then only the the cache type is needed to access it.
    (e.g. ``CSOEconGameAccountClient``)

.. code:: python

    dota_client.socache[ESOType.CSOEconItem]          # dict with item objects, key = item id
    dota_client.socache[ESOType.CSOEconItem][123456]  # item object

    dota_client.socache[ESOType.CSOEconGameAccountClient]  # returns a CSOEconGameAccountClient object

Events will be fired when individual objects are updated.
Event key is a :class:`tuple`` in the following format: ``(event, cache_type)``.

The available events are ``new``, ``updated``, and ``removed``.
Each event has a single parameter, which is the object instance.
Even when removed, there is object instance returned, usually only with the key field filled.

.. code:: python

    @dota_client.socache.on(('new', ESOType.CSOEconItem))
    def got_a_new_item(obj):
        print "Got a new item! Yay"
        print obj

    # access the item via socache at any time
    print dota_client.socache[ESOType.CSOEconItem][obj.id]

"""
import logging
from eventemitter import EventEmitter
from dota2.enums import EGCBaseClientMsg, ESOMsg, ESOType
from dota2.protobufs import base_gcmessages_pb2 as _gc_base
from dota2.protobufs import dota_gcmessages_client_pb2 as _gc_client
from dota2.protobufs import dota_gcmessages_common_pb2 as _gc_common
from dota2.protobufs import dota_gcmessages_common_match_management_pb2 as  _gc_cmm


def find_so_proto(type_id):
    """Resolves proto massage for given type_id

    :param type_id: SO type
    :type  type_id: :class:`dota2.enums.ESOType`
    :returns: proto message or `None`
    """
    if not isinstance(type_id, ESOType):
        return None

    proto = getattr(_gc_base, type_id.name, None)
    if proto is None:
        proto = getattr(_gc_client, type_id.name, None)
    if proto is None:
        proto = getattr(_gc_common, type_id.name, None)
    if proto is None:
        proto = getattr(_gc_cmm, type_id.name, None)

    return proto

# hack to mark certain CSO as having no key
class NO_KEY:
    pass

so_key_fields = {
    _gc_base.CSOEconItem.DESCRIPTOR: ['id'],
    _gc_base.CSOEconGameAccountClient.DESCRIPTOR: NO_KEY,
    _gc_common.CSODOTAGameAccountClient.DESCRIPTOR: NO_KEY,
}

# key is either one or a number of fields marked with option 'key_field'=true in protos
def get_so_key_fields(desc):
    if desc in so_key_fields:
        return so_key_fields[desc]
    else:
        fields = []

        for field in desc.fields:
            for odesc, value in field.GetOptions().ListFields():
                if odesc.name == 'key_field' and value == True:
                    fields.append(field.name)

        so_key_fields[desc] = fields
        return fields

def get_key_for_object(obj):
    key = get_so_key_fields(obj.DESCRIPTOR)

    if key is NO_KEY:
        return NO_KEY
    elif not key:
        return None
    elif len(key) == 1:
        return getattr(obj, key[0])
    else:
        return tuple(map(lambda x: getattr(obj, x), key))


class SOBase(object):
    def __init__(self):
        super(SOBase, self).__init__()

        #: Shared Object Caches
        name = "%s.socache" % self.__class__.__name__
        self.socache = SOCache(self, name)


class SOCache(EventEmitter, dict):
    ESOType = ESOType   #: expose ESOType

    file_version = None  #: so file version

    def __init__(self, dota_client, logger_name):
        self._LOG = logging.getLogger(logger_name if logger_name else self.__class__.__name__)
        self._caches = {}
        self._dota = dota_client

        # register our handlers
        dota_client.on(ESOMsg.Create, self._handle_create)
        dota_client.on(ESOMsg.Update, self._handle_update)
        dota_client.on(ESOMsg.Destroy, self._handle_destroy)
        dota_client.on(ESOMsg.UpdateMultiple, self._handle_update_multiple)
        dota_client.on(ESOMsg.CacheSubscribed, self._handle_cache_subscribed)
        dota_client.on(ESOMsg.CacheUnsubscribed, self._handle_cache_unsubscribed)
        dota_client.on(EGCBaseClientMsg.EMsgGCClientWelcome, self._handle_client_welcome)
        dota_client.on('notready', self._handle_cleanup)

    def __hash__(self):
        # pretend that we are a hashable dict, lol
        # don't attach more than one SOCache per DotaClient
        return hash((self._dota, 42))

    def __getitem__(self, key):
        try:
            key = ESOType(key)
        except ValueError:
            raise KeyError("%s" % key)
        if key not in self:
            self[key] = dict()
        return dict.__getitem__(self, key)

    def __repr__(self):
        return "<SOCache(%s)>" % repr(self._dota)

    def emit(self, event, *args):
        if event is not None:
            self._LOG.debug("Emit event: %s" % repr(event))
        super(SOCache, self).emit(event, *args)

    def _handle_cleanup(self):
        for v in self.values():
            if isinstance(v, dict):
                v.clear()
        self.clear()
        self._caches.clear()

    def _get_proto_for_type(self, type_id):
        try:
            type_id = ESOType(type_id)
        except ValueError:
            self._LOG.error("Unsupported type: %d" % type_id)
            return

        proto = find_so_proto(type_id)

        if proto is None:
            self._LOG.error("Unable to locate proto for: %s" % repr(type_id))
            return

        return proto

    def _parse_object_data(self, type_id, object_data):
        proto = self._get_proto_for_type(type_id)

        if proto is None:
            return

        if not get_so_key_fields(proto.DESCRIPTOR):
            self._LOG.error("Unable to find key for %s" % type_id)
            return

        obj = proto.FromString(object_data)
        key = get_key_for_object(obj)

        return key, obj

    def _update_object(self, type_id, object_data):
        result = self._parse_object_data(type_id, object_data)

        if result:
            key, obj = result
            type_id = ESOType(type_id)

            if key is NO_KEY:
                if not isinstance(self[type_id], dict):
                    self[type_id].CopyFrom(obj)
                    obj = self[type_id]
                else:
                    self[type_id] = obj
            else:
                if key in self[type_id]:
                    self[type_id][key].CopyFrom(obj)
                    obj = self[type_id][key]
                else:
                    self[type_id][key] = obj

            return type_id, obj

    def _handle_create(self, message):
        result = self._update_object(message.type_id, message.object_data)
        if result:
            type_id, obj = result
            self.emit(('new', type_id), obj)

    def _handle_update(self, message):
        result = self._update_object(message.type_id, message.object_data)
        if result:
            type_id, obj = result

            if self._dota.verbose_debug:
                self._LOG.debug("Incoming: %s\n%s", repr(type_id), obj)

            self.emit(('updated', type_id), obj)

    def _handle_destroy(self, so):
        result = self._parse_object_data(so.type_id, so.object_data)
        if result:
            key, obj = result
            type_id = ESOType(so.type_id)
            current = None

            if key is NO_KEY:
                current = self.pop(type_id, None)
            else:
                current = self[type_id].pop(key, None)

            if current: current.CopyFrom(obj)

            self.emit(('removed', type_id), current or obj)

    def _handle_update_multiple(self, message):
        for so_object in message.objects_modified:
            self._handle_update(so_object)
        for so_object in message.objects_added:
            self._handle_create(so_object)
        for so_object in message.objects_removed:
            self._handle_destroy(so_object)

    def _handle_client_welcome(self, message):
        self.file_version = message.gc_socache_file_version

        for one in message.outofdate_subscribed_caches:
            self._handle_cache_subscribed(one)

    def _handle_cache_subscribed(self, message):
        cache_key = message.owner_soid.type, message.owner_soid.id
        self._caches.setdefault(cache_key, dict())

        cache = self._caches[cache_key]
        cache['version'] = message.version
        cache.setdefault('type_ids', set()).update(map(lambda x: x.type_id, message.objects))

        for objects in message.objects:
            for object_bytes in objects.object_data:
                result = self._update_object(objects.type_id, object_bytes)
                if not result: break

                type_id, obj = result

                if self._dota.verbose_debug:
                    self._LOG.debug("Incoming: %s\n%s", repr(type_id), obj)

                self.emit(('new', type_id), obj)

    def _handle_cache_unsubscribed(self, message):
        cache_key = message.owner_soid.type, message.owner_soid.id

        if cache_key not in self._caches: return
        cache = self._caches[cache_key]

        for type_id in cache['type_ids']:
            if type_id in self:
                type_id = ESOType(type_id)

                if isinstance(self[type_id], dict):
                    for key in list(self[type_id].keys()):
                        self.emit(('removed', type_id), self[type_id].pop(key))
                else:
                    self.emit(('removed', type_id), self.pop(type_id))

                del self[type_id]
        del self._caches[cache_key]


