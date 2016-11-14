from dota2.enums import ESOType, EGCBaseMsg, EDOTAGCMsg
from dota2.enums import DOTA_GC_TEAM, DOTABotDifficulty


class Lobby(object):
    EVENT_LOBBY_INVITE = 'lobby_invite'
    """When a lobby invite is received
    :param message: `CSDOTALobbyInvite <https://github.com/ValvePython/dota2/blob/ca75440adca20d852b9aec3917e4387466848d5b/protobufs/dota_gcmessages_common_match_management.proto#L100>`_
    :type message: proto message
    """
    EVENT_LOBBY_INVITE_REMOVED = 'lobby_invite_removed'
    """When a lobby invite is no longer valid
    :param message: `CSDOTALobbyInvite <https://github.com/ValvePython/dota2/blob/ca75440adca20d852b9aec3917e4387466848d5b/protobufs/dota_gcmessages_common_match_management.proto#L100>`_
    :type message: proto message
    """
    EVENT_LOBBY_NEW = 'lobby_new'
    """Entered a lobby, either by creating one or accepting an invite

    :param message: `CSODOTALobby <https://github.com/ValvePython/dota2/blob/ca75440adca20d852b9aec3917e4387466848d5b/protobufs/dota_gcmessages_common_match_management.proto#L193>`_
    :type message: proto message
    """
    EVENT_LOBBY_CHANGED = 'lobby_changed'
    """Anything changes to the lobby state, players, options, broadcasters...

    :param message: `CSODOTALobby <https://github.com/ValvePython/dota2/blob/ca75440adca20d852b9aec3917e4387466848d5b/protobufs/dota_gcmessages_common_match_management.proto#L193>`_
    :type message: proto message
    """
    EVENT_LOBBY_REMOVED = 'lobby_removed'
    """The lobby is not valid anymore, quit or kick.

    :param message: `CSODOTALobby <https://github.com/ValvePython/dota2/blob/ca75440adca20d852b9aec3917e4387466848d5b/protobufs/dota_gcmessages_common_match_management.proto#L193>`_
    :type message: proto message
    """

    lobby = None

    def __init__(self):
        super(Lobby, self).__init__()
        self.socache.on(('new', ESOType.CSODOTALobbyInvite), self.__handle_lobby_invite)
        self.socache.on(('removed', ESOType.CSODOTALobbyInvite), self.__handle_lobby_invite_removed)

        self.socache.on(('new', ESOType.CSODOTALobby), self.__handle_lobby_new)
        self.socache.on(('updated', ESOType.CSODOTALobby), self.__handle_lobby_changed)
        self.socache.on(('removed', ESOType.CSODOTALobby), self.__handle_lobby_removed)

    def __lobby_cleanup(self):
        self.lobby = None

    def __handle_lobby_invite(self, message):
        self.emit(self.EVENT_LOBBY_INVITE, message)

    def __handle_lobby_invite_removed(self, message):
        self.emit(self.EVENT_LOBBY_INVITE_REMOVED, message)

    def __handle_lobby_new(self, message):
        self.lobby = message
        self.emit(self.EVENT_LOBBY_NEW, message)

    def __handle_lobby_changed(self, message):
        self.lobby = message
        self.emit(self.EVENT_LOBBY_CHANGED, message)

    def __handle_lobby_removed(self, message):
        self.lobby = None
        self.emit(self.EVENT_LOBBY_REMOVED, message)

    def create_practice_lobby(self, password="", options=None):
        """
        Sends a message to the Game Coordinator requesting to create a lobby.

        :param password: password of lobby
        :type password: :class:`str`
        :param options: options
        :type options: :class:`dict`
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

        self.send(EDOTAGCMsg.EMsgGCPracticeLobbyCreate, command)

    def config_practice_lobby(self, lobby_id, options=None):
        options = {} if options is None else options
        raise NotImplementedError()

    def request_practice_lobby_list(self):
        raise NotImplementedError()

    def request_friend_practice_lobby_list(self):
        raise NotImplementedError()

    def balanced_shuffle_lobby(self):
        """
        Balance shuffle the the lobby.
        """
        if self.verbose_debug:
            self._LOG.debug("Balance shuffle the the lobby")

        self.send(EDOTAGCMsg.EMsgGCBalancedShuffleLobby, {})

    def flip_lobby_teams(self):
        """
        Flip both teams of the lobby.
        """
        if self.verbose_debug:
            self._LOG.debug("Flipping teams of the lobby")

        self.send(EDOTAGCMsg.EMsgGCFlipLobbyTeams, {})

    def invite_to_lobby(self, steam_id):
        """
        Asks to invite a player to your lobby. This creates a new default lobby when you are not already in one.

        :param steam_id: steam_id
        :type steam_id: :class:`int`
        """
        if self.verbose_debug:
            self._LOG.debug("Inviting %s to a lobby." % steam_id)

        self.send(EGCBaseMsg.EMsgGCInviteToLobby, {
            "steam_id": steam_id
        })

    def practice_lobby_kick(self, account_id):
        """
        Kick a player from the lobby.

        :param account_id: steam_id
        :type account_id: :class:`int`
        """
        if self.verbose_debug:
            self._LOG.debug("Kicking %s from the lobby." % account_id)

        self.send(EDOTAGCMsg.EMsgGCPracticeLobbyKick, {
            "account_id": account_id
        })

    def practice_lobby_kick_from_team(self, account_id):
        """
        Kick a player from the his current lobby team.

        :param account_id: account_id
        :type account_id: :class:`int`
        """
        if self.verbose_debug:
            self._LOG.debug("Kicking %s from his lobby team." % account_id)

        self.send(EDOTAGCMsg.EMsgGCPracticeLobbyKickFromTeam, {
            "account_id": account_id
        })

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

        self.send(EDOTAGCMsg.EMsgGCPracticeLobbyLeave, {})

    def abandon_current_game(self):
        raise NotImplementedError()

    def launch_practice_lobby(self):
        raise NotImplementedError()

    def join_practice_lobby_team(self, slot=1, team=DOTA_GC_TEAM.PLAYER_POOL):
        """
        Join on of the lobby team at the specified slot.

        :param slot: slot to join into
        :type slot: :class:`int`
        :param team: team to join
        :type team: :class:`DOTA_GC_TEAM`
        """
        if self.verbose_debug:
            self._LOG.debug("Joining slot %s of lobby team %s." % (slot, team))

        self.send(EDOTAGCMsg.EMsgGCPracticeLobbySetTeamSlot, {
            "team": team,
            "slot": slot
        })

    def join_practice_lobby_broadcast_channel(self, channel):
        raise NotImplementedError()

    def add_bot_to_practice_lobby(self, slot=1, team=DOTA_GC_TEAM.GOOD_GUYS, bot_difficulty=DOTABotDifficulty.BOT_DIFFICULTY_PASSIVE):
        """
        Add a bot in the lobby.

        :param slot: slot to join into
        :type slot: :class:`int`
        :param team: team to join
        :type team: :class:`DOTA_GC_TEAM`
        :param bot_difficulty: difficulty of the bot
        :type bot_difficulty: :class:`DOTABotDifficulty`
        """
        if self.verbose_debug:
            self._LOG.debug("Adding a bot %s in slot %s of lobby team %s." % (bot_difficulty, slot, team))

        self.send(EDOTAGCMsg.EMsgGCPracticeLobbySetTeamSlot, {
            "team": team,
            "slot": slot,
            "bot_difficulty": bot_difficulty
        })

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
