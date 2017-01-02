from steam.enums import EResult
from dota2.enums import EDOTAGCMsg, DOTAChatChannelType_t


class Chat(object):
    """"""

    EVENT_CHANNEL_JOIN = 'channel_join'
    """When the client join a channel.
    :param message:
    :type  message:
    """
    EVENT_CHANNEL_MESSAGE = 'channel_message'
    """When there is a new message in a channel.
    :param message:
    :type  message:
    """
    EVENT_CHANNEL_MEMBER_JOIN = 'channel_member_join'
    """When a member joins a channel.
    :param message:
    :type  message:
    """
    EVENT_CHANNEL_MEMBER_LEAVE = 'channel_member_leave'
    """When a member leaves a channel.
    :param message:
    :type  message:
    """

    def __init__(self):
        super(Chat, self).__init__()

        self.channels = {}
        self.on('notready', self.__chat_cleanup)

        # register our handlers
        self.on(EDOTAGCMsg.EMsgGCJoinChatChannelResponse, self.__handle_channel_join)
        self.on(EDOTAGCMsg.EMsgGCChatMessage, self.__handle_channel_message)
        self.on(EDOTAGCMsg.EMsgGCOtherJoinedChannel, self.__handle_channel_member_join)
        self.on(EDOTAGCMsg.EMsgGCOtherLeftChannel, self.__handle_channel_member_leave)

    def __chat_cleanup(self):
        self.channels = {}

    def __handle_channel_join(self, channel_info):
        self.channels[channel_info.channel_id] = channel_info
        self.emit(self.EVENT_CHANNEL_JOIN, channel_info)

    def __handle_channel_message(self, message_info):
        self.emit(self.EVENT_CHANNEL_MESSAGE, message_info)

    def __handle_channel_member_join(self, member_info):
        self.emit(self.EVENT_CHANNEL_MEMBER_JOIN, member_info)

    def __handle_channel_member_leave(self, member_info):
        self.emit(self.EVENT_CHANNEL_MEMBER_LEAVE, member_info)

    def join_channel(self, channel_name, channel_type=DOTAChatChannelType_t.DOTAChannelType_Custom):
        """
        Send a join channel requests to the GC.

        :param channel_name: Name of the channel to join
        :type channel_name: :class: `str`
        :param channel_type: Type of channel to join
        :type channel_type: :class: `DOTAChatChannelType_t`

        Response event: ``channel_join``

        :param message: `EMsgGCJoinChatChannelResponse`
        :type  message: proto message
        """
        if self.verbose_debug:
            self._LOG.debug("Joining chat channel: {0}".format(channel_name))

        self.send(EDOTAGCMsg.EMsgGCJoinChatChannel, {
            "channel_name": channel_name,
            "channel_type": channel_type
        })

    def join_lobby_channel(self):
        """
        Join the lobby channel if the client is in a lobby.

        Response event: ``channel_join``

        :param message: `EMsgGCJoinChatChannelResponse`
        :type  message: proto message
        """
        if self.lobby is None:
            if self.verbose_debug:
                self._LOG.debug("Can't join lobby channel if you aren't in the lobby")
            return

        self.join_channel("Lobby_%s" % self.lobby.lobby_id, DOTAChatChannelType_t.DOTAChannelType_Lobby)

    def leave_channel(self, channel_id):
        """
        Send a leave channel requests to the GC.

        :param channel_id: id of the channel to leave
        :type channel_id: :class: `int`
        """
        channel = self.channels.get(channel_id)
        if channel is None:
            if self.verbose_debug:
                self._LOG.debug("Impossible to leave a channel you are not member of.")
            return

        if self.verbose_debug:
            self._LOG.debug("Leaving chat channel: {0} {1}".format(channel_id, channel.channel_name))

        self.send(EDOTAGCMsg.EMsgGCLeaveChatChannel,{
            "channel_id": channel_id
        })

        del self.channels[channel_id]

    def send_message(self, channel_id, message):
        """
        Send a message to a channel the client has joined.

        :param channel_id: id of the channel to send a message to
        :type channel_id: :class: `int`
        :param message: message to send in the channel
        :type message: :class: `str`
        """
        channel = self.channels.get(channel_id)
        if channel is None:
            if self.verbose_debug:
                self._LOG.debug("Impossible to send a message to a channel you have not joined.")
            return

        if self.verbose_debug:
            self._LOG.debug("Send message to channel {0}: '{1}'".format(channel_id, message))

        self.send(EDOTAGCMsg.EMsgGCChatMessage, {
            "channel_id": channel_id,
            "text": message
        })

    def share_lobby(self, channel_id):
        """
        Share user lobby in the target channel.

        :param channel_id: id of the channel to share the lobby into
        :type channel_id: :class: `int`
        """
        if self.lobby is None:
            if self.verbose_debug:
                self._LOG.debug("Impossible to share lobby if not inside a lobby.")
            return

        channel = self.channels.get(channel_id)
        if channel is None:
            if self.verbose_debug:
                self._LOG.debug("Impossible to share lobby in a channel not joined.")
            return

        self.send(EDOTAGCMsg.EMsgGCChatMessage, {
            "channel_id": channel_id,
            "share_lobby_id": self.lobby.lobby_id,
            "share_lobby_passkey": self.lobby.pass_key
        })

    def flip_coin(self, channel_id):
        """
        Flip a coin in the target lobby.

        :param channel_id: id of the channel to share a coin into
        :type channel_id: :class: `int`
        """
        channel = self.channels.get(channel_id)
        if channel is None:
            if self.verbose_debug:
                self._LOG.debug("Impossible to flip a coin channel not joined.")
            return

        self.send(EDOTAGCMsg.EMsgGCChatMessage, {
            "channel_id": channel_id,
            "coin_flip": True
        })

    def roll_dice(self, channel_id, min=1, max=100):
        """
        Roll a dice in the target lobby.

        :param channel_id: id of the channel to roll a dice into
        :type channel_id: :class: `int`
        :param min: dice starting value
        :type min: :class: `int`
        :param max: dice ending value
        :type max: :class: `int`
        """
        channel = self.channels.get(channel_id)
        if channel is None:
            if self.verbose_debug:
                self._LOG.debug("Impossible to roll a dice in a channel not joined.")
            return

        self.send(EDOTAGCMsg.EMsgGCChatMessage, {
            "channel_id": channel_id,
            "dice_roll": {
                "roll_min": min,
                "roll_max": max
            }
        })

    def request_chat_channels(self):
        """
        Requests a list of chat channels from the GC.

        :return List of chat channels
        :rtype `EMsgGCRequestChatChannelListResponse`
        """
        if self.verbose_debug:
            self._LOG.debug("Requesting channel list from GC.")

        jobid = self.send_job(EDOTAGCMsg.EMsgGCRequestChatChannelList, {})
        resp = self.wait_msg(jobid, timeout=10)

        return resp
