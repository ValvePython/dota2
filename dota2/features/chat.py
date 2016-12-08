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

    def __chat_cleanup(self):
        self.channels = {}

    def __handle_channel_join(self, message):
        self.channels[message.channel_id] = message
        self.emit(self.EVENT_CHANNEL_JOIN, message)

    def __handle_channel_message(self, message):
        self.emit(self.EVENT_CHANNEL_MESSAGE, message)

    def join_channel(self, channel_name, channel_type=DOTAChatChannelType_t.DOTAChannelType_Custom):
        """Send a join channel requests to the GC.

        :param channel_name: Name of the channel to join
        :type channel_name: :class: `str`
        :param channel_type: Type of channel to join
        :type channel_type: :class: `DOTAChatChannelType_t`

        Response event: ``channel_join``

        :param message: `EMsgGCJoinChatChannelResponse <>
        :type  message: proto message
        """
        if self.verbose_debug:
            self._LOG.debug("Joining chat channel: {0}".format(channel_name))

        self.send(EDOTAGCMsg.EMsgGCJoinChatChannel, {
            "channel_name": channel_name,
            "channel_type": channel_type
        })

    def leave_channel(self, channel_id):
        """Send a leave channel requests to the GC.

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

    def send_message(self, channel_id, message):
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

    def share_lobby(self, channel_name, channel_type):
        pass

    def flip_coin(self, channel_name, channel_type):
        pass

    def roll_dice(self, channel_name, channel_type, min, max):
        pass

    def request_chat_channels(self):
        """Requests a list of chat channels from the GC.

        :return
        :rtype
        """
        if self.verbose_debug:
            self._LOG.debug("Requesting channel list from GC.")

        jobid = self.send_job(EDOTAGCMsg.EMsgGCRequestChatChannelList, {})
        resp = self.wait_msg(jobid, timeout=10)

        return resp
