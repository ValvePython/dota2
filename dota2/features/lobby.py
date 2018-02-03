from dota2.enums import ESOType, EGCBaseMsg, EDOTAGCMsg, DOTA_GameMode, EServerRegion
from dota2.enums import DOTAJoinLobbyResult, DOTA_GC_TEAM, DOTABotDifficulty


class Lobby(object):
    EVENT_LOBBY_INVITE = 'lobby_invite'
    """When a lobby invite is received
    :param message: `CSDOTALobbyInvite <https://github.com/ValvePython/dota2/blob/ca75440adca20d852b9aec3917e4387466848d5b/protobufs/dota_gcmessages_common_match_management.proto#L100>`_
    :type  message: proto message
    """
    EVENT_LOBBY_INVITE_REMOVED = 'lobby_invite_removed'
    """When a lobby invite is no longer valid
    :param message: `CSDOTALobbyInvite <https://github.com/ValvePython/dota2/blob/ca75440adca20d852b9aec3917e4387466848d5b/protobufs/dota_gcmessages_common_match_management.proto#L100>`_
    :type  message: proto message
    """
    EVENT_LOBBY_NEW = 'lobby_new'
    """Entered a lobby, either by creating one or accepting an invite

    :param message: `CSODOTALobby <https://github.com/ValvePython/dota2/blob/ca75440adca20d852b9aec3917e4387466848d5b/protobufs/dota_gcmessages_common_match_management.proto#L193>`_
    :type  message: proto message
    """
    EVENT_LOBBY_CHANGED = 'lobby_changed'
    """Anything changes to the lobby state, players, options, broadcasters...

    :param message: `CSODOTALobby <https://github.com/ValvePython/dota2/blob/ca75440adca20d852b9aec3917e4387466848d5b/protobufs/dota_gcmessages_common_match_management.proto#L193>`_
    :type  message: proto message
    """
    EVENT_LOBBY_REMOVED = 'lobby_removed'
    """The lobby is not valid anymore, quit or kick.

    :param message: `CSODOTALobby <https://github.com/ValvePython/dota2/blob/ca75440adca20d852b9aec3917e4387466848d5b/protobufs/dota_gcmessages_common_match_management.proto#L193>`_
    :type  message: proto message
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
        :type  password: :class:`str`
        :param options: options to setup the lobby with
        :type  options: :class:`dict`
        """
        return self.create_tournament_lobby(password=password, options=options)

    def create_tournament_lobby(self, password="", tournament_game_id=None, tournament_id=0, options=None):
        """
        Sends a message to the Game Coordinator requesting to create a tournament lobby.

        :param password: password of lobby
        :type  password: :class:`str`
        :param tournament_game_id: tournament game id
        :type  tournament_game_id: :class:`int`
        :param tournament_id: tournament id
        :type  tournament_id: :class:`int`
        :param options: options to setup the lobby with
        :type  options: :class:`dict`
        """
        options = {} if options is None else options
        options["pass_key"] = password

        command = {
            "lobby_details": options,
            "pass_key": password
        }
        if tournament_game_id is not None:
            command.update({
                "tournament_game": True,
                "tournament_game_id": tournament_game_id,
                "tournament_id": tournament_id
            })

        if self.verbose_debug:
            self._LOG.debug("Sending match CMsgPracticeLobbyCreate request")

        self.send(EDOTAGCMsg.EMsgGCPracticeLobbyCreate, command)

    def config_practice_lobby(self, options):
        """
        Change settings of the current lobby.

        :param options: options to change in the lobby
        :type  options: :class:`dict`
        """
        if self.lobby is None or self.lobby.leader_id != self.steam.steam_id:
            return

        options = {} if options is None else options
        options['lobby_id'] = self.lobby.lobby_id

        if self.verbose_debug:
            self._LOG.debug("Changing lobby options of lobby %s", self.lobby.lobby_id)

        self.send(EDOTAGCMsg.EMsgGCPracticeLobbySetDetails, options)

    def get_lobby_list(self, server_region=EServerRegion.Unspecified, game_mode=DOTA_GameMode.DOTA_GAMEMODE_NONE):
        """
        Get a lobby list

        .. note::
            These are regular lobbies. (e.g. All pick, Captains Mode, etc)

        :param server_region: limit to a specific server region
        :type  server_region: :class:`.EServerRegion`
        :param game_mode: limit to specific game mode, ``DOTA_GAMEMODE_NONE`` means any
        :type  game_mode: :class:`.DOTA_GameMode`
        :return: List of `CMsgPracticeLobbyListResponseEntry <https://github.com/ValvePython/dota2/blob/ca75440adca20d852b9aec3917e4387466848d5b/protobufs/dota_gcmessages_client_match_management.proto#L202-L226>`_
        :rtype: proto message, :class:`None`
        """
        if self.verbose_debug:
            self._LOG.debug("Requesting lobby list.")

        jobid = self.send(EDOTAGCMsg.EMsgGCLobbyList,
                          {
                             'server_region': server_region,
                             'game_mode': game_mode,
                          })

        resp = self.wait_msg(EDOTAGCMsg.EMsgGCLobbyListResponse, timeout=10)
        return resp.lobbies if resp else None

    def get_practice_lobby_list(self, tournament_games=False, password=''):
        """
        Get list of practice lobbies

        .. note::
            These are private Custom Game lobbies

        :param tournament_games: whether to show tournament games only
        :type  tournament_games: :class:`bool`
        :param password: practice lobbies with this password
        :type  password: :class:`str`
        :return: List of `CMsgPracticeLobbyListResponseEntry <https://github.com/ValvePython/dota2/blob/ca75440adca20d852b9aec3917e4387466848d5b/protobufs/dota_gcmessages_client_match_management.proto#L202-L226>`_
        :rtype: proto message, :class:`None`
        """
        if self.verbose_debug:
            self._LOG.debug("Requesting practice lobby list.")

        jobid = self.send_job(EDOTAGCMsg.EMsgGCPracticeLobbyList,
                             {
                                'tournament_games': tournament_games,
                                'pass_key': password,
                             })

        resp = self.wait_msg(jobid, timeout=10)
        return resp.lobbies if resp else None

    def get_friend_practice_lobby_list(self):
        """
        Request a list of friend practice lobbies.

        :return: List of `CMsgPracticeLobbyListResponseEntry <https://github.com/ValvePython/dota2/blob/ca75440adca20d852b9aec3917e4387466848d5b/protobufs/dota_gcmessages_client_match_management.proto#L202-L226>`_
        :rtype: proto message, :class:`None`
        """
        if self.verbose_debug:
            self._LOG.debug("Requesting friend practice lobby list.")

        jobid = self.send_job(EDOTAGCMsg.EMsgGCFriendPracticeLobbyListRequest, {})
        resp = self.wait_msg(jobid, timeout=10)

        return resp.lobbies if resp else None

    def balanced_shuffle_lobby(self):
        """
        Balance shuffle the the lobby.
        """
        if self.lobby is None or self.lobby.leader_id != self.steam.steam_id:
            return

        if self.verbose_debug:
            self._LOG.debug("Balance shuffle the the lobby")

        self.send(EDOTAGCMsg.EMsgGCBalancedShuffleLobby, {})

    def flip_lobby_teams(self):
        """
        Flip both teams of the lobby.
        """
        if self.lobby is None or self.lobby.leader_id != self.steam.steam_id:
            return

        if self.verbose_debug:
            self._LOG.debug("Flipping teams of the lobby")

        self.send(EDOTAGCMsg.EMsgGCFlipLobbyTeams, {})

    def invite_to_lobby(self, steam_id):
        """
        Asks to invite a player to your lobby. This creates a new default lobby when you are not already in one.

        :param steam_id: steam_id
        :type  steam_id: :class:`int`
        """
        if self.lobby is None:
            return

        if self.verbose_debug:
            self._LOG.debug("Inviting %s to a lobby." % steam_id)

        self.send(EGCBaseMsg.EMsgGCInviteToLobby, {
            "steam_id": steam_id
        })

    def practice_lobby_kick(self, account_id):
        """
        Kick a player from the lobby.

        :param account_id: 32-bit steam_id of the user to kick from the lobby
        :type  account_id: :class:`int`
        """
        if self.lobby is None or self.lobby.leader_id != self.steam.steam_id:
            return

        if self.verbose_debug:
            self._LOG.debug("Kicking %s from the lobby." % account_id)

        self.send(EDOTAGCMsg.EMsgGCPracticeLobbyKick, {
            "account_id": account_id
        })

    def practice_lobby_kick_from_team(self, account_id):
        """
        Kick a player from the his current lobby team.

        :param account_id: 32-bit steam_id of the user to kick from a team
        :type  account_id: :class:`int`
        """
        if self.lobby is None or self.lobby.leader_id != self.steam.steam_id:
            return

        if self.verbose_debug or self.lobby.leader_id != self.steam.steam_id:
            self._LOG.debug("Kicking %s from his lobby team." % account_id)

        self.send(EDOTAGCMsg.EMsgGCPracticeLobbyKickFromTeam, {
            "account_id": account_id
        })

    def join_practice_lobby(self, id, password=""):
        """
        Join the target practice lobby.

        :param id: id of the lobby to join
        :type  id: :class:`int`
        :param password: password necessary to join the lobby
        :type  password: :class:`str`
        :return: Result of the join command from the GC
        :rtype: :class: `DOTAJoinLobbyResult`. `DOTAJoinLobbyResult.DOTA_JOIN_RESULT_TIMEOUT` if timeout
        """
        if self.verbose_debug:
            self._LOG.debug("Trying to join practice lobby %s using password %s" % (id, password))

        jobid = self.send_job(EDOTAGCMsg.EMsgGCPracticeLobbyJoin, {
            "lobby_id": id,
            "pass_key": password
        })
        resp = self.wait_msg(jobid, timeout=10)

        return DOTAJoinLobbyResult(resp.result) if resp else DOTAJoinLobbyResult.DOTA_JOIN_RESULT_TIMEOUT

    def leave_practice_lobby(self):
        """
        Sends a message to the Game Coordinator requesting to leave the current lobby.
        """
        if self.lobby is None:
            return

        if self.verbose_debug:
            self._LOG.debug("Sending match CMsgPracticeLobbyLeave request")

        self.send(EDOTAGCMsg.EMsgGCPracticeLobbyLeave, {})

    def abandon_current_game(self):
        """
        Abandon the current game.
        """
        if self.lobby is None:
            return

        if self.verbose_debug:
            self._LOG.debug("Abandoning current game.")

        self.send(EDOTAGCMsg.EMsgGCAbandonCurrentGame, {})

    def launch_practice_lobby(self):
        """
        Launch the current lobby into a game.
        """
        if self.lobby is None or self.lobby.leader_id != self.steam.steam_id:
            return

        if self.verbose_debug:
            self._LOG.debug("Starting current lobby.")

        self.send(EDOTAGCMsg.EMsgGCPracticeLobbyLaunch, {})

    def join_practice_lobby_team(self, slot=1, team=DOTA_GC_TEAM.PLAYER_POOL):
        """
        Join on of the lobby team at the specified slot.

        :param slot: slot to join into
        :type  slot: :class:`int`
        :param team: team to join
        :type  team: :class:`DOTA_GC_TEAM`
        """
        if self.lobby is None:
            return

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
        :type  channel: :class:`int`
        """
        if self.lobby is None:
            return

        if self.verbose_debug:
            self._LOG.debug("Joining channel %s of lobby broadcst." % channel)

        self.send(EDOTAGCMsg.EMsgGCPracticeLobbyJoinBroadcastChannel, {
            "channel": channel
        })

    def add_bot_to_practice_lobby(self, slot=1, team=DOTA_GC_TEAM.GOOD_GUYS, bot_difficulty=DOTABotDifficulty.BOT_DIFFICULTY_PASSIVE):
        """
        Add a bot in the lobby.

        :param slot: slot to join into
        :type  slot: :class:`int`
        :param team: team to join
        :type  team: :class:`.DOTA_GC_TEAM`
        :param bot_difficulty: difficulty of the bot
        :type  bot_difficulty: :class:`.DOTABotDifficulty`
        """
        if self.lobby is None or self.lobby.leader_id != self.steam.steam_id:
            return

        if self.verbose_debug:
            self._LOG.debug("Adding a bot %s in slot %s of lobby team %s." % (bot_difficulty, slot, team))

        self.send(EDOTAGCMsg.EMsgGCPracticeLobbySetTeamSlot, {
            "team": team,
            "slot": slot,
            "bot_difficulty": bot_difficulty
        })

    def respond_to_lobby_invite(self, lobby_id, accept=False):
        """
        Answer to a lobby invite.

        :param id: lobby_id to answer to.
        :type  id: :class:`int`
        :param accept: answer to the lobby invite
        :type  accept: :class:`bool`
        """
        if self.verbose_debug:
            self._LOG.debug("Responding to lobby invite %s, accept: %s" % (lobby_id, accept))

        self.send(EGCBaseMsg.EMsgGCLobbyInviteResponse, {
            "lobby_id": lobby_id,
            "accept": accept
        })

    def destroy_lobby(self):
        """
        Destroy the current lobby (host only)

        :return: job_id for response
        :rtype: :class:`str`
        """
        if self.verbose_debug:
            self._LOG.debug("Destroying current lobby.")

        return self.send_job(EDOTAGCMsg.EMsgDestroyLobbyRequest, {})
