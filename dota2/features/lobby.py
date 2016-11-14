import inspect

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
    EVENT_LOBBY_JOIN_ANSWER = 'lobby_join_answer'
    """Answer to the join lobby request.

    :param message: `EMsgGCPracticeLobbyJoinResponse <>`_
    :type message: proto message
    """
    EVENT_LOBBY_LIST_ANSWER = 'lobby_list_answer'
    """Answer to the request for lobby list

    :param message: `EMsgGCPracticeLobbyListResponse <>`_
    :type message: proto message
    """
    EVENT_LOBBY_FRIEND_LIST_ANSWER = 'lobby_friend_list_answer'
    """Answer to the request for friend lobby list

    :param message: `EMsgGCFriendPracticeLobbyListResponse <>`_
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

    def config_practice_lobby(self, lobby_id, game_name=None, server_region=None, game_mode=None, game_version=None,
                              cm_pick=None, allow_cheats=None, fill_with_bots=None, allow_spectating=None,
                              pass_key=None, series_type=None, radiant_series_wins=None, dire_series_wins=None,
                              allchat=None, leagueid=None, dota_tv_delay=None, custom_game_mode=None,
                              custom_map_name=None, custom_difficulty=None, custom_game_id=None):
        """
        Change settings of the selected lobby.

        :param lobby_id: target lobby
        :type lobby_id: :class:`int`
        :param game_name: name of the lobby
        :type game_name: :class:`str`
        :param server_region: region to host the game on
        :type server_region: :class:`int`
        :param game_mode: game mode of the region
        :type server_region: :class:`DOTA_GameMode`
        :param game_version: version to use in the lobby
        :type game_version: :class:`DOTAGameVersion`
        ...
        """
        options = {}

        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        for i in args:
            if i == 'self':
                continue
            if values[i] is None:
                continue
            options[i] = values[i]

        self._LOG.debug('%s', options)
        if self.verbose_debug:
            self._LOG.debug("Changing lobby options of lobby %s", lobby_id)

        self.send(EDOTAGCMsg.EMsgGCPracticeLobbySetDetails, options)

    def request_practice_lobby_list(self):
        """
        Request a list of practice lobbies.
        """
        if self.verbose_debug:
            self._LOG.debug("Requesting practice lobby list.")

        jobid = self.send_job(EDOTAGCMsg.EMsgGCPracticeLobbyList, {})

        @self.once(jobid)
        def wrap_lobby_list(message):
            self.emit(self.EVENT_LOBBY_LIST_ANSWER, message)

        return jobid

    def request_friend_practice_lobby_list(self):
        """
        Request a list of friend practice lobbies.
        """
        if self.verbose_debug:
            self._LOG.debug("Requesting friend practice lobby list.")

        jobid = self.send_job(EDOTAGCMsg.EMsgGCFriendPracticeLobbyListRequest, {})

        @self.once(jobid)
        def wrap_lobby_list(message):
            self.emit(self.EVENT_LOBBY_FRIEND_LIST_ANSWER, message)

        return jobid

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

    def join_practice_lobby(self, id, password=""):
        """
        Join the target practice lobby.

        :param id: id of the lobby to join
        :type password: :class:`str` pass phrase of the lobby to join
        """
        if self.verbose_debug:
            self._LOG.debug("Trying to join practice lobby %s using password %s" % (id, password))

        jobid = self.send_job(EDOTAGCMsg.EMsgGCPracticeLobbyJoin, {
            "lobby_id": id,
            "pass_key": password
        })

        @self.once(jobid)
        def wrap_join_lobby(message):
            self.emit(self.EVENT_LOBBY_JOIN_ANSWER, message)

        return jobid

    def leave_practice_lobby(self):
        """
        Sends a message to the Game Coordinator requesting to leave the current lobby.
        """
        if self.verbose_debug:
            self._LOG.debug("Sending match CMsgPracticeLobbyLeave request")

        self.send(EDOTAGCMsg.EMsgGCPracticeLobbyLeave, {})

    def abandon_current_game(self):
        """
        Abandon the current game.
        """
        if self.verbose_debug:
            self._LOG.debug("Abandoning current game.")

        self.send(EDOTAGCMsg.EMsgGCAbandonCurrentGame, {})

    def launch_practice_lobby(self):
        """
        Launch the current lobby into a game.
        """
        if self.verbose_debug:
            self._LOG.debug("Starting current lobby.")

        self.send(EDOTAGCMsg.EMsgGCPracticeLobbyLaunch, {})

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

    def join_practice_lobby_broadcast_channel(self, channel=1):
        """
        Join a specific channel of the broadcasters.

        :param channel: channel to join into
        :type channel: :class:`int`
        :param team: team to join
        :type team: :class:`DOTA_GC_TEAM`
        """
        if self.verbose_debug:
            self._LOG.debug("Joining channel %s of lobby broadcst." % channel)

        self.send(EDOTAGCMsg.EMsgGCPracticeLobbyJoinBroadcastChannel, {
            "channel": channel
        })

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
