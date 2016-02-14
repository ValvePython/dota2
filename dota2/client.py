import logging
import gevent
import google.protobuf
from steam.util.events import EventEmitter
from steam.core.msg import GCMsgHdrProto
from steam.client.gc import GameCoordinator
from dota2.features import FeatureBase
from dota2.enums import EGCBaseClientMsg, EDOTAGCSessionNeed, GCConnectionStatus, ESourceEngine
from dota2.msg import get_emsg_enum, find_proto
from dota2.protobufs import gcsdk_gcmessages_pb2 as pb_gc
from dota2.protobufs import dota_gcmessages_client_pb2 as pb_gclient

logger = logging.getLogger("Dota2Client")


class Dota2Client(EventEmitter, FeatureBase):
    _logger = logger
    verbose_debug = False
    appid = 570

    @property
    def account_id(self):
        return self.steam.steam_id.id

    def __init__(self, client_instance=None):
        super(Dota2Client, self).__init__()

        from steam.client import SteamClient

        if not isinstance(client_instance, SteamClient):
            raise ValueError("Expected an instance of SteamClient as argument")

        self.steam = client_instance
        self.gc = GameCoordinator(self.steam, self.appid)

        self.gc.on(None, self._handle_gc_message)

        self.ready = False
        self.connection_status = GCConnectionStatus.NO_SESSION

        self.on(EGCBaseClientMsg.EMsgGCClientConnectionStatus, self._handle_conn_status)
        self.on(EGCBaseClientMsg.EMsgGCClientWelcome, self._handle_client_welcome)

    def __repr__(self):
        return "<%s(%s) %s>" % (self.__class__.__name__,
                                              repr(self.steam),
                                              repr(self.connection_status),
                                              )

    def emit(self, event, *args):
        if event is not None:
            logger.debug("Emit event: %s" % repr(event))
        super(Dota2Client, self).emit(event, *args)

    def _handle_client_welcome(self, message):
        self._set_connection_status(GCConnectionStatus.HAVE_SESSION)

    def _handle_conn_status(self, message):
        self._set_connection_status(message.status)
        self.emit("connetion_status", self.connection_status)

    def _handle_gc_message(self, emsg, header, payload):
        emsg = get_emsg_enum(emsg)
        proto = find_proto(emsg)

        if proto is None:
            logger.error("Failed to parse: %s" % repr(emsg))
            return

        message = proto()
        message.ParseFromString(payload)

        if self.verbose_debug:
            logger.debug("Incoming: %s\n%s\n---------\n%s" % (repr(emsg),
                                                              str(header),
                                                              str(message),
                                                              ))
        else:
            logger.debug("Incoming: %s", repr(emsg))

        self.emit(emsg, message)

    def _set_connection_status(self, status):
        self.connection_status = GCConnectionStatus(status)

        if self.connection_status == GCConnectionStatus.HAVE_SESSION and not self.ready:
            self.ready = True
            self.emit('ready')
        elif self.connection_status != GCConnectionStatus.HAVE_SESSION and self.ready:
            self.ready = False
            self.emit('notready')

    def send(self, emsg, data={}, proto=None):
        if not isinstance(data, dict):
            raise ValueError("data kwarg can only be a dict")

        if proto is None:
            proto = find_proto(emsg)

        if not issubclass(proto, google.protobuf.message.Message):
            raise ValueError("Unable to find proto for emsg, or proto kwarg is invalid")

        message = proto()

        for key, value in data.items():
            setattr(message, key, value)

        self.gc.send(GCMsgHdrProto(emsg), message.SerializeToString())

    def launch(self):
        if not self.steam.logged_on:
            self.steam.wait_event('logged_on')

        self.steam.games_played([self.appid])

        self.send(EGCBaseClientMsg.EMsgGCClientHello, {
            'client_session_need': EDOTAGCSessionNeed.UserInUINeverConnected,
            'engine': ESourceEngine.ESE_Source2,
            })

    def exit(self):
        self.steam.games_played([])
        self._set_connection_status(GCConnectionStatus.NO_SESSION)
