from dota2.enums import ESOType, EGCBaseMsg, EDOTAGCMsg


class Lobby(object):
    EVENT_LOBBY_INVITE = 'lobby_invite'
    """When a lobby invite is received
    :param message: `CSDOTALobbyInvite <https://github.com/ValvePython/dota2/blob/ca75440adca20d852b9aec3917e4387466848d5b/protobufs/dota_gcmessages_common_match_management.proto#L100>`_
    :type message: proto message
    """
    EVENT_NEW_LOBBY = 'new_lobby'
    """Entered a lobby, either by creating one or accepting an invite

    :param message: `CSODOTALobby <https://github.com/ValvePython/dota2/blob/ca75440adca20d852b9aec3917e4387466848d5b/protobufs/dota_gcmessages_common_match_management.proto#L193>`_
    :type message: proto message
    """

    lobby = None
    lobby_invite = None

    def __init__(self):
        super(Lobby, self).__init__()
        self.on(EDOTAGCMsg.EMsgGCPracticeLobbyResponse, self.__handle_practice_lobby_response)

    def __lobby_cleanup(self):
        self.lobby = None
        self.lobby_invite = None

    def __handle_lobby_invite(self, message):
        self.emit('lobby_invite', message)

    def __handle_lobby_new(self, message):
        self.lobby = message
        self.emit('new_lobby', message)

    def __handle_practice_lobby_response(self, message):
        self.emit('practice_lobby_response', message)

    def create_practice_lobby(self, password="", options=None):
        """
        Sends a message to the Game Coordinator requesting to create a lobby.

        :param password: password of lobby
        :type password: :class:`str`
        :param options: options
        :type options: :class:`dict`
        :return: job event id
        :rtype: str

        Response event: ``create_tournament_lobby``

        :param message: `CMsgPracticeLobbyCreate <https://github.com/ValvePython/dota2/blob/ca75440adca20d852b9aec3917e4387466848d5b/protobufs/dota_gcmessages_client_match_management.proto#L134>`_ proto message
        """
        options = {} if options is None else options
        return self.create_tournament_lobby(password, options=options)

    def create_tournament_lobby(self, password="", tournament_game_id=0,
                                tournament_id=0, options=None):
        """
        Sends a message to the Game Coordinator requesting to create a tournament lobby.

        :param password: password of lobby
        :type password: :class:`str`
        :param tournament_game_id: tournament game id
        :type tournament_game_id: :class:`int`
        :param tournament_id: tournament id
        :type tournament_id: :class:`int`
        :param options: options
        :type options: :class:`dict`
        :return: job event id
        :rtype: str

        Response event: ``create_tournament_lobby``

        :param message: `CMsgPracticeLobbyCreate <https://github.com/ValvePython/dota2/blob/ca75440adca20d852b9aec3917e4387466848d5b/protobufs/dota_gcmessages_client_match_management.proto#L134>`_ proto message
        """
        options = {} if options is None else options
        options["pass_key"] = password
        if self.verbose_debug:
            self._LOG.debug("Sending match CMsgPracticeLobbyCreate request")

        command = {
            "lobby_details": options,
            "pass_key": password
        }
        if tournament_game_id > 0:
            command.update({
                "tournament_game": True,
                "tournament_game_id": tournament_game_id,
                "tournament_id": tournament_id
            })
        jobid = self.send_job(EDOTAGCMsg.EMsgGCPracticeLobbyCreate, command)

        @self.once(jobid)
        def wrap_create_tournament_lobby(message):
            self.emit('create_tournament_lobby', message)

        return jobid

    def config_practice_lobby(self, lobby_id, options=None):
        options = {} if options is None else options
        raise NotImplementedError()

    def request_practice_lobby_list(self):
        raise NotImplementedError()

    def request_friend_practice_lobby_list(self):
        raise NotImplementedError()

    def balanced_shuffle_lobby(self):
        raise NotImplementedError()

    def flip_lobby_teams(self):
        raise NotImplementedError()

    def invite_to_lobby(self, steam_id):
        """
        Asks to invite a player to your lobby. This creates a new default lobby when you are not already in one.

        :param steam_id: steam_id
        :type steam_id: :class:`int`
        :return: job event id
        :rtype: str

        Response event: ``create_invite_to_lobby``

        :param message: `CMsgInviteToLobby <https://github.com/ValvePython/dota2/blob/ca75440adca20d852b9aec3917e4387466848d5b/protobufs/base_gcmessages.proto#L88>`_ proto message
        """
        import ipdb; ipdb.set_trace()
        if self.verbose_debug:
            self._LOG.debug("Inviting %s to a lobby." % steam_id)

        jobid = self.send_job(EGCBaseMsg.EMsgGCInviteToLobby, {
            "steam_id": steam_id
        })

        @self.once(jobid)
        def wrap_create_invite_to_lobby(message):
            self.emit('create_invite_to_lobby', message)

        return jobid

    def practice_lobby_kick(self, account_id):
        raise NotImplementedError()

    def practice_lobby_kick_from_team(self, account_id):
        raise NotImplementedError()

    def join_practice_lobby(self, id, password):
        raise NotImplementedError()

    def leave_practice_lobby(self):
        """
        Sends a message to the Game Coordinator requesting to leave the current lobby.

        :return: job event id
        :rtype: str

        Response event: ``leave_practice_lobby``

        :param message: `CMsgPracticeLobbyLeave <https://github.com/ValvePython/dota2/blob/ca75440adca20d852b9aec3917e4387466848d5b/protobufs/dota_gcmessages_client_match_management.proto#L181>`_ proto message
        """
        if self.verbose_debug:
            self._LOG.debug("Sending match CMsgPracticeLobbyLeave request")

        jobid = self.send_job(EDOTAGCMsg.EMsgGCPracticeLobbyLeave, {})

        @self.once(jobid)
        def wrap_leave_practice_lobby(message):
            self.emit('leave_practice_lobby', message)

        return jobid

    def abandon_current_game(self):
        raise NotImplementedError()

    def launch_practice_lobby(self):
        raise NotImplementedError()

    def join_practice_lobby_team(self, slot, team):
        raise NotImplementedError()

    def join_practice_lobby_broadcast_channel(self, channel):
        raise NotImplementedError()

    def add_bot_to_practice_lobby(self, slot, team, bot_difficulty):
        raise NotImplementedError()

    def respond_lobby_invite(self, id, accept=False):
        """
        Answer to a lobby invite.
        :param id: lobby_id to answer to.
        :param accept: answer to the lobby invite
        """
        if self.verbose_debug:
            self._LOG.debug("Responding to lobby invite %s, accept: %s" % (id, accept))

        self.send(EGCBaseMsg.EMsgGCLobbyInviteResponse, {
            "lobby_id": id,
            "accept": accept
        })
