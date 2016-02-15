"""
Only the most essential features to :class:`dota2.client.Dota2Client` are found here. Every other feature is inherited from
the :mod:`dota2.features` package and it's submodules.
"""

import logging
import gevent
import google.protobuf
from eventemitter import EventEmitter
from steam.core.msg import GCMsgHdrProto
from steam.client.gc import GameCoordinator
from dota2.features import FeatureBase
from dota2.enums import EGCBaseClientMsg, EDOTAGCSessionNeed, GCConnectionStatus, ESourceEngine
from dota2.msg import get_emsg_enum, find_proto
from dota2.protobufs import gcsdk_gcmessages_pb2 as pb_gc
from dota2.protobufs import dota_gcmessages_client_pb2 as pb_gclient

logger = logging.getLogger("Dota2Client")


class Dota2Client(EventEmitter, FeatureBase):
    """
    :param steam_client: Instance of the steam client
    :type steam_client: :class:`steam.client.SteamClient`
    """
    _logger = logger
    verbose_debug = False  #: enable pretty print of messages in debug logging
    appid = 570  #: main client app id
    current_jobid = 0
    ready = False  #: ``True`` when we have a session with GC
    connection_status = GCConnectionStatus.NO_SESSION  #: :class:`dota2.enums.GCConnectionStatus`

    @property
    def account_id(self):
        """
        Account ID of the logged in user in the steam client
        """
        return self.steam.steam_id.id

    def __init__(self, steam_client=None):
        super(Dota2Client, self).__init__()

        from steam.client import SteamClient

        if not isinstance(steam_client, SteamClient):
            raise ValueError("Expected an instance of SteamClient as argument")

        self.steam = steam_client  #: instance of steam client
        self.gc = GameCoordinator(self.steam, self.appid)  #: instance of :class:`steam.client.gc.GameCoordinator`

        self.gc.on(None, self._handle_gc_message)

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

        if header.proto.job_id_target != 18446744073709551615:
            self.emit('job_%d' % header.proto.job_id_target, message)

    def _set_connection_status(self, status):
        self.connection_status = GCConnectionStatus(status)

        if self.connection_status == GCConnectionStatus.HAVE_SESSION and not self.ready:
            self.ready = True
            self.emit('ready')
        elif self.connection_status != GCConnectionStatus.HAVE_SESSION and self.ready:
            self.ready = False
            self.emit('notready')

    def send_job(self, *args, **kwargs):
        """
        Send a message as a job

        Exactly the same as :meth:`send`

        :return: jobid event identifier
        :rtype: :class:`str`

        """
        jobid = self.current_jobid = (self.current_jobid + 1) % 4294967295

        self._send(*args, jobid=jobid, **kwargs)

        return "job_%d" % jobid

    def send(self, emsg, data={}, proto=None):
        """
        Send a message

        :param emsg: Enum for the message
        :param data: data for the proto message
        :type data: :class:`dict`
        :param proto: (optional) manually specify protobuf, other it's detected based on ``emsg``
        """
        self._send(emsg, data, proto)

    def _send(self, emsg, data={}, proto=None, jobid=None):
        if not isinstance(data, dict):
            raise ValueError("data kwarg can only be a dict")

        if proto is None:
            proto = find_proto(emsg)

        if not issubclass(proto, google.protobuf.message.Message):
            raise ValueError("Unable to find proto for emsg, or proto kwarg is invalid")

        message = proto()

        for key, value in data.items():
            if isinstance(value, list):
                getattr(message, key).extend(value)
            else:
                setattr(message, key, value)

        header = GCMsgHdrProto(emsg)

        if jobid is not None:
            header.proto.job_id_source = jobid

        self.gc.send(header, message.SerializeToString())

    def launch(self):
        """
        Launch Dota 2 and establish connection with the game coordinator

        ``ready`` event will fire when the session is ready.
        If the session is lost ``notready`` event will fire.
        Alternatively, ``connection_status`` event can be monitored for changes.
        """
        if not self.steam.logged_on:
            self.steam.wait_event('logged_on')

        self.steam.games_played([self.appid])

        self.send(EGCBaseClientMsg.EMsgGCClientHello, {
            'client_session_need': EDOTAGCSessionNeed.UserInUINeverConnected,
            'engine': ESourceEngine.ESE_Source2,
            })

    def exit(self):
        """
        Close connection to Dota 2's game coordinator
        """
        self.steam.games_played([])
        self._set_connection_status(GCConnectionStatus.NO_SESSION)
