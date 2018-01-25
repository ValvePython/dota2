import logging
import six
from eventemitter import EventEmitter
from dota2.enums import EDOTAGCMsg, DOTAChatChannelType_t
from dota2.protobufs.dota_gcmessages_client_chat_pb2 import CMsgDOTAJoinChatChannelResponse,\
                                                            CMsgDOTAChatChannelFullUpdate,\
                                                            CMsgDOTAOtherJoinedChatChannel,\
                                                            CMsgDOTAOtherLeftChatChannel,\
                                                            CMsgDOTAChatChannelMemberUpdate


class ChatBase(object):
    def __init__(self):
        super(ChatBase, self).__init__()
        name = "%s.channels" % self.__class__.__name__
        self.channels = ChannelManager(self, name)


class ChannelManager(EventEmitter):
    EVENT_JOINED_CHANNEL = 'channel_joined'
    """When the client join a channel.

    :param channel: channel instance
    :type  channel: :class:`ChatChannel`
    """
    EVENT_LEFT_CHANNEL = 'channel_left'
    """When the client leaves a channel.

    :param channel: channel instance
    :type  channel: :class:`ChatChannel`
    """
    EVENT_MESSAGE = 'message'
    """On a new channel message

    :param channel: channel instance
    :type  channel: :class:`ChatChannel`
    :param message: message data
    :type  message: `CMsgDOTAChatMessage <https://github.com/ValvePython/dota2/blob/6cb1008f3070e008e9bed9521fad8d1438123aa1/protobufs/dota_gcmessages_client_chat.proto#L86-L122>`_
    """
    EVENT_CHANNEL_MEMBERS_UPDATE = 'members_update'
    """When users join/leave a channel

    :param channel: channel instance
    :type  channel: :class:`ChatChannel`
    :param joined: list of members who joined
    :type  joined: list
    :param left: list of members who left
    :type  left: list
    """

    def emit(self, event, *args):
        if event is not None:
            self._LOG.debug("Emit event: %s" % repr(event))
        EventEmitter.emit(self, event, *args)

    def __init__(self, dota_client, logger_name):
        super(ChannelManager, self).__init__()

        self._LOG = logging.getLogger(logger_name if logger_name else self.__class__.__name__)
        self._dota = dota_client
        self._channels = {}
        self._channels_by_name = {}

        # register our handlers
        self._dota.on('notready', self._cleanup)
        self._dota.on(EDOTAGCMsg.EMsgGCJoinChatChannelResponse, self._handle_join_response)
        self._dota.on(EDOTAGCMsg.EMsgGCChatMessage, self._handle_message)
        self._dota.on(EDOTAGCMsg.EMsgGCOtherJoinedChannel, self._handle_members_update)
        self._dota.on(EDOTAGCMsg.EMsgGCOtherLeftChannel, self._handle_members_update)
        self._dota.on(EDOTAGCMsg.EMsgDOTAChatChannelMemberUpdate, self._handle_members_update)

    def __repr__(self):
        return "<ChannelManager(): %d channels>" % (
                    len(self),
                    )

    def _cleanup(self):
        self._channels.clear()
        self._channels_by_name.clear()

    def _remove_channel(self, channel_id):
        channel = self._channels.pop(channel_id, None)
        self._channels_by_name.pop((channel.name, channel.type), None)

    def __contains__(self, key):
        return (key in self._channels) or (key in self._channels_by_name)

    def __getitem__(self, key):
        if isinstance(key, tuple):
            return self._channels_by_name[key]
        else:
            return self._channels[key]

    def __len__(self):
        return len(self._channels)

    def __iter__(self):
        return six.itervalues(self._channels)

    def _handle_join_response(self, message):
        key = (message.channel_name, message.channel_type)
        self.emit(('join_result',) + key, message.result)

        if message.result == message.JOIN_SUCCESS:
            if message.channel_id in self:
                channel = self[message.channel_id]
            else:
                channel = ChatChannel(self, message)

                self._channels[channel.id] = channel
                self._channels_by_name[key] = channel

            self.emit(self.EVENT_JOINED_CHANNEL, channel)

    def _handle_message(self, message):
        if message.channel_id in self:
            self.emit(self.EVENT_MESSAGE, self[message.channel_id], message)

    def _handle_members_update(self, message):
        if message.channel_id in self:
            channel = self[message.channel_id]
            joined = []
            left = []

            if isinstance(message, CMsgDOTAOtherLeftChatChannel):
                left.append(message.steam_id or message.channel_user_id)
            elif isinstance(message, CMsgDOTAOtherJoinedChatChannel):
                joined.append(message.steam_id or message.channel_user_id)
            elif isinstance(message, CMsgDOTAChatChannelMemberUpdate):
                left = list(message.left_steam_ids)
                joined = list(map(lambda x: x.steam_id or x.channel_user_id, message.joined_members))
            elif isinstance(message, CMsgDOTAChatChannelFullUpdate):
                pass

            channel._process_members_from_proto(message)

            if joined or left:
                self.emit(self.EVENT_CHANNEL_MEMBERS_UPDATE, channel, joined, left)

    def join_channel(self, channel_name, channel_type=DOTAChatChannelType_t.DOTAChannelType_Custom):
        """Join a chat channel

        :param channel_name: channel name
        :type  channel_name: str
        :param channel_type: channel type
        :type  channel_type: :class:`.DOTAChatChannelType_t`
        :return: join result
        :rtype: int

        Response event: :attr:`EVENT_JOINED_CHANNEL`
        """
        if self._dota.verbose_debug:
            self._LOG.debug("Request to join chat channel: %s", channel_name)

        self._dota.send(EDOTAGCMsg.EMsgGCJoinChatChannel, {
            "channel_name": channel_name,
            "channel_type": channel_type
        })

        resp = self.wait_event(('join_result', channel_name, channel_type), timeout=25)

        if resp:
            return resp[0]
        else:
            return None

    def join_lobby_channel(self):
        """
        Join the lobby channel if the client is in a lobby.

        Response event: :attr:`EVENT_JOINED_CHANNEL`
        """
        if self._dota.lobby:
            key = "Lobby_%s" % self._dota.lobby.lobby_id, DOTAChatChannelType_t.DOTAChannelType_Lobby
            return self.join_channel(*key)

    @property
    def lobby(self):
        """References lobby channel if client has joined it

        :return: channel instance
        :rtype: :class:`.ChatChannel`
        """
        if self._dota.lobby:
            key = "Lobby_%s" % self._dota.lobby.lobby_id, DOTAChatChannelType_t.DOTAChannelType_Lobby
            return self._channels_by_name.get(key, None)

    def join_party_channel(self):
        """
        Join the lobby channel if the client is in a lobby.

        Response event: :attr:`EVENT_JOINED_CHANNEL`
        """
        if self._dota.party:
            key = "Party_%s" % self._dota.party.party_id, DOTAChatChannelType_t.DOTAChannelType_Party
            return self.join_channel(*key)

    @property
    def party(self):
        """References party channel if client has joined it

        :return: channel instance
        :rtype: :class:`.ChatChannel`
        """
        if self._dota.party:
            key = "Party_%s" % self._dota.party.party_id, DOTAChatChannelType_t.DOTAChannelType_Party
            return self._channels_by_name.get(key, None)

    def get_channel_list(self):
        """
        Requests a list of chat channels from the GC.

        :return: List of chat channels
        :rtype: `CMsgDOTAChatGetUserListResponse <https://github.com/ValvePython/dota2/blob/6cb1008f3070e008e9bed9521fad8d1438123aa1/protobufs/dota_gcmessages_client_chat.proto#L210-L220>`_, ``None``
        """
        if self._dota.verbose_debug:
            self._LOG.debug("Requesting channel list from GC.")

        jobid = self._dota.send_job(EDOTAGCMsg.EMsgGCRequestChatChannelList, {})
        resp = self._dota.wait_msg(jobid, timeout=25)

        return resp

    def leave_channel(self, channel_id):
        if channel_id in self:
            channel = self[channel_id]

            if self._dota.verbose_debug:
                self._LOG.debug("Leaving chat channel: %s", repr(channel))

            self._dota.send(EDOTAGCMsg.EMsgGCLeaveChatChannel, {
                "channel_id": channel_id
            })

            self._remove_channel(channel_id)
            self.emit(self.EVENT_LEFT_CHANNEL, channel)


class ChatChannel(object):
    def __init__(self, channel_manager, join_data):
        self._manager = channel_manager
        self._dota = self._manager._dota
        self._LOG = self._manager._LOG

        self.members = {}
        self.id = join_data.channel_id
        self.name = join_data.channel_name
        self.type = join_data.channel_type
        self.user_id = join_data.channel_user_id
        self.max_members = join_data.max_members

        self._process_members_from_proto(join_data)

    def __repr__(self):
        return "<ChatChannel(%s, %s, %s)>" % (
                    self.id,
                    repr(self.name),
                    self.type,
                    )

    def _process_members_from_proto(self, data):
        if isinstance(data, CMsgDOTAOtherLeftChatChannel):
            self.members.pop(data.steam_id or data.channel_user_id, None)
            return
        elif isinstance(data, CMsgDOTAOtherJoinedChatChannel):
            members = [data]
        elif isinstance(data, CMsgDOTAJoinChatChannelResponse):
            members = data.members
        elif isinstance(data, CMsgDOTAChatChannelMemberUpdate):
            for steam_id in data.left_steam_ids:
                self.members.pop(steam_id, None)

            members = data.joined_members

        for member in members:
            self.members[member.steam_id or member.channel_user_id] = (
                member.persona_name,
                member.status
            )


    def leave(self):
        """Leave channel"""
        self._manager.leave_channel(self.id)

    def send(self, message):
        """Send a message to the channel

        :param message: message text
        :type  message: str
        """
        self._dota.send(EDOTAGCMsg.EMsgGCChatMessage, {
            "channel_id": self.id,
            "text": message
        })

    def share_lobby(self):
        """Share current lobby to the channel"""
        if self._dota.lobby:
            self._dota.send(EDOTAGCMsg.EMsgGCChatMessage, {
                "channel_id": self.id,
                "share_lobby_id": self._dota.lobby.lobby_id,
                "share_lobby_passkey": self._dota.lobby.pass_key
            })

    def flip_coin(self):
        """Flip a coin"""
        self._dota.send(EDOTAGCMsg.EMsgGCChatMessage, {
            "channel_id": self.id,
            "coin_flip": True
        })

    def roll_dice(self, rollmin=1, rollmax=100):
        """Roll a dice

        :param rollmin: dice min value
        :type  rollmin: int
        :param rollmax: dice max value
        :type  rollmax: int
        """
        self._dota.send(EDOTAGCMsg.EMsgGCChatMessage, {
            "channel_id": self.id,
            "dice_roll": {
                "roll_min": dmin,
                "roll_max": dmax
            }
        })
