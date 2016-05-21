import logging
from eventemitter import EventEmitter
from dota2.enums import  EGCBaseClientMsg, ESOMsg, ESOType
from dota2.protobufs import base_gcmessages_pb2 as _gc_base
from dota2.protobufs import dota_gcmessages_client_pb2 as _gc_client
from dota2.protobufs import dota_gcmessages_common_pb2 as _gc_common

def find_so_proto(type_id):
    """Resolves proto massage for given type_id

    :param type_id: SO type
    :type type_id: :class:`dota2.enums.ESOType`
    :returns: proto message or `None`
    """
    if not isinstance(type_id, ESOType):
        return None

    proto = getattr(_gc_base, type_id.name, None)
    if proto is None:
        proto = getattr(_gc_client, type_id.name, None)
    if proto is None:
        proto = getattr(_gc_common, type_id.name, None)

    return proto


class SOBase(object):
    def __init__(self):
        super(SOBase, self).__init__()

        #: Shared Object Caches
        self.socache = SOCache(self)


class SOCache(EventEmitter, dict):
    version = None      #: cache version
    owner_soid = None   #: type and steamid, no clue what type represents

    def __init__(self, dota_client):
        self._dota = dota_client
        self._LOG = logging.getLogger("SOCache")

        # register our handlers
        dota_client.on(ESOMsg.CacheSubscribed, self._handle_cache_subscribed)
        dota_client.on(EGCBaseClientMsg.EMsgGCClientWelcome, self._handle_client_welcome)

    def __hash__(self):
        # pretend that we are a hashable dict, lol
        # don't attach more than one SOCache per DotaClient
        return hash((self._dota, 42))

    def emit(self, event, *args):
        if event is not None:
            self._LOG.debug("Emit event: %s" % repr(event))
        super(SOCache, self).emit(event, *args)

    def _update_cache(self, cache):
        try:
            type_id = ESOType(cache.type_id)
        except ValueError:
            self._LOG.error("Unsupported type: %d" % type_id)
            return

        proto = find_so_proto(type_id)

        if proto is None:
            self._LOG.error("Unable to locate proto for: %s" % repr(type_id))
            return

        self[type_id] = map(proto.FromString, cache.object_data)

        self.emit("cache_updated", type_id)

    def _handle_client_welcome(self, message):
        for one in message.outofdate_subscribed_caches:
            self._handle_cache_subscribed(one)

    def _handle_cache_subscribed(self, message):
        for cache in message.objects:
            self._update_cache(cache)
