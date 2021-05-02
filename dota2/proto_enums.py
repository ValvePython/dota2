from enum import IntEnum

class DOTA_2013PassportSelectionIndices(IntEnum):
    PP13_SEL_ALLSTAR_PLAYER_0 = 0
    PP13_SEL_ALLSTAR_PLAYER_1 = 1
    PP13_SEL_ALLSTAR_PLAYER_2 = 2
    PP13_SEL_ALLSTAR_PLAYER_3 = 3
    PP13_SEL_ALLSTAR_PLAYER_4 = 4
    PP13_SEL_ALLSTAR_PLAYER_5 = 5
    PP13_SEL_ALLSTAR_PLAYER_6 = 6
    PP13_SEL_ALLSTAR_PLAYER_7 = 7
    PP13_SEL_ALLSTAR_PLAYER_8 = 8
    PP13_SEL_ALLSTAR_PLAYER_9 = 9
    PP13_SEL_QUALPRED_WEST_0 = 10
    PP13_SEL_QUALPRED_WEST_1 = 11
    PP13_SEL_QUALPRED_WEST_2 = 12
    PP13_SEL_QUALPRED_WEST_3 = 13
    PP13_SEL_QUALPRED_WEST_4 = 14
    PP13_SEL_QUALPRED_WEST_5 = 15
    PP13_SEL_QUALPRED_WEST_6 = 16
    PP13_SEL_QUALPRED_WEST_7 = 17
    PP13_SEL_QUALPRED_WEST_8 = 18
    PP13_SEL_QUALPRED_WEST_9 = 19
    PP13_SEL_QUALPRED_WEST_10 = 20
    PP13_SEL_QUALPRED_WEST_11 = 21
    PP13_SEL_QUALPRED_WEST_12 = 22
    PP13_SEL_QUALPRED_WEST_13 = 23
    PP13_SEL_QUALPRED_WEST_14 = 24
    PP13_SEL_QUALPRED_EAST_0 = 25
    PP13_SEL_QUALPRED_EAST_1 = 26
    PP13_SEL_QUALPRED_EAST_2 = 27
    PP13_SEL_QUALPRED_EAST_3 = 28
    PP13_SEL_QUALPRED_EAST_4 = 29
    PP13_SEL_QUALPRED_EAST_5 = 30
    PP13_SEL_QUALPRED_EAST_6 = 31
    PP13_SEL_QUALPRED_EAST_7 = 32
    PP13_SEL_QUALPRED_EAST_8 = 33
    PP13_SEL_QUALPRED_EAST_9 = 34
    PP13_SEL_QUALPRED_EAST_10 = 35
    PP13_SEL_QUALPRED_EAST_11 = 36
    PP13_SEL_QUALPRED_EAST_12 = 37
    PP13_SEL_QUALPRED_EAST_13 = 38
    PP13_SEL_QUALPRED_EAST_14 = 39
    PP13_SEL_TEAMCUP_TEAM = 40
    PP13_SEL_TEAMCUP_PLAYER = 41
    PP13_SEL_TEAMCUP_TEAM_LOCK = 42
    PP13_SEL_TEAMCUP_PLAYER_LOCK = 43
    PP13_SEL_EVENTPRED_0 = 44
    PP13_SEL_EVENTPRED_1 = 45
    PP13_SEL_EVENTPRED_2 = 46
    PP13_SEL_EVENTPRED_3 = 47
    PP13_SEL_EVENTPRED_4 = 48
    PP13_SEL_EVENTPRED_5 = 49
    PP13_SEL_EVENTPRED_6 = 50
    PP13_SEL_EVENTPRED_7 = 51
    PP13_SEL_EVENTPRED_8 = 52
    PP13_SEL_EVENTPRED_9 = 53
    PP13_SEL_EVENTPRED_10 = 54
    PP13_SEL_EVENTPRED_11 = 55
    PP13_SEL_EVENTPRED_12 = 56
    PP13_SEL_EVENTPRED_13 = 57
    PP13_SEL_EVENTPRED_14 = 58
    PP13_SEL_EVENTPRED_15 = 59
    PP13_SEL_EVENTPRED_16 = 60
    PP13_SEL_EVENTPRED_17 = 61
    PP13_SEL_EVENTPRED_18 = 62
    PP13_SEL_EVENTPRED_19 = 63
    PP13_SEL_EVENTPRED_20 = 64
    PP13_SEL_EVENTPRED_21 = 65
    PP13_SEL_EVENTPRED_22 = 66
    PP13_SEL_EVENTPRED_23 = 67
    PP13_SEL_EVENTPRED_24 = 68
    PP13_SEL_EVENTPRED_25 = 69
    PP13_SEL_EVENTPRED_26 = 70
    PP13_SEL_EVENTPRED_27 = 71
    PP13_SEL_EVENTPRED_28 = 72
    PP13_SEL_EVENTPRED_29 = 73
    PP13_SEL_EVENTPRED_30 = 74
    PP13_SEL_EVENTPRED_31 = 75
    PP13_SEL_EVENTPRED_32 = 76
    PP13_SEL_EVENTPRED_33 = 77
    PP13_SEL_EVENTPRED_34 = 78
    PP13_SEL_EVENTPRED_35 = 79
    PP13_SEL_EVENTPRED_36 = 80
    PP13_SEL_EVENTPRED_37 = 81
    PP13_SEL_EVENTPRED_38 = 82
    PP13_SEL_EVENTPRED_39 = 83
    PP13_SEL_EVENTPRED_40 = 84
    PP13_SEL_EVENTPRED_41 = 85
    PP13_SEL_EVENTPRED_42 = 86
    PP13_SEL_EVENTPRED_43 = 87
    PP13_SEL_SOLO_0 = 88
    PP13_SEL_SOLO_1 = 89
    PP13_SEL_SOLO_2 = 90
    PP13_SEL_SOLO_3 = 91
    PP13_SEL_SOLO_4 = 92
    PP13_SEL_SOLO_5 = 93
    PP13_SEL_SOLO_6 = 94
    PP13_SEL_SOLO_7 = 95

class DOTA_BOT_MODE(IntEnum):
    NONE = 0
    LANING = 1
    ATTACK = 2
    ROAM = 3
    RETREAT = 4
    SECRET_SHOP = 5
    SIDE_SHOP = 6
    RUNE = 7
    PUSH_TOWER_TOP = 8
    PUSH_TOWER_MID = 9
    PUSH_TOWER_BOT = 10
    DEFEND_TOWER_TOP = 11
    DEFEND_TOWER_MID = 12
    DEFEND_TOWER_BOT = 13
    ASSEMBLE = 14
    ASSEMBLE_WITH_HUMANS = 15
    TEAM_ROAM = 16
    FARM = 17
    DEFEND_ALLY = 18
    EVASIVE_MANEUVERS = 19
    ROSHAN = 20
    ITEM = 21
    WARD = 22
    COMPANION = 23
    TUTORIAL_BOSS = 24
    MINION = 25
    OUTPOST = 26

class DOTA_CM_PICK(IntEnum):
    DOTA_CM_RANDOM = 0
    DOTA_CM_GOOD_GUYS = 1
    DOTA_CM_BAD_GUYS = 2

class DOTA_COMBATLOG_TYPES(IntEnum):
    DOTA_COMBATLOG_INVALID = -1
    DOTA_COMBATLOG_DAMAGE = 0
    DOTA_COMBATLOG_HEAL = 1
    DOTA_COMBATLOG_MODIFIER_ADD = 2
    DOTA_COMBATLOG_MODIFIER_REMOVE = 3
    DOTA_COMBATLOG_DEATH = 4
    DOTA_COMBATLOG_ABILITY = 5
    DOTA_COMBATLOG_ITEM = 6
    DOTA_COMBATLOG_LOCATION = 7
    DOTA_COMBATLOG_GOLD = 8
    DOTA_COMBATLOG_GAME_STATE = 9
    DOTA_COMBATLOG_XP = 10
    DOTA_COMBATLOG_PURCHASE = 11
    DOTA_COMBATLOG_BUYBACK = 12
    DOTA_COMBATLOG_ABILITY_TRIGGER = 13
    DOTA_COMBATLOG_PLAYERSTATS = 14
    DOTA_COMBATLOG_MULTIKILL = 15
    DOTA_COMBATLOG_KILLSTREAK = 16
    DOTA_COMBATLOG_TEAM_BUILDING_KILL = 17
    DOTA_COMBATLOG_FIRST_BLOOD = 18
    DOTA_COMBATLOG_MODIFIER_STACK_EVENT = 19
    DOTA_COMBATLOG_NEUTRAL_CAMP_STACK = 20
    DOTA_COMBATLOG_PICKUP_RUNE = 21
    DOTA_COMBATLOG_REVEALED_INVISIBLE = 22
    DOTA_COMBATLOG_HERO_SAVED = 23
    DOTA_COMBATLOG_MANA_RESTORED = 24
    DOTA_COMBATLOG_HERO_LEVELUP = 25
    DOTA_COMBATLOG_BOTTLE_HEAL_ALLY = 26
    DOTA_COMBATLOG_ENDGAME_STATS = 27
    DOTA_COMBATLOG_INTERRUPT_CHANNEL = 28
    DOTA_COMBATLOG_ALLIED_GOLD = 29
    DOTA_COMBATLOG_AEGIS_TAKEN = 30
    DOTA_COMBATLOG_MANA_DAMAGE = 31
    DOTA_COMBATLOG_PHYSICAL_DAMAGE_PREVENTED = 32
    DOTA_COMBATLOG_UNIT_SUMMONED = 33
    DOTA_COMBATLOG_ATTACK_EVADE = 34
    DOTA_COMBATLOG_TREE_CUT = 35
    DOTA_COMBATLOG_SUCCESSFUL_SCAN = 36
    DOTA_COMBATLOG_END_KILLSTREAK = 37
    DOTA_COMBATLOG_BLOODSTONE_CHARGE = 38
    DOTA_COMBATLOG_CRITICAL_DAMAGE = 39
    DOTA_COMBATLOG_SPELL_ABSORB = 40
    DOTA_COMBATLOG_UNIT_TELEPORTED = 41
    DOTA_COMBATLOG_KILL_EATER_EVENT = 42

class DOTA_GameMode(IntEnum):
    DOTA_GAMEMODE_NONE = 0
    DOTA_GAMEMODE_AP = 1
    DOTA_GAMEMODE_CM = 2
    DOTA_GAMEMODE_RD = 3
    DOTA_GAMEMODE_SD = 4
    DOTA_GAMEMODE_AR = 5
    DOTA_GAMEMODE_INTRO = 6
    DOTA_GAMEMODE_HW = 7
    DOTA_GAMEMODE_REVERSE_CM = 8
    DOTA_GAMEMODE_XMAS = 9
    DOTA_GAMEMODE_TUTORIAL = 10
    DOTA_GAMEMODE_MO = 11
    DOTA_GAMEMODE_LP = 12
    DOTA_GAMEMODE_POOL1 = 13
    DOTA_GAMEMODE_FH = 14
    DOTA_GAMEMODE_CUSTOM = 15
    DOTA_GAMEMODE_CD = 16
    DOTA_GAMEMODE_BD = 17
    DOTA_GAMEMODE_ABILITY_DRAFT = 18
    DOTA_GAMEMODE_EVENT = 19
    DOTA_GAMEMODE_ARDM = 20
    DOTA_GAMEMODE_1V1MID = 21
    DOTA_GAMEMODE_ALL_DRAFT = 22
    DOTA_GAMEMODE_TURBO = 23
    DOTA_GAMEMODE_MUTATION = 24
    DOTA_GAMEMODE_COACHES_CHALLENGE = 25

class DOTA_GameState(IntEnum):
    DOTA_GAMERULES_STATE_INIT = 0
    DOTA_GAMERULES_STATE_WAIT_FOR_PLAYERS_TO_LOAD = 1
    DOTA_GAMERULES_STATE_HERO_SELECTION = 2
    DOTA_GAMERULES_STATE_STRATEGY_TIME = 3
    DOTA_GAMERULES_STATE_PRE_GAME = 4
    DOTA_GAMERULES_STATE_GAME_IN_PROGRESS = 5
    DOTA_GAMERULES_STATE_POST_GAME = 6
    DOTA_GAMERULES_STATE_DISCONNECT = 7
    DOTA_GAMERULES_STATE_TEAM_SHOWCASE = 8
    DOTA_GAMERULES_STATE_CUSTOM_GAME_SETUP = 9
    DOTA_GAMERULES_STATE_WAIT_FOR_MAP_TO_LOAD = 10
    DOTA_GAMERULES_STATE_LAST = 11

class DOTA_GC_TEAM(IntEnum):
    GOOD_GUYS = 0
    BAD_GUYS = 1
    BROADCASTER = 2
    SPECTATOR = 3
    PLAYER_POOL = 4
    NOTEAM = 5

class DOTA_TournamentEvents(IntEnum):
    TE_FIRST_BLOOD = 0
    TE_GAME_END = 1
    TE_MULTI_KILL = 2
    TE_HERO_DENY = 3
    TE_AEGIS_DENY = 4
    TE_AEGIS_STOLEN = 5
    TE_GODLIKE = 6
    TE_COURIER_KILL = 7
    TE_ECHOSLAM = 8
    TE_RAPIER = 9
    TE_EARLY_ROSHAN = 10
    TE_BLACK_HOLE = 11

class DOTA_WatchReplayType(IntEnum):
    DOTA_WATCH_REPLAY_NORMAL = 0
    DOTA_WATCH_REPLAY_HIGHLIGHTS = 1

class DOTABotDifficulty(IntEnum):
    BOT_DIFFICULTY_PASSIVE = 0
    BOT_DIFFICULTY_EASY = 1
    BOT_DIFFICULTY_MEDIUM = 2
    BOT_DIFFICULTY_HARD = 3
    BOT_DIFFICULTY_UNFAIR = 4
    BOT_DIFFICULTY_INVALID = 5
    BOT_DIFFICULTY_EXTRA1 = 6
    BOT_DIFFICULTY_EXTRA2 = 7
    BOT_DIFFICULTY_EXTRA3 = 8
    BOT_DIFFICULTY_NPX = 9

class DOTAChatChannelType_t(IntEnum):
    DOTAChannelType_Regional = 0
    DOTAChannelType_Custom = 1
    DOTAChannelType_Party = 2
    DOTAChannelType_Lobby = 3
    DOTAChannelType_Team = 4
    DOTAChannelType_Guild = 5
    DOTAChannelType_Fantasy = 6
    DOTAChannelType_Whisper = 7
    DOTAChannelType_Console = 8
    DOTAChannelType_Tab = 9
    DOTAChannelType_Invalid = 10
    DOTAChannelType_GameAll = 11
    DOTAChannelType_GameAllies = 12
    DOTAChannelType_GameSpectator = 13
    DOTAChannelType_GameCoaching = 14
    DOTAChannelType_Cafe = 15
    DOTAChannelType_CustomGame = 16
    DOTAChannelType_Private = 17
    DOTAChannelType_PostGame = 18
    DOTAChannelType_BattleCup = 19
    DOTAChannelType_HLTVSpectator = 20
    DOTAChannelType_GameEvents = 21
    DOTAChannelType_Trivia = 22
    DOTAChannelType_NewPlayer = 23
    DOTAChannelType_PrivateCoaching = 24

class DOTAConnectionState_t(IntEnum):
    DOTA_CONNECTION_STATE_UNKNOWN = 0
    DOTA_CONNECTION_STATE_NOT_YET_CONNECTED = 1
    DOTA_CONNECTION_STATE_CONNECTED = 2
    DOTA_CONNECTION_STATE_DISCONNECTED = 3
    DOTA_CONNECTION_STATE_ABANDONED = 4
    DOTA_CONNECTION_STATE_LOADING = 5
    DOTA_CONNECTION_STATE_FAILED = 6

class DOTAGameVersion(IntEnum):
    GAME_VERSION_CURRENT = 0
    GAME_VERSION_STABLE = 1

class DOTAJoinLobbyResult(IntEnum):
    DOTA_JOIN_RESULT_SUCCESS = 0
    DOTA_JOIN_RESULT_ALREADY_IN_GAME = 1
    DOTA_JOIN_RESULT_INVALID_LOBBY = 2
    DOTA_JOIN_RESULT_INCORRECT_PASSWORD = 3
    DOTA_JOIN_RESULT_ACCESS_DENIED = 4
    DOTA_JOIN_RESULT_GENERIC_ERROR = 5
    DOTA_JOIN_RESULT_INCORRECT_VERSION = 6
    DOTA_JOIN_RESULT_IN_TEAM_PARTY = 7
    DOTA_JOIN_RESULT_NO_LOBBY_FOUND = 8
    DOTA_JOIN_RESULT_LOBBY_FULL = 9
    DOTA_JOIN_RESULT_CUSTOM_GAME_INCORRECT_VERSION = 10
    DOTA_JOIN_RESULT_TIMEOUT = 11
    DOTA_JOIN_RESULT_CUSTOM_GAME_COOLDOWN = 12
    DOTA_JOIN_RESULT_BUSY = 13
    DOTA_JOIN_RESULT_NO_PLAYTIME = 14

class DOTALeaverStatus_t(IntEnum):
    DOTA_LEAVER_NONE = 0
    DOTA_LEAVER_DISCONNECTED = 1
    DOTA_LEAVER_DISCONNECTED_TOO_LONG = 2
    DOTA_LEAVER_ABANDONED = 3
    DOTA_LEAVER_AFK = 4
    DOTA_LEAVER_NEVER_CONNECTED = 5
    DOTA_LEAVER_NEVER_CONNECTED_TOO_LONG = 6
    DOTA_LEAVER_FAILED_TO_READY_UP = 7
    DOTA_LEAVER_DECLINED = 8

class DOTALobbyReadyState(IntEnum):
    UNDECLARED = 0
    ACCEPTED = 1
    DECLINED = 2

class DOTALobbyVisibility(IntEnum):
    Public = 0
    Friends = 1
    Unlisted = 2

class DOTALowPriorityBanType(IntEnum):
    DOTA_LOW_PRIORITY_BAN_ABANDON = 0
    DOTA_LOW_PRIORITY_BAN_REPORTS = 1
    DOTA_LOW_PRIORITY_BAN_SECONDARY_ABANDON = 2
    DOTA_LOW_PRIORITY_BAN_PRE_GAME_ROLE = 3

class DOTAMatchVote(IntEnum):
    INVALID = 0
    POSITIVE = 1
    NEGATIVE = 2

class DOTASelectionPriorityChoice(IntEnum):
    Invalid = 0
    FirstPick = 1
    SecondPick = 2
    Radiant = 3
    Dire = 4

class DOTASelectionPriorityRules(IntEnum):
    Manual = 0
    Automatic = 1

class EBadgeType(IntEnum):
    TI7_Midweek = 1
    TI7_Finals = 2
    TI7_AllEvent = 3
    TI8_Midweek = 4
    TI8_Finals = 5
    TI8_AllEvent = 6

class EBroadcastTimelineEvent(IntEnum):
    MatchStarted = 1
    GameStateChanged = 2
    TowerDeath = 3
    BarracksDeath = 4
    AncientDeath = 5
    RoshanDeath = 6
    HeroDeath = 7
    TeamFight = 8
    FirstBlood = 9

EChatSpecialPrivileges = IntEnum('EChatSpecialPrivileges', {
    'None': 0,
    'Moderator': 1,
    'SuperModerator': 2,
    })

class ECustomGameInstallStatus(IntEnum):
    Unknown = 0
    Ready = 1
    Busy = 2
    FailedGeneric = 101
    FailedInternalError = 102
    RequestedTimestampTooOld = 103
    RequestedTimestampTooNew = 104
    CRCMismatch = 105
    FailedSteam = 106
    FailedCanceled = 107

class ECustomGameWhitelistState(IntEnum):
    CUSTOM_GAME_WHITELIST_STATE_UNKNOWN = 0
    CUSTOM_GAME_WHITELIST_STATE_APPROVED = 1
    CUSTOM_GAME_WHITELIST_STATE_REJECTED = 2

class EDACPlatform(IntEnum):
    eDACPlatform_None = 0
    eDACPlatform_PC = 1
    eDACPlatform_Mac = 2
    eDACPlatform_Linux = 3
    eDACPlatform_Android = 4
    eDACPlatform_iOS = 5

class EDevEventRequestResult(IntEnum):
    Success = 0
    NotAllowed = 1
    InvalidEvent = 2
    SqlFailure = 3
    Timeout = 4
    LockFailure = 5
    SDOLoadFailure = 6

class EDOTADraftTriviaAnswerResult(IntEnum):
    Success = 0
    InvalidMatchID = 1
    AlreadyAnswered = 2
    InternalError = 3
    TriviaDisabled = 4
    GCDown = 5

class EDOTAGCMsg(IntEnum):
    EMsgGCDOTABase = 7000
    EMsgGCGeneralResponse = 7001
    EMsgGCGameMatchSignOut = 7004
    EMsgGCGameMatchSignOutResponse = 7005
    EMsgGCJoinChatChannel = 7009
    EMsgGCJoinChatChannelResponse = 7010
    EMsgGCOtherJoinedChannel = 7013
    EMsgGCOtherLeftChannel = 7014
    EMsgGCMatchHistoryList = 7017
    EMsgServerToGCRequestStatus = 7026
    EMsgGCGetRecentMatches = 7027
    EMsgGCRecentMatchesResponse = 7028
    EMsgGCStartFindingMatch = 7033
    EMsgGCConnectedPlayers = 7034
    EMsgGCAbandonCurrentGame = 7035
    EMsgGCStopFindingMatch = 7036
    EMsgGCPracticeLobbyCreate = 7038
    EMsgGCPracticeLobbyLeave = 7040
    EMsgGCPracticeLobbyLaunch = 7041
    EMsgGCPracticeLobbyList = 7042
    EMsgGCPracticeLobbyListResponse = 7043
    EMsgGCPracticeLobbyJoin = 7044
    EMsgGCPracticeLobbySetDetails = 7046
    EMsgGCPracticeLobbySetTeamSlot = 7047
    EMsgGCInitialQuestionnaireResponse = 7049
    EMsgGCPracticeLobbyResponse = 7055
    EMsgGCBroadcastNotification = 7056
    EMsgGCLiveScoreboardUpdate = 7057
    EMsgGCRequestChatChannelList = 7060
    EMsgGCRequestChatChannelListResponse = 7061
    EMsgGCRequestMatches = 7064
    EMsgGCRequestMatchesResponse = 7065
    EMsgGCReadyUp = 7070
    EMsgGCKickedFromMatchmakingQueue = 7071
    EMsgGCLeaverDetected = 7072
    EMsgGCSpectateFriendGame = 7073
    EMsgGCSpectateFriendGameResponse = 7074
    EMsgGCPlayerReports = 7075
    EMsgGCReportsRemainingRequest = 7076
    EMsgGCReportsRemainingResponse = 7077
    EMsgGCSubmitPlayerReport = 7078
    EMsgGCSubmitPlayerReportResponse = 7079
    EMsgGCPracticeLobbyKick = 7081
    EMsgGCReportCountsRequest = 7082
    EMsgGCReportCountsResponse = 7083
    EMsgGCRequestSaveGames = 7084
    EMsgGCRequestSaveGamesServer = 7085
    EMsgGCRequestSaveGamesResponse = 7086
    EMsgGCLeaverDetectedResponse = 7087
    EMsgGCPlayerFailedToConnect = 7088
    EMsgGCGCToRelayConnect = 7089
    EMsgGCGCToRelayConnectresponse = 7090
    EMsgGCWatchGame = 7091
    EMsgGCWatchGameResponse = 7092
    EMsgGCBanStatusRequest = 7093
    EMsgGCBanStatusResponse = 7094
    EMsgGCMatchDetailsRequest = 7095
    EMsgGCMatchDetailsResponse = 7096
    EMsgGCCancelWatchGame = 7097
    EMsgGCPopup = 7102
    EMsgGCDOTAClearNotifySuccessfulReport = 7104
    EMsgGCFriendPracticeLobbyListRequest = 7111
    EMsgGCFriendPracticeLobbyListResponse = 7112
    EMsgGCPracticeLobbyJoinResponse = 7113
    EMsgClientEconNotification_Job = 7114
    EMsgGCCreateTeam = 7115
    EMsgGCCreateTeamResponse = 7116
    EMsgGCTeamData = 7121
    EMsgGCTeamInvite_InviterToGC = 7122
    EMsgGCTeamInvite_GCImmediateResponseToInviter = 7123
    EMsgGCTeamInvite_GCRequestToInvitee = 7124
    EMsgGCTeamInvite_InviteeResponseToGC = 7125
    EMsgGCTeamInvite_GCResponseToInviter = 7126
    EMsgGCTeamInvite_GCResponseToInvitee = 7127
    EMsgGCKickTeamMember = 7128
    EMsgGCKickTeamMemberResponse = 7129
    EMsgGCLeaveTeam = 7130
    EMsgGCLeaveTeamResponse = 7131
    EMsgGCSuggestTeamMatchmaking = 7132
    EMsgGCPlayerHeroesFavoritesAdd = 7133
    EMsgGCPlayerHeroesFavoritesRemove = 7134
    EMsgGCApplyTeamToPracticeLobby = 7142
    EMsgGCTransferTeamAdmin = 7144
    EMsgGCPracticeLobbyJoinBroadcastChannel = 7149
    EMsgGC_TournamentItemEvent = 7150
    EMsgGC_TournamentItemEventResponse = 7151
    EMsgCastMatchVote = 7152
    EMsgCastMatchVoteResponse = 7153
    EMsgRetrieveMatchVote = 7154
    EMsgRetrieveMatchVoteResponse = 7155
    EMsgTeamFanfare = 7156
    EMsgResponseTeamFanfare = 7157
    EMsgGC_GameServerUploadSaveGame = 7158
    EMsgGC_GameServerSaveGameResult = 7159
    EMsgGC_GameServerGetLoadGame = 7160
    EMsgGC_GameServerGetLoadGameResult = 7161
    EMsgGCEditTeamDetails = 7166
    EMsgGCEditTeamDetailsResponse = 7167
    EMsgGCProTeamListRequest = 7168
    EMsgGCProTeamListResponse = 7169
    EMsgGCReadyUpStatus = 7170
    EMsgGCHallOfFame = 7171
    EMsgGCHallOfFameRequest = 7172
    EMsgGCHallOfFameResponse = 7173
    EMsgGCGenerateDiretidePrizeList = 7174
    EMsgGCRewardDiretidePrizes = 7176
    EMsgGCDiretidePrizesRewardedResponse = 7177
    EMsgGCHalloweenHighScoreRequest = 7178
    EMsgGCHalloweenHighScoreResponse = 7179
    EMsgGCGenerateDiretidePrizeListResponse = 7180
    EMsgGCStorePromoPagesRequest = 7182
    EMsgGCStorePromoPagesResponse = 7183
    EMsgGCToGCMatchCompleted = 7186
    EMsgGCBalancedShuffleLobby = 7188
    EMsgGCToGCCheckLeaguePermission = 7189
    EMsgGCToGCCheckLeaguePermissionResponse = 7190
    EMsgGCMatchmakingStatsRequest = 7197
    EMsgGCMatchmakingStatsResponse = 7198
    EMsgGCBotGameCreate = 7199
    EMsgGCSetMatchHistoryAccess = 7200
    EMsgGCSetMatchHistoryAccessResponse = 7201
    EMsgUpgradeLeagueItem = 7203
    EMsgUpgradeLeagueItemResponse = 7204
    EMsgGCTeamMemberProfileRequest = 7205
    EMsgGCWatchDownloadedReplay = 7206
    EMsgGCSetMapLocationState = 7207
    EMsgGCSetMapLocationStateResponse = 7208
    EMsgGCResetMapLocations = 7209
    EMsgGCResetMapLocationsResponse = 7210
    EMsgRefreshPartnerAccountLink = 7216
    EMsgClientsRejoinChatChannels = 7217
    EMsgGCToGCGetUserChatInfo = 7218
    EMsgGCToGCGetUserChatInfoResponse = 7219
    EMsgGCToGCLeaveAllChatChannels = 7220
    EMsgGCToGCUpdateAccountChatBan = 7221
    EMsgGCToGCCanInviteUserToTeam = 7234
    EMsgGCToGCCanInviteUserToTeamResponse = 7235
    EMsgGCToGCGetUserRank = 7236
    EMsgGCToGCGetUserRankResponse = 7237
    EMsgGCToGCUpdateTeamStats = 7240
    EMsgGCToGCValidateTeam = 7241
    EMsgGCToGCValidateTeamResponse = 7242
    EMsgGCPassportDataRequest = 7248
    EMsgGCPassportDataResponse = 7249
    EMsgGCToGCGetLeagueAdmin = 7255
    EMsgGCToGCGetLeagueAdminResponse = 7256
    EMsgGCRequestLeaguePrizePool = 7258
    EMsgGCRequestLeaguePrizePoolResponse = 7259
    EMsgGCLeaveChatChannel = 7272
    EMsgGCChatMessage = 7273
    EMsgGCGetHeroStandings = 7274
    EMsgGCGetHeroStandingsResponse = 7275
    EMsgGCItemEditorReservationsRequest = 7283
    EMsgGCItemEditorReservationsResponse = 7284
    EMsgGCItemEditorReserveItemDef = 7285
    EMsgGCItemEditorReserveItemDefResponse = 7286
    EMsgGCItemEditorReleaseReservation = 7287
    EMsgGCItemEditorReleaseReservationResponse = 7288
    EMsgGCRewardTutorialPrizes = 7289
    EMsgGCLastHitChallengeHighScorePost = 7290
    EMsgGCLastHitChallengeHighScoreRequest = 7291
    EMsgGCLastHitChallengeHighScoreResponse = 7292
    EMsgGCCreateFantasyLeagueRequest = 7293
    EMsgGCCreateFantasyLeagueResponse = 7294
    EMsgGCFantasyLeagueInfoRequest = 7297
    EMsgGCFantasyLeagueInfoResponse = 7298
    EMsgGCFantasyLeagueInfo = 7299
    EMsgGCCreateFantasyTeamRequest = 7300
    EMsgGCCreateFantasyTeamResponse = 7301
    EMsgGCEditFantasyTeamRequest = 7302
    EMsgGCEditFantasyTeamResponse = 7303
    EMsgGCFantasyTeamInfoRequestByFantasyLeagueID = 7304
    EMsgGCFantasyTeamInfoRequestByOwnerAccountID = 7305
    EMsgGCFantasyTeamInfoResponse = 7306
    EMsgGCFantasyTeamInfo = 7307
    EMsgGCFantasyLivePlayerStats = 7308
    EMsgGCFantasyFinalPlayerStats = 7309
    EMsgGCFantasyMatch = 7310
    EMsgGCFantasyTeamScoreRequest = 7312
    EMsgGCFantasyTeamScoreResponse = 7313
    EMsgGCFantasyTeamStandingsRequest = 7314
    EMsgGCFantasyTeamStandingsResponse = 7315
    EMsgGCFantasyPlayerScoreRequest = 7316
    EMsgGCFantasyPlayerScoreResponse = 7317
    EMsgGCFantasyPlayerStandingsRequest = 7318
    EMsgGCFantasyPlayerStandingsResponse = 7319
    EMsgGCFlipLobbyTeams = 7320
    EMsgGCCustomGameCreate = 7321
    EMsgGCToGCProcessPlayerReportForTarget = 7324
    EMsgGCToGCProcessReportSuccess = 7325
    EMsgGCNotifyAccountFlagsChange = 7326
    EMsgGCSetProfilePrivacy = 7327
    EMsgGCSetProfilePrivacyResponse = 7328
    EMsgGCFantasyLeagueCreateInfoRequest = 7331
    EMsgGCFantasyLeagueCreateInfoResponse = 7332
    EMsgGCFantasyLeagueInviteInfoRequest = 7333
    EMsgGCFantasyLeagueInviteInfoResponse = 7334
    EMsgGCClientIgnoredUser = 7335
    EMsgGCFantasyLeagueCreateRequest = 7336
    EMsgGCFantasyLeagueCreateResponse = 7337
    EMsgGCFantasyTeamCreateRequest = 7338
    EMsgGCFantasyTeamCreateResponse = 7339
    EMsgGCFantasyLeagueFriendJoinListRequest = 7340
    EMsgGCFantasyLeagueFriendJoinListResponse = 7341
    EMsgGCClientSuspended = 7342
    EMsgGCPartyMemberSetCoach = 7343
    EMsgGCFantasyLeagueEditInvitesRequest = 7344
    EMsgGCFantasyLeagueEditInvitesResponse = 7345
    EMsgGCPracticeLobbySetCoach = 7346
    EMsgGCFantasyLeagueEditInfoRequest = 7347
    EMsgGCFantasyLeagueEditInfoResponse = 7348
    EMsgGCFantasyLeagueDraftStatusRequest = 7349
    EMsgGCFantasyLeagueDraftStatus = 7350
    EMsgGCFantasyLeagueDraftPlayerRequest = 7351
    EMsgGCFantasyLeagueDraftPlayerResponse = 7352
    EMsgGCFantasyLeagueMatchupsRequest = 7353
    EMsgGCFantasyLeagueMatchupsResponse = 7354
    EMsgGCFantasyTeamRosterSwapRequest = 7355
    EMsgGCFantasyTeamRosterSwapResponse = 7356
    EMsgGCFantasyTeamRosterRequest = 7357
    EMsgGCFantasyTeamRosterResponse = 7358
    EMsgGCChatModeratorBan = 7359
    EMsgGCFantasyTeamRosterAddDropRequest = 7361
    EMsgGCFantasyTeamRosterAddDropResponse = 7362
    EMsgPresentedClientTerminateDlg = 7363
    EMsgGCFantasyPlayerHisoricalStatsRequest = 7364
    EMsgGCFantasyPlayerHisoricalStatsResponse = 7365
    EMsgGCPCBangTimedRewardMessage = 7366
    EMsgGCLobbyUpdateBroadcastChannelInfo = 7367
    EMsgGCFantasyTeamTradesRequest = 7368
    EMsgGCFantasyTeamTradesResponse = 7369
    EMsgGCFantasyTeamTradeCancelRequest = 7370
    EMsgGCFantasyTeamTradeCancelResponse = 7371
    EMsgGCToGCGrantTournamentItem = 7372
    EMsgGCProcessFantasyScheduledEvent = 7373
    EMsgGCToGCUpgradeTwitchViewerItems = 7375
    EMsgGCToGCGetLiveMatchAffiliates = 7376
    EMsgGCToGCGetLiveMatchAffiliatesResponse = 7377
    EMsgGCToGCUpdatePlayerPennantCounts = 7378
    EMsgGCToGCGetPlayerPennantCounts = 7379
    EMsgGCToGCGetPlayerPennantCountsResponse = 7380
    EMsgGCGameMatchSignOutPermissionRequest = 7381
    EMsgGCGameMatchSignOutPermissionResponse = 7382
    EMsgDOTAChatChannelMemberUpdate = 7383
    EMsgDOTAAwardEventPoints = 7384
    EMsgDOTAGetEventPoints = 7387
    EMsgDOTAGetEventPointsResponse = 7388
    EMsgDOTASendFriendRecruits = 7393
    EMsgDOTAFriendRecruitsRequest = 7394
    EMsgDOTAFriendRecruitsResponse = 7395
    EMsgDOTAFriendRecruitInviteAcceptDecline = 7396
    EMsgGCPartyLeaderWatchGamePrompt = 7397
    EMsgDOTAFrostivusTimeElapsed = 7398
    EMsgDOTALiveLeagueGameUpdate = 7402
    EMsgDOTAChatGetUserList = 7403
    EMsgDOTAChatGetUserListResponse = 7404
    EMsgGCCompendiumSetSelection = 7405
    EMsgGCCompendiumDataRequest = 7406
    EMsgGCCompendiumDataResponse = 7407
    EMsgDOTAGetPlayerMatchHistory = 7408
    EMsgDOTAGetPlayerMatchHistoryResponse = 7409
    EMsgGCToGCMatchmakingAddParty = 7410
    EMsgGCToGCMatchmakingRemoveParty = 7411
    EMsgGCToGCMatchmakingRemoveAllParties = 7412
    EMsgGCToGCMatchmakingMatchFound = 7413
    EMsgGCToGCUpdateMatchManagementStats = 7414
    EMsgGCToGCUpdateMatchmakingStats = 7415
    EMsgGCToServerPingRequest = 7416
    EMsgGCToServerPingResponse = 7417
    EMsgGCToServerConsoleCommand = 7418
    EMsgGCMakeOffering = 7423
    EMsgGCRequestOfferings = 7424
    EMsgGCRequestOfferingsResponse = 7425
    EMsgGCToGCProcessMatchLeaver = 7426
    EMsgGCNotificationsRequest = 7427
    EMsgGCNotificationsResponse = 7428
    EMsgGCToGCModifyNotification = 7429
    EMsgGCToGCSetNewNotifications = 7430
    EMsgGCLeagueAdminList = 7434
    EMsgGCNotificationsMarkReadRequest = 7435
    EMsgGCFantasyMessageAdd = 7436
    EMsgGCFantasyMessagesRequest = 7437
    EMsgGCFantasyMessagesResponse = 7438
    EMsgGCFantasyScheduledMatchesRequest = 7439
    EMsgGCFantasyScheduledMatchesResponse = 7440
    EMsgGCEventGameCreate = 7443
    EMsgGCPerfectWorldUserLookupRequest = 7444
    EMsgGCPerfectWorldUserLookupResponse = 7445
    EMsgGCFantasyRemoveOwner = 7448
    EMsgGCFantasyRemoveOwnerResponse = 7449
    EMsgServerToGCRequestBatchPlayerResources = 7450
    EMsgServerToGCRequestBatchPlayerResourcesResponse = 7451
    EMsgGCToGCSendUpdateLeagues = 7452
    EMsgGCCompendiumSetSelectionResponse = 7453
    EMsgGCPlayerInfoRequest = 7454
    EMsgGCPlayerInfo = 7455
    EMsgGCPlayerInfoSubmit = 7456
    EMsgGCPlayerInfoSubmitResponse = 7457
    EMsgGCToGCGetAccountLevel = 7458
    EMsgGCToGCGetAccountLevelResponse = 7459
    EMsgGCToGCGetAccountPartner = 7460
    EMsgGCToGCGetAccountPartnerResponse = 7461
    EMsgDOTAGetWeekendTourneySchedule = 7464
    EMsgDOTAWeekendTourneySchedule = 7465
    EMsgGCJoinableCustomGameModesRequest = 7466
    EMsgGCJoinableCustomGameModesResponse = 7467
    EMsgGCJoinableCustomLobbiesRequest = 7468
    EMsgGCJoinableCustomLobbiesResponse = 7469
    EMsgGCQuickJoinCustomLobby = 7470
    EMsgGCQuickJoinCustomLobbyResponse = 7471
    EMsgGCToGCGrantEventPointAction = 7472
    EMsgServerGrantSurveyPermission = 7475
    EMsgServerGrantSurveyPermissionResponse = 7476
    EMsgClientProvideSurveyResult = 7477
    EMsgGCToGCSetCompendiumSelection = 7478
    EMsgGCToGCUpdateTI4HeroQuest = 7480
    EMsgGCCompendiumDataChanged = 7481
    EMsgDOTAFantasyLeagueFindRequest = 7482
    EMsgDOTAFantasyLeagueFindResponse = 7483
    EMsgGCHasItemQuery = 7484
    EMsgGCHasItemResponse = 7485
    EMsgGCConsumeFantasyTicket = 7486
    EMsgGCConsumeFantasyTicketFailure = 7487
    EMsgGCToGCGrantEventPointActionMsg = 7488
    EMsgClientToGCTrackDialogResult = 7489
    EMsgGCFantasyLeaveLeagueRequest = 7490
    EMsgGCFantasyLeaveLeagueResponse = 7491
    EMsgGCToGCGetCompendiumSelections = 7492
    EMsgGCToGCGetCompendiumSelectionsResponse = 7493
    EMsgServerToGCMatchConnectionStats = 7494
    EMsgGCToClientTournamentItemDrop = 7495
    EMsgSQLDelayedGrantLeagueDrop = 7496
    EMsgServerGCUpdateSpectatorCount = 7497
    EMsgGCFantasyPlayerScoreDetailsRequest = 7499
    EMsgGCFantasyPlayerScoreDetailsResponse = 7500
    EMsgGCToGCEmoticonUnlock = 7501
    EMsgSignOutDraftInfo = 7502
    EMsgClientToGCEmoticonDataRequest = 7503
    EMsgGCToClientEmoticonData = 7504
    EMsgGCPracticeLobbyToggleBroadcastChannelCameramanStatus = 7505
    EMsgGCToGCCreateWeekendTourneyRequest = 7506
    EMsgGCToGCCreateWeekendTourneyResponse = 7507
    EMsgClientToGCSetAdditionalEquips = 7513
    EMsgClientToGCGetAdditionalEquips = 7514
    EMsgClientToGCGetAdditionalEquipsResponse = 7515
    EMsgServerToGCGetAdditionalEquips = 7516
    EMsgServerToGCGetAdditionalEquipsResponse = 7517
    EMsgDOTARedeemItem = 7518
    EMsgDOTARedeemItemResponse = 7519
    EMsgSQLGCToGCGrantAllHeroProgress = 7520
    EMsgClientToGCGetAllHeroProgress = 7521
    EMsgClientToGCGetAllHeroProgressResponse = 7522
    EMsgGCToGCGetServerForClient = 7523
    EMsgGCToGCGetServerForClientResponse = 7524
    EMsgSQLProcessTournamentGameOutcome = 7525
    EMsgSQLGrantTrophyToAccount = 7526
    EMsgClientToGCGetTrophyList = 7527
    EMsgClientToGCGetTrophyListResponse = 7528
    EMsgGCToClientTrophyAwarded = 7529
    EMsgGCGameBotMatchSignOut = 7530
    EMsgGCGameBotMatchSignOutPermissionRequest = 7531
    EMsgSignOutBotInfo = 7532
    EMsgGCToGCUpdateProfileCards = 7533
    EMsgClientToGCGetProfileCard = 7534
    EMsgClientToGCGetProfileCardResponse = 7535
    EMsgServerToGCGetProfileCard = 7536
    EMsgServerToGCGetProfileCardResponse = 7537
    EMsgClientToGCSetProfileCardSlots = 7538
    EMsgGCToClientProfileCardUpdated = 7539
    EMsgServerToGCVictoryPredictions = 7540
    EMsgClientToGCMarkNotificationListRead = 7542
    EMsgServerToGCSuspiciousActivity = 7544
    EMsgSignOutCommunicationSummary = 7545
    EMsgServerToGCRequestStatus_Response = 7546
    EMsgClientToGCCreateHeroStatue = 7547
    EMsgGCToClientHeroStatueCreateResult = 7548
    EMsgGCGCToLANServerRelayConnect = 7549
    EMsgServerToGCGetIngameEventData = 7551
    EMsgGCToGCUpdateIngameEventDataBroadcast = 7552
    EMsgGCToServerIngameEventData_OraclePA = 7553
    EMsgServerToGCReportKillSummaries = 7554
    EMsgGCToGCReportKillSummaries = 7555
    EMsgGCToGCUpdateAssassinMinigame = 7556
    EMsgGCToGCFantasySetMatchLeague = 7557
    EMsgGCToGCUpdatePlayerPredictions = 7561
    EMsgGCToServerPredictionResult = 7562
    EMsgServerToGCSignoutAwardAdditionalDrops = 7563
    EMsgGCToGCSignoutAwardAdditionalDrops = 7564
    EMsgGCToClientEventStatusChanged = 7565
    EMsgGCHasItemDefsQuery = 7566
    EMsgGCHasItemDefsResponse = 7567
    EMsgGCToGCReplayMonitorValidateReplay = 7569
    EMsgLobbyEventPoints = 7572
    EMsgGCToGCGetCustomGameTickets = 7573
    EMsgGCToGCGetCustomGameTicketsResponse = 7574
    EMsgGCToGCCustomGamePlayed = 7576
    EMsgGCToGCGrantEventPointsToUser = 7577
    EMsgGCToGCSetEventMMPanicFlushTime = 7578
    EMsgGameserverCrashReport = 7579
    EMsgGameserverCrashReportResponse = 7580
    EMsgGCToClientSteamDatagramTicket = 7581
    EMsgGCToGCGrantEventOwnership = 7582
    EMsgGCToGCSendAccountsEventPoints = 7583
    EMsgClientToGCRerollPlayerChallenge = 7584
    EMsgServerToGCRerollPlayerChallenge = 7585
    EMsgGCRerollPlayerChallengeResponse = 7586
    EMsgSignOutUpdatePlayerChallenge = 7587
    EMsgClientToGCSetPartyLeader = 7588
    EMsgClientToGCCancelPartyInvites = 7589
    EMsgGCToGCMasterReloadAccount = 7590
    EMsgSQLGrantLeagueMatchToTicketHolders = 7592
    EMsgClientToGCSetAdditionalEquipsResponse = 7593
    EMsgGCToGCEmoticonUnlockNoRollback = 7594
    EMsgGCToGCGetCompendiumFanfare = 7595
    EMsgGCToGCChatNewUserSession = 7598
    EMsgClientToGCApplyGemCombiner = 7603
    EMsgClientToGCDOTACreateStaticRecipe = 7604
    EMsgClientToGCDOTACreateStaticRecipeResponse = 7605
    EMsgClientToGCGetAllHeroOrder = 7606
    EMsgClientToGCGetAllHeroOrderResponse = 7607
    EMsgSQLGCToGCGrantBadgePoints = 7608
    EMsgGCToGCGetAccountMatchStatus = 7609
    EMsgGCToGCGetAccountMatchStatusResponse = 7610
    EMsgGCToGCCheckOwnsEntireEmoticonRange = 7611
    EMsgGCToGCCheckOwnsEntireEmoticonRangeResponse = 7612
    EMsgClientToGCRecycleHeroRelic = 7619
    EMsgClientToGCRecycleHeroRelicResponse = 7620
    EMsgGCToGCRevokeEventOwnership = 7621
    EMsgGCToClientRequestLaneSelection = 7623
    EMsgGCToClientRequestLaneSelectionResponse = 7624
    EMsgServerToGCCavernCrawlIsHeroActive = 7625
    EMsgServerToGCCavernCrawlIsHeroActiveResponse = 7626
    EMsgClientToGCPlayerCardSpecificPurchaseRequest = 7627
    EMsgClientToGCPlayerCardSpecificPurchaseResponse = 7628
    EMsgGCtoServerTensorflowInstance = 7629
    EMsgSQLSetIsLeagueAdmin = 7630
    EMsgGCToGCGetLiveLeagueMatches = 7631
    EMsgGCToGCGetLiveLeagueMatchesResponse = 7632
    EMsgDOTALeagueInfoListAdminsRequest = 7633
    EMsgDOTALeagueInfoListAdminsReponse = 7634
    EMsgGCToGCLeagueMatchStarted = 7645
    EMsgGCToGCLeagueMatchCompleted = 7646
    EMsgGCToGCLeagueMatchStartedResponse = 7647
    EMsgDOTALeagueNodeRequest = 7648
    EMsgDOTALeagueNodeResponse = 7649
    EMsgDOTALeagueAvailableLobbyNodesRequest = 7650
    EMsgDOTALeagueAvailableLobbyNodes = 7651
    EMsgGCToGCLeagueRequest = 7652
    EMsgGCToGCLeagueResponse = 7653
    EMsgGCToGCLeagueNodeGroupRequest = 7654
    EMsgGCToGCLeagueNodeGroupResponse = 7655
    EMsgGCToGCLeagueNodeRequest = 7656
    EMsgGCToGCLeagueNodeResponse = 7657
    EMsgGCToGCRealtimeStatsTerseRequest = 7658
    EMsgGCToGCRealtimeStatsTerseResponse = 7659
    EMsgGCToGCGetTopMatchesRequest = 7660
    EMsgGCToGCGetTopMatchesResponse = 7661
    EMsgClientToGCGetFilteredPlayers = 7662
    EMsgGCToClientGetFilteredPlayersResponse = 7663
    EMsgClientToGCRemoveFilteredPlayer = 7664
    EMsgGCToClientRemoveFilteredPlayerResponse = 7665
    EMsgGCToClientPlayerBeaconState = 7666
    EMsgGCToClientPartyBeaconUpdate = 7667
    EMsgGCToClientPartySearchInvite = 7668
    EMsgClientToGCUpdatePartyBeacon = 7669
    EMsgClientToGCRequestActiveBeaconParties = 7670
    EMsgGCToClientRequestActiveBeaconPartiesResponse = 7671
    EMsgClientToGCManageFavorites = 7672
    EMsgGCToClientManageFavoritesResponse = 7673
    EMsgClientToGCJoinPartyFromBeacon = 7674
    EMsgGCToClientJoinPartyFromBeaconResponse = 7675
    EMsgClientToGCGetFavoritePlayers = 7676
    EMsgGCToClientGetFavoritePlayersResponse = 7677
    EMsgClientToGCVerifyFavoritePlayers = 7678
    EMsgGCToClientVerifyFavoritePlayersResponse = 7679
    EMsgGCToClientPartySearchInvites = 7680
    EMsgGCToClientRequestMMInfo = 7681
    EMsgClientToGCMMInfo = 7682
    EMsgSignOutTextMuteInfo = 7683
    EMsgGCDev_GrantWarKill = 8001
    EMsgServerToGCLockCharmTrading = 8004
    EMsgClientToGCPlayerStatsRequest = 8006
    EMsgGCToClientPlayerStatsResponse = 8007
    EMsgGCClearPracticeLobbyTeam = 8008
    EMsgClientToGCFindTopSourceTVGames = 8009
    EMsgGCToClientFindTopSourceTVGamesResponse = 8010
    EMsgGCLobbyList = 8011
    EMsgGCLobbyListResponse = 8012
    EMsgGCPlayerStatsMatchSignOut = 8013
    EMsgClientToGCCustomGamePlayerCountRequest = 8014
    EMsgGCToClientCustomGamePlayerCountResponse = 8015
    EMsgClientToGCSocialFeedPostCommentRequest = 8016
    EMsgGCToClientSocialFeedPostCommentResponse = 8017
    EMsgClientToGCCustomGamesFriendsPlayedRequest = 8018
    EMsgGCToClientCustomGamesFriendsPlayedResponse = 8019
    EMsgClientToGCFriendsPlayedCustomGameRequest = 8020
    EMsgGCToClientFriendsPlayedCustomGameResponse = 8021
    EMsgGCTopCustomGamesList = 8024
    EMsgClientToGCSetPartyOpen = 8029
    EMsgClientToGCMergePartyInvite = 8030
    EMsgGCToClientMergeGroupInviteReply = 8031
    EMsgClientToGCMergePartyResponse = 8032
    EMsgGCToClientMergePartyResponseReply = 8033
    EMsgClientToGCGetProfileCardStats = 8034
    EMsgClientToGCGetProfileCardStatsResponse = 8035
    EMsgClientToGCTopLeagueMatchesRequest = 8036
    EMsgClientToGCTopFriendMatchesRequest = 8037
    EMsgGCToClientProfileCardStatsUpdated = 8040
    EMsgServerToGCRealtimeStats = 8041
    EMsgGCToServerRealtimeStatsStartStop = 8042
    EMsgGCToGCGetServersForClients = 8045
    EMsgGCToGCGetServersForClientsResponse = 8046
    EMsgGCPracticeLobbyKickFromTeam = 8047
    EMsgDOTAChatGetMemberCount = 8048
    EMsgDOTAChatGetMemberCountResponse = 8049
    EMsgClientToGCSocialFeedPostMessageRequest = 8050
    EMsgGCToClientSocialFeedPostMessageResponse = 8051
    EMsgCustomGameListenServerStartedLoading = 8052
    EMsgCustomGameClientFinishedLoading = 8053
    EMsgGCPracticeLobbyCloseBroadcastChannel = 8054
    EMsgGCStartFindingMatchResponse = 8055
    EMsgSQLGCToGCGrantAccountFlag = 8057
    EMsgGCToGCGetAccountFlags = 8058
    EMsgGCToGCGetAccountFlagsResponse = 8059
    EMsgSignOutWagerStats = 8060
    EMsgGCToClientTopLeagueMatchesResponse = 8061
    EMsgGCToClientTopFriendMatchesResponse = 8062
    EMsgClientToGCMatchesMinimalRequest = 8063
    EMsgClientToGCMatchesMinimalResponse = 8064
    EMsgGCToGCGetProfileBadgePoints = 8065
    EMsgGCToGCGetProfileBadgePointsResponse = 8066
    EMsgGCToClientChatRegionsEnabled = 8067
    EMsgClientToGCPingData = 8068
    EMsgServerToGCMatchDetailsRequest = 8069
    EMsgGCToServerMatchDetailsResponse = 8070
    EMsgGCToGCEnsureAccountInParty = 8071
    EMsgGCToGCEnsureAccountInPartyResponse = 8072
    EMsgClientToGCGetProfileTickets = 8073
    EMsgClientToGCGetProfileTicketsResponse = 8074
    EMsgGCToClientMatchGroupsVersion = 8075
    EMsgClientToGCH264Unsupported = 8076
    EMsgClientToGCRequestH264Support = 8077
    EMsgClientToGCGetQuestProgress = 8078
    EMsgClientToGCGetQuestProgressResponse = 8079
    EMsgSignOutXPCoins = 8080
    EMsgGCToClientMatchSignedOut = 8081
    EMsgGCGetHeroStatsHistory = 8082
    EMsgGCGetHeroStatsHistoryResponse = 8083
    EMsgClientToGCPrivateChatInvite = 8084
    EMsgClientToGCPrivateChatKick = 8088
    EMsgClientToGCPrivateChatPromote = 8089
    EMsgClientToGCPrivateChatDemote = 8090
    EMsgGCToClientPrivateChatResponse = 8091
    EMsgClientToGCPrivateChatInfoRequest = 8092
    EMsgGCToClientPrivateChatInfoResponse = 8093
    EMsgClientToGCLatestConductScorecardRequest = 8095
    EMsgClientToGCLatestConductScorecard = 8096
    EMsgServerToGCPostMatchTip = 8097
    EMsgServerToGCPostMatchTipResponse = 8098
    EMsgClientToGCWageringRequest = 8099
    EMsgGCToClientWageringResponse = 8100
    EMsgClientToGCEventGoalsRequest = 8103
    EMsgClientToGCEventGoalsResponse = 8104
    EMsgClientToGCLeaguePredictions = 8106
    EMsgGCToClientLeaguePredictionsResponse = 8107
    EMsgGCToGCLeaguePredictionsUpdate = 8108
    EMsgClientToGCSuspiciousActivity = 8109
    EMsgGCToGCAddUserToPostGameChat = 8110
    EMsgClientToGCHasPlayerVotedForMVP = 8111
    EMsgClientToGCHasPlayerVotedForMVPResponse = 8112
    EMsgClientToGCVoteForMVP = 8113
    EMsgClientToGCVoteForMVPResponse = 8114
    EMsgGCToGCGetEventOwnership = 8115
    EMsgGCToGCGetEventOwnershipResponse = 8116
    EMsgGCToClientAutomatedTournamentStateChange = 8117
    EMsgClientToGCWeekendTourneyOpts = 8118
    EMsgClientToGCWeekendTourneyOptsResponse = 8119
    EMsgClientToGCWeekendTourneyLeave = 8120
    EMsgClientToGCWeekendTourneyLeaveResponse = 8121
    EMsgClientToGCTeammateStatsRequest = 8124
    EMsgClientToGCTeammateStatsResponse = 8125
    EMsgClientToGCGetGiftPermissions = 8126
    EMsgClientToGCGetGiftPermissionsResponse = 8127
    EMsgClientToGCVoteForArcana = 8128
    EMsgClientToGCVoteForArcanaResponse = 8129
    EMsgClientToGCRequestArcanaVotesRemaining = 8130
    EMsgClientToGCRequestArcanaVotesRemainingResponse = 8131
    EMsgGCTransferTeamAdminResponse = 8132
    EMsgGCToClientTeamInfo = 8135
    EMsgGCToClientTeamsInfo = 8136
    EMsgClientToGCMyTeamInfoRequest = 8137
    EMsgClientToGCPublishUserStat = 8140
    EMsgGCToGCSignoutSpendWager = 8141
    EMsgGCSubmitLobbyMVPVote = 8144
    EMsgGCSubmitLobbyMVPVoteResponse = 8145
    EMsgSignOutCommunityGoalProgress = 8150
    EMsgGCToClientLobbyMVPNotifyRecipient = 8151
    EMsgGCToClientLobbyMVPAwarded = 8152
    EMsgGCToClientQuestProgressUpdated = 8153
    EMsgGCToClientWageringUpdate = 8154
    EMsgGCToClientArcanaVotesUpdate = 8155
    EMsgClientToGCAddTI6TreeProgress = 8156
    EMsgClientToGCSetSpectatorLobbyDetails = 8157
    EMsgClientToGCSetSpectatorLobbyDetailsResponse = 8158
    EMsgClientToGCCreateSpectatorLobby = 8159
    EMsgClientToGCCreateSpectatorLobbyResponse = 8160
    EMsgClientToGCSpectatorLobbyList = 8161
    EMsgClientToGCSpectatorLobbyListResponse = 8162
    EMsgSpectatorLobbyGameDetails = 8163
    EMsgServerToGCCompendiumInGamePredictionResults = 8166
    EMsgServerToGCCloseCompendiumInGamePredictionVoting = 8167
    EMsgClientToGCOpenPlayerCardPack = 8168
    EMsgClientToGCOpenPlayerCardPackResponse = 8169
    EMsgClientToGCSelectCompendiumInGamePrediction = 8170
    EMsgClientToGCSelectCompendiumInGamePredictionResponse = 8171
    EMsgClientToGCWeekendTourneyGetPlayerStats = 8172
    EMsgClientToGCWeekendTourneyGetPlayerStatsResponse = 8173
    EMsgClientToGCRecyclePlayerCard = 8174
    EMsgClientToGCRecyclePlayerCardResponse = 8175
    EMsgClientToGCCreatePlayerCardPack = 8176
    EMsgClientToGCCreatePlayerCardPackResponse = 8177
    EMsgClientToGCGetPlayerCardRosterRequest = 8178
    EMsgClientToGCGetPlayerCardRosterResponse = 8179
    EMsgClientToGCSetPlayerCardRosterRequest = 8180
    EMsgClientToGCSetPlayerCardRosterResponse = 8181
    EMsgServerToGCCloseCompendiumInGamePredictionVotingResponse = 8183
    EMsgServerToGCCompendiumInGamePredictionResultsResponse = 8185
    EMsgLobbyBattleCupVictory = 8186
    EMsgGCGetPlayerCardItemInfo = 8187
    EMsgGCGetPlayerCardItemInfoResponse = 8188
    EMsgClientToGCRequestSteamDatagramTicket = 8189
    EMsgClientToGCRequestSteamDatagramTicketResponse = 8190
    EMsgGCToClientBattlePassRollupRequest = 8191
    EMsgGCToClientBattlePassRollupResponse = 8192
    EMsgClientToGCTransferSeasonalMMRRequest = 8193
    EMsgClientToGCTransferSeasonalMMRResponse = 8194
    EMsgGCToGCPublicChatCommunicationBan = 8195
    EMsgGCToGCUpdateAccountInfo = 8196
    EMsgGCChatReportPublicSpam = 8197
    EMsgClientToGCSetPartyBuilderOptions = 8198
    EMsgClientToGCSetPartyBuilderOptionsResponse = 8199
    EMsgGCToClientPlaytestStatus = 8200
    EMsgClientToGCJoinPlaytest = 8201
    EMsgClientToGCJoinPlaytestResponse = 8202
    EMsgLobbyPlaytestDetails = 8203
    EMsgDOTASetFavoriteTeam = 8204
    EMsgGCToClientBattlePassRollupListRequest = 8205
    EMsgGCToClientBattlePassRollupListResponse = 8206
    EMsgGCIsProQuery = 8207
    EMsgGCIsProResponse = 8208
    EMsgDOTAClaimEventAction = 8209
    EMsgDOTAClaimEventActionResponse = 8210
    EMsgDOTAGetPeriodicResource = 8211
    EMsgDOTAGetPeriodicResourceResponse = 8212
    EMsgDOTAPeriodicResourceUpdated = 8213
    EMsgServerToGCSpendWager = 8214
    EMsgGCToGCSignoutSpendWagerToken = 8215
    EMsgSubmitTriviaQuestionAnswer = 8216
    EMsgSubmitTriviaQuestionAnswerResponse = 8217
    EMsgClientToGCGiveTip = 8218
    EMsgClientToGCGiveTipResponse = 8219
    EMsgStartTriviaSession = 8220
    EMsgStartTriviaSessionResponse = 8221
    EMsgAnchorPhoneNumberRequest = 8222
    EMsgAnchorPhoneNumberResponse = 8223
    EMsgUnanchorPhoneNumberRequest = 8224
    EMsgUnanchorPhoneNumberResponse = 8225
    EMsgGCToClientTipNotification = 8226
    EMsgClientToGCRequestSlarkGameResult = 8227
    EMsgClientToGCRequestSlarkGameResultResponse = 8228
    EMsgGCToGCSignoutSpendRankWager = 8229
    EMsgGCToGCGetFavoriteTeam = 8230
    EMsgGCToGCGetFavoriteTeamResponse = 8231
    EMsgSignOutEventGameData = 8232
    EMsgGCToClientAllStarVotesRequest = 8233
    EMsgGCToClientAllStarVotesReply = 8234
    EMsgGCToClientAllStarVotesSubmit = 8236
    EMsgGCToClientAllStarVotesSubmitReply = 8237
    EMsgClientToGCQuickStatsRequest = 8238
    EMsgClientToGCQuickStatsResponse = 8239
    EMsgGCToGCSubtractEventPointsFromUser = 8240
    EMsgSelectionPriorityChoiceRequest = 8241
    EMsgSelectionPriorityChoiceResponse = 8242
    EMsgGCToGCCompendiumInGamePredictionResults = 8243
    EMsgGameAutographReward = 8244
    EMsgGameAutographRewardResponse = 8245
    EMsgDestroyLobbyRequest = 8246
    EMsgDestroyLobbyResponse = 8247
    EMsgPurchaseItemWithEventPoints = 8248
    EMsgPurchaseItemWithEventPointsResponse = 8249
    EMsgServerToGCMatchPlayerItemPurchaseHistory = 8250
    EMsgGCToGCGrantPlusHeroMatchResults = 8251
    EMsgGCGetHeroTimedStats = 8252
    EMsgGCGetHeroTimedStatsResponse = 8253
    EMsgLobbyPlayerPlusSubscriptionData = 8254
    EMsgServerToGCMatchStateHistory = 8255
    EMsgPurchaseHeroRelic = 8256
    EMsgPurchaseHeroRelicResponse = 8257
    EMsgPurchaseHeroRandomRelic = 8258
    EMsgPurchaseHeroRandomRelicResponse = 8259
    EMsgClientToGCClaimEventActionUsingItem = 8260
    EMsgClientToGCClaimEventActionUsingItemResponse = 8261
    EMsgPartyReadyCheckRequest = 8262
    EMsgPartyReadyCheckResponse = 8263
    EMsgPartyReadyCheckAcknowledge = 8264
    EMsgGetRecentPlayTimeFriendsRequest = 8265
    EMsgGetRecentPlayTimeFriendsResponse = 8266
    EMsgGCToClientCommendNotification = 8267
    EMsgProfileRequest = 8268
    EMsgProfileResponse = 8269
    EMsgProfileUpdate = 8270
    EMsgProfileUpdateResponse = 8271
    EMsgSuccessfulHero = 8273
    EMsgHeroGlobalDataRequest = 8274
    EMsgHeroGlobalDataResponse = 8275
    EMsgClientToGCRequestPlusWeeklyChallengeResult = 8276
    EMsgClientToGCRequestPlusWeeklyChallengeResultResponse = 8277
    EMsgGCToGCGrantPlusPrepaidTime = 8278
    EMsgPrivateMetadataKeyRequest = 8279
    EMsgPrivateMetadataKeyResponse = 8280
    EMsgGCToGCReconcilePlusStatus = 8281
    EMsgGCToGCCheckPlusStatus = 8282
    EMsgGCToGCCheckPlusStatusResponse = 8283
    EMsgGCToGCReconcilePlusAutoGrantItems = 8284
    EMsgGCToGCReconcilePlusStatusUnreliable = 8285
    EMsgActivatePlusFreeTrialRequest = 8286
    EMsgActivatePlusFreeTrialResponse = 8287
    EMsgGCToClientCavernCrawlMapPathCompleted = 8288
    EMsgClientToGCCavernCrawlClaimRoom = 8289
    EMsgClientToGCCavernCrawlClaimRoomResponse = 8290
    EMsgClientToGCCavernCrawlUseItemOnRoom = 8291
    EMsgClientToGCCavernCrawlUseItemOnRoomResponse = 8292
    EMsgClientToGCCavernCrawlUseItemOnPath = 8293
    EMsgClientToGCCavernCrawlUseItemOnPathResponse = 8294
    EMsgClientToGCCavernCrawlRequestMapState = 8295
    EMsgClientToGCCavernCrawlRequestMapStateResponse = 8296
    EMsgSignOutTips = 8297
    EMsgClientToGCRequestEventPointLogV2 = 8298
    EMsgClientToGCRequestEventPointLogResponseV2 = 8299
    EMsgClientToGCRequestEventTipsSummary = 8300
    EMsgClientToGCRequestEventTipsSummaryResponse = 8301
    EMsgHeroGlobalDataAllHeroes = 8302
    EMsgClientToGCRequestSocialFeed = 8303
    EMsgClientToGCRequestSocialFeedResponse = 8304
    EMsgClientToGCRequestSocialFeedComments = 8305
    EMsgClientToGCRequestSocialFeedCommentsResponse = 8306
    EMsgClientToGCCavernCrawlGetClaimedRoomCount = 8308
    EMsgClientToGCCavernCrawlGetClaimedRoomCountResponse = 8309
    EMsgGCToGCReconcilePlusAutoGrantItemsUnreliable = 8310
    EMsgServerToGCAddBroadcastTimelineEvent = 8311
    EMsgGCToServerUpdateSteamBroadcasting = 8312
    EMsgClientToGCRecordContestVote = 8313
    EMsgGCToClientRecordContestVoteResponse = 8314
    EMsgGCToGCGrantAutograph = 8315
    EMsgGCToGCGrantAutographResponse = 8316
    EMsgSignOutConsumableUsage = 8317
    EMsgLobbyEventGameDetails = 8318
    EMsgDevGrantEventPoints = 8319
    EMsgDevGrantEventPointsResponse = 8320
    EMsgDevGrantEventAction = 8321
    EMsgDevGrantEventActionResponse = 8322
    EMsgDevResetEventState = 8323
    EMsgDevResetEventStateResponse = 8324
    EMsgGCToGCReconcileEventOwnership = 8325
    EMsgConsumeEventSupportGrantItem = 8326
    EMsgConsumeEventSupportGrantItemResponse = 8327
    EMsgGCToClientClaimEventActionUsingItemCompleted = 8328
    EMsgGCToClientCavernCrawlMapUpdated = 8329
    EMsgServerToGCRequestPlayerRecentAccomplishments = 8330
    EMsgServerToGCRequestPlayerRecentAccomplishmentsResponse = 8331
    EMsgClientToGCRequestPlayerRecentAccomplishments = 8332
    EMsgClientToGCRequestPlayerRecentAccomplishmentsResponse = 8333
    EMsgClientToGCRequestPlayerHeroRecentAccomplishments = 8334
    EMsgClientToGCRequestPlayerHeroRecentAccomplishmentsResponse = 8335
    EMsgSignOutEventActionGrants = 8336
    EMsgClientToGCRequestPlayerCoachMatches = 8337
    EMsgClientToGCRequestPlayerCoachMatchesResponse = 8338
    EMsgClientToGCGetTicketCodesRequest = 8339
    EMsgClientToGCGetTicketCodesResponse = 8340
    EMsgClientToGCSubmitCoachTeammateRating = 8341
    EMsgClientToGCSubmitCoachTeammateRatingResponse = 8342
    EMsgGCToClientCoachTeammateRatingsChanged = 8343
    EMsgClientToGCVoteForLeagueGameMVP = 8344
    EMsgClientToGCRequestPlayerCoachMatch = 8345
    EMsgClientToGCRequestPlayerCoachMatchResponse = 8346
    EMsgClientToGCRequestContestVotes = 8347
    EMsgClientToGCRequestContestVotesResponse = 8348
    EMsgClientToGCMVPVoteTimeout = 8349
    EMsgClientToGCMVPVoteTimeoutResponse = 8350
    EMsgClientToGCGetUnderlordsCDKeyRequest = 8351
    EMsgClientToGCGetUnderlordsCDKeyResponse = 8352
    EMsgDetailedGameStats = 8353
    EMsgClientToGCSetFavoriteAllStarPlayer = 8354
    EMsgClientToGCSetFavoriteAllStarPlayerResponse = 8355
    EMsgAllStarStats = 8356
    EMsgClientToGCGetFavoriteAllStarPlayerRequest = 8357
    EMsgClientToGCGetFavoriteAllStarPlayerResponse = 8358
    EMsgClientToGCVerifyIntegrity = 8359
    EMsgMatchMatchmakingStats = 8360
    EMsgClientToGCSubmitPlayerMatchSurvey = 8361
    EMsgClientToGCSubmitPlayerMatchSurveyResponse = 8362
    EMsgSQLGCToGCGrantAllHeroProgressAccount = 8363
    EMsgSQLGCToGCGrantAllHeroProgressVictory = 8364
    EMsgDevDeleteEventActions = 8365
    EMsgDevDeleteEventActionsResponse = 8366
    eMsgGCToGCGetAllHeroCurrent = 8635
    eMsgGCToGCGetAllHeroCurrentResponse = 8636
    EMsgGCSubmitPlayerAvoidRequest = 8637
    EMsgGCSubmitPlayerAvoidRequestResponse = 8638
    EMsgGCToClientNotificationsUpdated = 8639
    EMsgGCtoGCAssociatedExploiterAccountInfo = 8640
    EMsgGCtoGCAssociatedExploiterAccountInfoResponse = 8641
    EMsgGCtoGCRequestRecalibrationCheck = 8642
    EMsgGCToClientVACReminder = 8643
    EMsgClientToGCUnderDraftBuy = 8644
    EMsgClientToGCUnderDraftBuyResponse = 8645
    EMsgClientToGCUnderDraftReroll = 8646
    EMsgClientToGCUnderDraftRerollResponse = 8647
    EMsgNeutralItemStats = 8648
    EMsgClientToGCCreateGuild = 8649
    EMsgClientToGCCreateGuildResponse = 8650
    EMsgClientToGCSetGuildInfo = 8651
    EMsgClientToGCSetGuildInfoResponse = 8652
    EMsgClientToGCAddGuildRole = 8653
    EMsgClientToGCAddGuildRoleResponse = 8654
    EMsgClientToGCModifyGuildRole = 8655
    EMsgClientToGCModifyGuildRoleResponse = 8656
    EMsgClientToGCRemoveGuildRole = 8657
    EMsgClientToGCRemoveGuildRoleResponse = 8658
    EMsgClientToGCJoinGuild = 8659
    EMsgClientToGCJoinGuildResponse = 8660
    EMsgClientToGCLeaveGuild = 8661
    EMsgClientToGCLeaveGuildResponse = 8662
    EMsgClientToGCInviteToGuild = 8663
    EMsgClientToGCInviteToGuildResponse = 8664
    EMsgClientToGCDeclineInviteToGuild = 8665
    EMsgClientToGCDeclineInviteToGuildResponse = 8666
    EMsgClientToGCCancelInviteToGuild = 8667
    EMsgClientToGCCancelInviteToGuildResponse = 8668
    EMsgClientToGCKickGuildMember = 8669
    EMsgClientToGCKickGuildMemberResponse = 8670
    EMsgClientToGCSetGuildMemberRole = 8671
    EMsgClientToGCSetGuildMemberRoleResponse = 8672
    EMsgClientToGCRequestGuildData = 8673
    EMsgClientToGCRequestGuildDataResponse = 8674
    EMsgGCToClientGuildDataUpdated = 8675
    EMsgClientToGCRequestGuildMembership = 8676
    EMsgClientToGCRequestGuildMembershipResponse = 8677
    EMsgGCToClientGuildMembershipUpdated = 8678
    EMsgClientToGCRequestGuildSummary = 8679
    EMsgClientToGCRequestGuildSummaryResponse = 8680
    EMsgClientToGCAcceptInviteToGuild = 8681
    EMsgClientToGCAcceptInviteToGuildResponse = 8682
    EMsgClientToGCSetGuildRoleOrder = 8683
    EMsgClientToGCSetGuildRoleOrderResponse = 8684
    EMsgClientToGCRequestGuildFeed = 8685
    EMsgClientToGCRequestGuildFeedResponse = 8686
    EMsgClientToGCRequestAccountGuildEventData = 8687
    EMsgClientToGCRequestAccountGuildEventDataResponse = 8688
    EMsgGCToClientAccountGuildEventDataUpdated = 8689
    EMsgClientToGCRequestActiveGuildContracts = 8690
    EMsgClientToGCRequestActiveGuildContractsResponse = 8691
    EMsgGCToClientActiveGuildContractsUpdated = 8692
    EMsgGCToClientGuildFeedUpdated = 8693
    EMsgClientToGCSelectGuildContract = 8694
    EMsgClientToGCSelectGuildContractResponse = 8695
    EMsgGCToGCCompleteGuildContracts = 8696
    EMsgClientToGCAddPlayerToGuildChat = 8698
    EMsgClientToGCAddPlayerToGuildChatResponse = 8699
    EMsgClientToGCUnderDraftSell = 8700
    EMsgClientToGCUnderDraftSellResponse = 8701
    EMsgClientToGCUnderDraftRequest = 8702
    EMsgClientToGCUnderDraftResponse = 8703
    EMsgClientToGCUnderDraftRedeemReward = 8704
    EMsgClientToGCUnderDraftRedeemRewardResponse = 8705
    EMsgClientToGCUnderDraftRedeemSpecialReward = 8706
    EMsgClientToGCUnderDraftRedeemSpecialRewardResponse = 8707
    EMsgGCToServerLobbyHeroBanRates = 8708
    EMsgSetTeamFanContentStatus = 8709
    EMsgSetTeamFanContentStatusResponse = 8710
    EMsgSignOutGuildContractProgress = 8711
    EMsgSignOutMVPStats = 8712
    EMsgClientToGCRequestActiveGuildChallenge = 8713
    EMsgClientToGCRequestActiveGuildChallengeResponse = 8714
    EMsgGCToClientActiveGuildChallengeUpdated = 8715
    EMsgSignOutGuildChallengeProgress = 8720
    EMsgClientToGCRequestGuildEventMembers = 8721
    EMsgClientToGCRequestGuildEventMembersResponse = 8722
    EMsgClientToGCReportGuildContent = 8725
    EMsgClientToGCReportGuildContentResponse = 8726
    EMsgClientToGCRequestAccountGuildPersonaInfo = 8727
    EMsgClientToGCRequestAccountGuildPersonaInfoResponse = 8728
    EMsgClientToGCRequestAccountGuildPersonaInfoBatch = 8729
    EMsgClientToGCRequestAccountGuildPersonaInfoBatchResponse = 8730
    EMsgGCToClientUnderDraftGoldUpdated = 8731
    EMsgGCToServerRecordTrainingData = 8732
    EMsgSignOutBounties = 8733
    EMsgLobbyGauntletProgress = 8735
    EMsgClientToGCSubmitDraftTriviaMatchAnswer = 8736
    EMsgClientToGCSubmitDraftTriviaMatchAnswerResponse = 8737
    EMsgGCToGCSignoutSpendBounty = 8738
    EMsgClientToGCApplyGauntletTicket = 8739
    EMsgClientToGCUnderDraftRollBackBench = 8740
    EMsgClientToGCUnderDraftRollBackBenchResponse = 8741
    EMsgGCToGCGetEventActionScore = 8742
    EMsgGCToGCGetEventActionScoreResponse = 8743
    EMsgServerToGCGetGuildContracts = 8744
    EMsgServerToGCGetGuildContractsResponse = 8745
    EMsgLobbyEventGameData = 8746
    EMsgGCToClientGuildMembersDataUpdated = 8747
    EMsgSignOutReportActivityMarkers = 8748
    EMsgSignOutDiretideCandy = 8749
    EMsgGCToClientPostGameItemAwardNotification = 8750
    EMsgClientToGCGetOWMatchDetails = 8751
    EMsgClientToGCGetOWMatchDetailsResponse = 8752
    EMsgClientToGCSubmitOWConviction = 8753
    EMsgClientToGCSubmitOWConvictionResponse = 8754
    EMsgGCToGCGetAccountSteamChina = 8755
    EMsgGCToGCGetAccountSteamChinaResponse = 8756
    EMsgClientToGCClaimLeaderboardRewards = 8757
    EMsgClientToGCClaimLeaderboardRewardsResponse = 8758
    EMsgClientToGCRecalibrateMMR = 8759
    EMsgClientToGCRecalibrateMMRResponse = 8760
    EMsgGCToGCGrantEventPointActionList = 8761
    EMsgClientToGCChinaSSAURLRequest = 8764
    EMsgClientToGCChinaSSAURLResponse = 8765
    EMsgClientToGCChinaSSAAcceptedRequest = 8766
    EMsgClientToGCChinaSSAAcceptedResponse = 8767
    EMsgSignOutOverwatchSuspicion = 8768
    EMsgServerToGCGetSuspicionConfig = 8769
    EMsgServerToGCGetSuspicionConfigResponse = 8770
    EMsgGCToGCGrantPlusHeroChallengeMatchResults = 8771
    EMsgGCToClientOverwatchCasesAvailable = 8772
    EMsgServerToGCAccountCheck = 8773
    EMsgClientToGCStartWatchingOverwatch = 8774
    EMsgClientToGCStopWatchingOverwatch = 8775
    EMsgSignOutPerfData = 8776
    EMsgClientToGCGetDPCFavorites = 8777
    EMsgClientToGCGetDPCFavoritesResponse = 8778
    EMsgClientToGCSetDPCFavoriteState = 8779
    EMsgClientToGCSetDPCFavoriteStateResponse = 8780
    EMsgClientToGCOverwatchReplayError = 8781
    EMsgServerToGCPlayerChallengeHistory = 8782
    EMsgSignOutBanData = 8783
    EMsgWebapiDPCSeasonResults = 8784
    EMsgClientToGCCoachFriend = 8785
    EMsgClientToGCCoachFriendResponse = 8786
    EMsgClientToGCRequestPrivateCoachingSession = 8787
    EMsgClientToGCRequestPrivateCoachingSessionResponse = 8788
    EMsgClientToGCAcceptPrivateCoachingSession = 8789
    EMsgClientToGCAcceptPrivateCoachingSessionResponse = 8790
    EMsgClientToGCLeavePrivateCoachingSession = 8791
    EMsgClientToGCLeavePrivateCoachingSessionResponse = 8792
    EMsgClientToGCGetCurrentPrivateCoachingSession = 8793
    EMsgClientToGCGetCurrentPrivateCoachingSessionResponse = 8794
    EMsgGCToClientPrivateCoachingSessionUpdated = 8795
    EMsgClientToGCSubmitPrivateCoachingSessionRating = 8796
    EMsgClientToGCSubmitPrivateCoachingSessionRatingResponse = 8797
    EMsgClientToGCGetAvailablePrivateCoachingSessions = 8798
    EMsgClientToGCGetAvailablePrivateCoachingSessionsResponse = 8799
    EMsgClientToGCGetAvailablePrivateCoachingSessionsSummary = 8800
    EMsgClientToGCGetAvailablePrivateCoachingSessionsSummaryResponse = 8801
    EMsgClientToGCJoinPrivateCoachingSessionLobby = 8802
    EMsgClientToGCJoinPrivateCoachingSessionLobbyResponse = 8803
    EMsgClientToGCRespondToCoachFriendRequest = 8804
    EMsgClientToGCRespondToCoachFriendRequestResponse = 8805

class EDOTAGCSessionNeed(IntEnum):
    Unknown = 0
    UserNoSessionNeeded = 100
    UserInOnlineGame = 101
    UserInLocalGame = 102
    UserInUIWasConnected = 103
    UserInUINeverConnected = 104
    UserTutorials = 105
    UserInUIWasConnectedIdle = 106
    UserInUINeverConnectedIdle = 107
    GameServerOnline = 200
    GameServerLocal = 201
    GameServerIdle = 202
    GameServerRelay = 203
    GameServerLocalUpload = 204

class EDOTAGroupMergeResult(IntEnum):
    OK = 0
    FAILED_GENERIC = 1
    NOT_LEADER = 2
    TOO_MANY_PLAYERS = 3
    TOO_MANY_COACHES = 4
    ENGINE_MISMATCH = 5
    NO_SUCH_GROUP = 6
    OTHER_GROUP_NOT_OPEN = 7
    ALREADY_INVITED = 8
    NOT_INVITED = 9

EDOTAMMRBoostType = IntEnum('EDOTAMMRBoostType', {
    'None': 0,
    'Leader': 1,
    'Follower': 2,
    })

EDOTAPlayerMMRType = IntEnum('EDOTAPlayerMMRType', {
    'Invalid': 0,
    'GeneralHidden': 1,
    'GeneralCompetitive': 3,
    'SoloCompetitive2019': 4,
    '1v1Competitive_UNUSED': 5,
    })

class EDOTATriviaAnswerResult(IntEnum):
    Success = 0
    InvalidQuestion = 1
    InvalidAnswer = 2
    QuestionLocked = 3
    AlreadyAnswered = 4
    TriviaDisabled = 5

class EDOTATriviaQuestionCategory(IntEnum):
    AbilityIcon = 0
    AbilityCooldown = 1
    HeroAttributes = 2
    HeroMovementSpeed = 3
    TalentTree = 4
    HeroStats = 5
    ItemPrice = 6
    AbilitySound = 7
    InvokerSpells = 8
    AbilityManaCost = 9
    HeroAttackSound = 10
    AbilityName = 11
    ItemComponents = 12
    ItemLore = 13
    ItemPassives = 14

class EDPCFavoriteType(IntEnum):
    FAVORITE_TYPE_ALL = 0
    FAVORITE_TYPE_PLAYER = 1
    FAVORITE_TYPE_TEAM = 2
    FAVORITE_TYPE_LEAGUE = 3

class EDPCPushNotification(IntEnum):
    DPC_PUSH_NOTIFICATION_MATCH_STARTING = 1
    DPC_PUSH_NOTIFICATION_PLAYER_LEFT_TEAM = 10
    DPC_PUSH_NOTIFICATION_PLAYER_JOINED_TEAM = 11
    DPC_PUSH_NOTIFICATION_PLAYER_JOINED_TEAM_AS_COACH = 12
    DPC_PUSH_NOTIFICATION_PLAYER_LEFT_TEAM_AS_COACH = 13
    DPC_PUSH_NOTIFICATION_LEAGUE_RESULT = 20
    DPC_PUSH_NOTIFICATION_PREDICTION_MATCHES_AVAILABLE = 30
    DPC_PUSH_NOTIFICATION_PREDICTION_RESULT = 31
    DPC_PUSH_NOTIFICATION_FANTASY_PLAYER_CLEARED = 40
    DPC_PUSH_NOTIFICATION_FANTASY_DAILY_SUMMARY = 41
    DPC_PUSH_NOTIFICATION_FANTASY_FINAL_RESULTS = 42

class EEvent(IntEnum):
    EVENT_ID_NONE = 0
    EVENT_ID_DIRETIDE = 1
    EVENT_ID_SPRING_FESTIVAL = 2
    EVENT_ID_FROSTIVUS_2013 = 3
    EVENT_ID_COMPENDIUM_2014 = 4
    EVENT_ID_NEXON_PC_BANG = 5
    EVENT_ID_PWRD_DAC_2015 = 6
    EVENT_ID_NEW_BLOOM_2015 = 7
    EVENT_ID_INTERNATIONAL_2015 = 8
    EVENT_ID_FALL_MAJOR_2015 = 9
    EVENT_ID_ORACLE_PA = 10
    EVENT_ID_NEW_BLOOM_2015_PREBEAST = 11
    EVENT_ID_FROSTIVUS = 12
    EVENT_ID_WINTER_MAJOR_2016 = 13
    EVENT_ID_INTERNATIONAL_2016 = 14
    EVENT_ID_FALL_MAJOR_2016 = 15
    EVENT_ID_WINTER_MAJOR_2017 = 16
    EVENT_ID_NEW_BLOOM_2017 = 17
    EVENT_ID_INTERNATIONAL_2017 = 18
    EVENT_ID_PLUS_SUBSCRIPTION = 19
    EVENT_ID_SINGLES_DAY_2017 = 20
    EVENT_ID_FROSTIVUS_2017 = 21
    EVENT_ID_INTERNATIONAL_2018 = 22
    EVENT_ID_FROSTIVUS_2018 = 23
    EVENT_ID_NEW_BLOOM_2019 = 24
    EVENT_ID_INTERNATIONAL_2019 = 25
    EVENT_ID_NEW_PLAYER_EXPERIENCE = 26
    EVENT_ID_FROSTIVUS_2019 = 27
    EVENT_ID_NEW_BLOOM_2020 = 28
    EVENT_ID_INTERNATIONAL_2020 = 29
    EVENT_ID_TEAM_FANDOM = 30
    EVENT_ID_DIRETIDE_2020 = 31
    EVENT_ID_SPRING_2021 = 32
    EVENT_ID_COUNT = 33

class EEventActionScoreMode(IntEnum):
    eEventActionScoreMode_Add = 0
    eEventActionScoreMode_Min = 1

class EFeaturedHeroDataType(IntEnum):
    HeroID = 0
    ItemDef = 1
    HypeString = 2
    StartTimestamp = 3
    ExpireTimestamp = 4
    HeroWins = 5
    HeroLosses = 6
    SaleDiscount = 7
    ContainerItemDef = 8

class EFeaturedHeroTextField(IntEnum):
    NewHero = 0
    NewItem = 1
    ItemSetDescription = 2
    ItemDescription = 3
    Hype = 4
    HeroWinLoss = 5
    FrequentlyPlayedHero = 6
    FeaturedItem = 7
    PopularItem = 8
    SaleItem = 9
    SaleDiscount = 10
    Container = 11

class EGCBaseClientMsg(IntEnum):
    EMsgGCPingRequest = 3001
    EMsgGCPingResponse = 3002
    EMsgGCToClientPollConvarRequest = 3003
    EMsgGCToClientPollConvarResponse = 3004
    EMsgGCCompressedMsgToClient = 3005
    EMsgGCCompressedMsgToClient_Legacy = 523
    EMsgGCToClientRequestDropped = 3006
    EMsgGCClientWelcome = 4004
    EMsgGCServerWelcome = 4005
    EMsgGCClientHello = 4006
    EMsgGCServerHello = 4007
    EMsgGCClientConnectionStatus = 4009
    EMsgGCServerConnectionStatus = 4010

class EGCBaseMsg(IntEnum):
    EMsgGCSystemMessage = 4001
    EMsgGCReplicateConVars = 4002
    EMsgGCConVarUpdated = 4003
    EMsgGCInviteToParty = 4501
    EMsgGCInvitationCreated = 4502
    EMsgGCPartyInviteResponse = 4503
    EMsgGCKickFromParty = 4504
    EMsgGCLeaveParty = 4505
    EMsgGCServerAvailable = 4506
    EMsgGCClientConnectToServer = 4507
    EMsgGCGameServerInfo = 4508
    EMsgGCError = 4509
    EMsgGCLANServerAvailable = 4511
    EMsgGCInviteToLobby = 4512
    EMsgGCLobbyInviteResponse = 4513
    EMsgGCToClientPollFileRequest = 4514
    EMsgGCToClientPollFileResponse = 4515
    EMsgGCToGCPerformManualOp = 4516
    EMsgGCToGCPerformManualOpCompleted = 4517
    EMsgGCToGCReloadServerRegionSettings = 4518
    EMsgGCAdditionalWelcomeMsgList = 4519

class EGCBaseProtoObjectTypes(IntEnum):
    EProtoObjectPartyInvite = 1001
    EProtoObjectLobbyInvite = 1002

class EGCEconBaseMsg(IntEnum):
    EMsgGCGenericResult = 2579

class EGCItemMsg(IntEnum):
    EMsgGCBase = 1000
    EMsgGCSetItemPosition = 1001
    EMsgGCDelete = 1004
    EMsgGCVerifyCacheSubscription = 1005
    EMsgClientToGCNameItem = 1006
    EMsgGCPaintItem = 1009
    EMsgGCPaintItemResponse = 1010
    EMsgGCGoldenWrenchBroadcast = 1011
    EMsgGCMOTDRequest = 1012
    EMsgGCMOTDRequestResponse = 1013
    EMsgGCAddItemToSocket_DEPRECATED = 1014
    EMsgGCAddItemToSocketResponse_DEPRECATED = 1015
    EMsgGCAddSocketToBaseItem_DEPRECATED = 1016
    EMsgGCAddSocketToItem_DEPRECATED = 1017
    EMsgGCAddSocketToItemResponse_DEPRECATED = 1018
    EMsgGCNameBaseItem = 1019
    EMsgGCNameBaseItemResponse = 1020
    EMsgGCRemoveSocketItem_DEPRECATED = 1021
    EMsgGCRemoveSocketItemResponse_DEPRECATED = 1022
    EMsgGCCustomizeItemTexture = 1023
    EMsgGCCustomizeItemTextureResponse = 1024
    EMsgGCUseItemRequest = 1025
    EMsgGCUseItemResponse = 1026
    EMsgGCGiftedItems = 1027
    EMsgGCRemoveItemName = 1030
    EMsgGCRemoveItemPaint = 1031
    EMsgGCUnwrapGiftRequest = 1037
    EMsgGCUnwrapGiftResponse = 1038
    EMsgGCSetItemStyle_DEPRECATED = 1039
    EMsgGCUsedClaimCodeItem = 1040
    EMsgGCSortItems = 1041
    EMsgGC_RevolvingLootList_DEPRECATED = 1042
    EMsgGCUpdateItemSchema = 1049
    EMsgGCRemoveCustomTexture = 1051
    EMsgGCRemoveCustomTextureResponse = 1052
    EMsgGCRemoveMakersMark = 1053
    EMsgGCRemoveMakersMarkResponse = 1054
    EMsgGCRemoveUniqueCraftIndex = 1055
    EMsgGCRemoveUniqueCraftIndexResponse = 1056
    EMsgGCSaxxyBroadcast = 1057
    EMsgGCBackpackSortFinished = 1058
    EMsgGCAdjustItemEquippedState = 1059
    EMsgGCCollectItem = 1061
    EMsgGCItemAcknowledged = 1062
    EMsgGCPresets_SelectPresetForClass = 1063
    EMsgGCPresets_SetItemPosition = 1064
    EMsgGCPresets_SelectPresetForClassReply = 1067
    EMsgClientToGCNameItemResponse = 1068
    EMsgGCApplyConsumableEffects = 1069
    EMsgGCShowItemsPickedUp = 1071
    EMsgGCClientDisplayNotification = 1072
    EMsgGCApplyStrangePart = 1073
    EMsgGC_IncrementKillCountResponse = 1075
    EMsgGCApplyPennantUpgrade = 1076
    EMsgGCSetItemPositions = 1077
    EMsgGCSetItemPositions_RateLimited = 1096
    EMsgGCApplyEggEssence = 1078
    EMsgGCNameEggEssenceResponse = 1079
    EMsgGCFulfillDynamicRecipeComponent = 1082
    EMsgGCFulfillDynamicRecipeComponentResponse = 1083
    EMsgGCClientRequestMarketData = 1084
    EMsgGCClientRequestMarketDataResponse = 1085
    EMsgGCExtractGems = 1086
    EMsgGCAddSocket = 1087
    EMsgGCAddItemToSocket = 1088
    EMsgGCAddItemToSocketResponse = 1089
    EMsgGCAddSocketResponse = 1090
    EMsgGCResetStrangeGemCount = 1091
    EMsgGCRequestCrateItems = 1092
    EMsgGCRequestCrateItemsResponse = 1093
    EMsgGCExtractGemsResponse = 1094
    EMsgGCResetStrangeGemCountResponse = 1095
    EMsgGCServerUseItemRequest = 1103
    EMsgGCAddGiftItem = 1104
    EMsgGCRemoveItemGiftMessage = 1105
    EMsgGCRemoveItemGiftMessageResponse = 1106
    EMsgGCRemoveItemGifterAccountId = 1107
    EMsgGCRemoveItemGifterAccountIdResponse = 1108
    EMsgClientToGCRemoveItemGifterAttributes = 1109
    EMsgClientToGCRemoveItemName = 1110
    EMsgClientToGCRemoveItemDescription = 1111
    EMsgClientToGCRemoveItemAttributeResponse = 1112
    EMsgGCTradingBase = 1500
    EMsgGCTrading_InitiateTradeRequest = 1501
    EMsgGCTrading_InitiateTradeResponse = 1502
    EMsgGCTrading_StartSession = 1503
    EMsgGCTrading_SessionClosed = 1509
    EMsgGCTrading_InitiateTradeRequestResponse = 1514
    EMsgGCServerBrowser_FavoriteServer = 1601
    EMsgGCServerBrowser_BlacklistServer = 1602
    EMsgGCServerRentalsBase = 1700
    EMsgGCDev_NewItemRequest = 2001
    EMsgGCDev_NewItemRequestResponse = 2002
    EMsgGCDev_UnlockAllItemStylesRequest = 2003
    EMsgGCDev_UnlockAllItemStylesResponse = 2004
    EMsgGCStorePurchaseFinalize = 2504
    EMsgGCStorePurchaseFinalizeResponse = 2505
    EMsgGCStorePurchaseCancel = 2506
    EMsgGCStorePurchaseCancelResponse = 2507
    EMsgGCStorePurchaseInit = 2510
    EMsgGCStorePurchaseInitResponse = 2511
    EMsgGCToGCBannedWordListUpdated = 2515
    EMsgGCToGCDirtySDOCache = 2516
    EMsgGCToGCDirtyMultipleSDOCache = 2517
    EMsgGCToGCUpdateSQLKeyValue = 2518
    EMsgGCToGCBroadcastConsoleCommand = 2521
    EMsgGCServerVersionUpdated = 2522
    EMsgGCApplyAutograph = 2523
    EMsgGCToGCWebAPIAccountChanged = 2524
    EMsgGCClientVersionUpdated = 2528
    EMsgGCToGCUpdateWelcomeMsg = 2529
    EMsgGCItemPurgatory_FinalizePurchase = 2531
    EMsgGCItemPurgatory_FinalizePurchaseResponse = 2532
    EMsgGCItemPurgatory_RefundPurchase = 2533
    EMsgGCItemPurgatory_RefundPurchaseResponse = 2534
    EMsgGCToGCPlayerStrangeCountAdjustments = 2535
    EMsgGCRequestStoreSalesData = 2536
    EMsgGCRequestStoreSalesDataResponse = 2537
    EMsgGCRequestStoreSalesDataUpToDateResponse = 2538
    EMsgGCToGCPingRequest = 2539
    EMsgGCToGCPingResponse = 2540
    EMsgGCToGCGetUserSessionServer = 2541
    EMsgGCToGCGetUserSessionServerResponse = 2542
    EMsgGCToGCGetUserServerMembers = 2543
    EMsgGCToGCGetUserServerMembersResponse = 2544
    EMsgGCToGCGetUserPCBangNo = 2545
    EMsgGCToGCGetUserPCBangNoResponse = 2546
    EMsgGCToGCCanUseDropRateBonus = 2547
    EMsgSQLAddDropRateBonus = 2548
    EMsgGCToGCRefreshSOCache = 2549
    EMsgGCToGCApplyLocalizationDiff = 2550
    EMsgGCToGCApplyLocalizationDiffResponse = 2551
    EMsgGCToGCCheckAccountTradeStatus = 2552
    EMsgGCToGCCheckAccountTradeStatusResponse = 2553
    EMsgGCToGCGrantAccountRolledItems = 2554
    EMsgGCToGCGrantSelfMadeItemToAccount = 2555
    EMsgGCPartnerBalanceRequest = 2557
    EMsgGCPartnerBalanceResponse = 2558
    EMsgGCPartnerRechargeRedirectURLRequest = 2559
    EMsgGCPartnerRechargeRedirectURLResponse = 2560
    EMsgGCStatueCraft = 2561
    EMsgGCRedeemCode = 2562
    EMsgGCRedeemCodeResponse = 2563
    EMsgGCToGCItemConsumptionRollback = 2564
    EMsgClientToGCWrapAndDeliverGift = 2565
    EMsgClientToGCWrapAndDeliverGiftResponse = 2566
    EMsgClientToGCUnpackBundleResponse = 2567
    EMsgGCToClientStoreTransactionCompleted = 2568
    EMsgClientToGCEquipItems = 2569
    EMsgClientToGCEquipItemsResponse = 2570
    EMsgClientToGCUnlockItemStyle = 2571
    EMsgClientToGCUnlockItemStyleResponse = 2572
    EMsgClientToGCSetItemInventoryCategory = 2573
    EMsgClientToGCUnlockCrate = 2574
    EMsgClientToGCUnlockCrateResponse = 2575
    EMsgClientToGCUnpackBundle = 2576
    EMsgClientToGCSetItemStyle = 2577
    EMsgClientToGCSetItemStyleResponse = 2578
    EMsgSQLGCToGCGrantBackpackSlots = 2580
    EMsgClientToGCLookupAccountName = 2581
    EMsgClientToGCLookupAccountNameResponse = 2582
    EMsgGCToGCDevRevokeUserItems = 2583
    EMsgClientToGCCreateStaticRecipe = 2584
    EMsgClientToGCCreateStaticRecipeResponse = 2585
    EMsgGCToGCStoreProcessCDKeyTransaction = 2586
    EMsgGCToGCStoreProcessCDKeyTransactionResponse = 2587
    EMsgGCToGCStoreProcessSettlement = 2588
    EMsgGCToGCStoreProcessSettlementResponse = 2589
    EMsgGCToGCConsoleOutput = 2590
    EMsgGCToClientItemAges = 2591
    EMsgGCToGCInternalTestMsg = 2592
    EMsgGCToGCClientServerVersionsUpdated = 2593
    EMsgGCUseMultipleItemsRequest = 2594
    EMsgGCGetAccountSubscriptionItem = 2595
    EMsgGCGetAccountSubscriptionItemResponse = 2596
    EMsgGCToGCBroadcastMessageFromSub = 2598
    EMsgGCToClientCurrencyPricePoints = 2599
    EMsgGCToGCAddSubscriptionTime = 2600
    EMsgGCToGCFlushSteamInventoryCache = 2601
    EMsgGCRequestCrateEscalationLevel = 2602
    EMsgGCRequestCrateEscalationLevelResponse = 2603
    EMsgGCToGCUpdateSubscriptionItems = 2604
    EMsgGCToGCSelfPing = 2605
    EMsgGCToGCGetInfuxIntervalStats = 2606
    EMsgGCToGCGetInfuxIntervalStatsResponse = 2607
    EMsgGCToGCPurchaseSucceeded = 2608
    EMsgClientToGCGetLimitedItemPurchaseQuantity = 2609
    EMsgClientToGCGetLimitedItemPurchaseQuantityResponse = 2610

class EGCMsgInitiateTradeResponse(IntEnum):
    Accepted = 0
    Declined = 1
    VAC_Banned_Initiator = 2
    VAC_Banned_Target = 3
    Target_Already_Trading = 4
    Disabled = 5
    NotLoggedIn = 6
    Cancel = 7
    TooSoon = 8
    TooSoonPenalty = 9
    Trade_Banned_Initiator = 10
    Trade_Banned_Target = 11
    Free_Account_Initiator_DEPRECATED = 12
    Shared_Account_Initiator = 13
    Service_Unavailable = 14
    Target_Blocked = 15
    NeedVerifiedEmail = 16
    NeedSteamGuard = 17
    SteamGuardDuration = 18
    TheyCannotTrade = 19
    Recent_Password_Reset = 20
    Using_New_Device = 21
    Sent_Invalid_Cookie = 22
    TooRecentFriend = 23
    WalledFundsNotTrusted = 24

class EGCMsgResponse(IntEnum):
    EGCMsgResponseOK = 0
    EGCMsgResponseDenied = 1
    EGCMsgResponseServerError = 2
    EGCMsgResponseTimeout = 3
    EGCMsgResponseInvalid = 4
    EGCMsgResponseNoMatch = 5
    EGCMsgResponseUnknownError = 6
    EGCMsgResponseNotLoggedOn = 7
    EGCMsgFailedToCreate = 8

class EGCMsgUseItemResponse(IntEnum):
    ItemUsed = 0
    GiftNoOtherPlayers = 1
    ServerError = 2
    MiniGameAlreadyStarted = 3
    ItemUsed_ItemsGranted = 4
    DropRateBonusAlreadyGranted = 5
    NotInLowPriorityPool = 6
    NotHighEnoughLevel = 7
    EventNotActive = 8
    ItemUsed_EventPointsGranted = 9
    MissingRequirement = 10
    EmoticonUnlock_NoNew = 11
    EmoticonUnlock_Complete = 12
    ItemUsed_Compendium = 13

class EGCPartnerRequestResponse(IntEnum):
    EPartnerRequestOK = 1
    EPartnerRequestBadAccount = 2
    EPartnerRequestNotLinked = 3
    EPartnerRequestUnsupportedPartnerType = 4

class EHeroRelicRarity(IntEnum):
    HERO_RELIC_RARITY_INVALID = -1
    HERO_RELIC_RARITY_COMMON = 0
    HERO_RELIC_RARITY_RARE = 1

class EHighPriorityMMState(IntEnum):
    EHighPriorityMM_Unknown = 0
    EHighPriorityMM_MissingMMData = 1
    EHighPriorityMM_ResourceMissing = 2
    EHighPriorityMM_ManuallyDisabled = 3
    EHighPriorityMM_Min_Enabled = 64
    EHighPriorityMM_AllRolesSelected = 65
    EHighPriorityMM_UsingResource = 66
    EHighPriorityMM_FiveStack = 67
    EHighPriorityMM_HighDemand = 68

class EItemEditorReservationResult(IntEnum):
    OK = 1
    AlreadyExists = 2
    Reserved = 3
    TimedOut = 4

class EItemPurgatoryResponse_Finalize(IntEnum):
    ItemPurgatoryResponse_Finalize_Succeeded = 0
    ItemPurgatoryResponse_Finalize_Failed_Incomplete = 1
    ItemPurgatoryResponse_Finalize_Failed_ItemsNotInPurgatory = 2
    ItemPurgatoryResponse_Finalize_Failed_CouldNotFindItems = 3
    ItemPurgatoryResponse_Finalize_Failed_NoSOCache = 4
    ItemPurgatoryResponse_Finalize_BackpackFull = 5

class EItemPurgatoryResponse_Refund(IntEnum):
    ItemPurgatoryResponse_Refund_Succeeded = 0
    ItemPurgatoryResponse_Refund_Failed_ItemNotInPurgatory = 1
    ItemPurgatoryResponse_Refund_Failed_CouldNotFindItem = 2
    ItemPurgatoryResponse_Refund_Failed_NoSOCache = 3
    ItemPurgatoryResponse_Refund_Failed_NoDetail = 4

class ELaneSelection(IntEnum):
    SAFELANE = 0
    OFFLANE = 1
    MIDLANE = 2
    SUPPORT_SOFT = 3
    SUPPORT_HARD = 4

ELaneSelectionFlags = IntEnum('ELaneSelectionFlags', {
    'None': 0,
    'SAFELANE': 1,
    'OFFLANE': 2,
    'MIDLANE': 4,
    'CORE': 7,
    'SUPPORT_SOFT': 8,
    'SUPPORT_HARD': 16,
    'SUPPORT': 24,
    'ALL': 31,
    })

class ELaneType(IntEnum):
    LANE_TYPE_UNKNOWN = 0
    LANE_TYPE_SAFE = 1
    LANE_TYPE_OFF = 2
    LANE_TYPE_MID = 3
    LANE_TYPE_JUNGLE = 4
    LANE_TYPE_ROAM = 5

class ELeagueAuditAction(IntEnum):
    LEAGUE_AUDIT_ACTION_INVALID = 0
    LEAGUE_AUDIT_ACTION_LEAGUE_CREATE = 1
    LEAGUE_AUDIT_ACTION_LEAGUE_EDIT = 2
    LEAGUE_AUDIT_ACTION_LEAGUE_DELETE = 3
    LEAGUE_AUDIT_ACTION_LEAGUE_ADMIN_ADD = 4
    LEAGUE_AUDIT_ACTION_LEAGUE_ADMIN_REVOKE = 5
    LEAGUE_AUDIT_ACTION_LEAGUE_ADMIN_PROMOTE = 6
    LEAGUE_AUDIT_ACTION_LEAGUE_STREAM_ADD = 7
    LEAGUE_AUDIT_ACTION_LEAGUE_STREAM_REMOVE = 8
    LEAGUE_AUDIT_ACTION_LEAGUE_IMAGE_UPDATED = 9
    LEAGUE_AUDIT_ACTION_LEAGUE_MESSAGE_ADDED = 10
    LEAGUE_AUDIT_ACTION_LEAGUE_SUBMITTED = 11
    LEAGUE_AUDIT_ACTION_LEAGUE_SET_PRIZE_POOL = 12
    LEAGUE_AUDIT_ACTION_LEAGUE_ADD_PRIZE_POOL_ITEM = 13
    LEAGUE_AUDIT_ACTION_LEAGUE_REMOVE_PRIZE_POOL_ITEM = 14
    LEAGUE_AUDIT_ACTION_LEAGUE_MATCH_START = 15
    LEAGUE_AUDIT_ACTION_LEAGUE_MATCH_END = 16
    LEAGUE_AUDIT_ACTION_LEAGUE_ADD_INVITED_TEAM = 17
    LEAGUE_AUDIT_ACTION_LEAGUE_REMOVE_INVITED_TEAM = 18
    LEAGUE_AUDIT_ACTION_LEAGUE_STATUS_CHANGED = 19
    LEAGUE_AUDIT_ACTION_LEAGUE_STREAM_EDIT = 20
    LEAGUE_AUDIT_ACTION_LEAGUE_TEAM_SWAP = 21
    LEAGUE_AUDIT_ACTION_NODEGROUP_CREATE = 100
    LEAGUE_AUDIT_ACTION_NODEGROUP_DESTROY = 101
    LEAGUE_AUDIT_ACTION_NODEGROUP_ADD_TEAM = 102
    LEAGUE_AUDIT_ACTION_NODEGROUP_REMOVE_TEAM = 103
    LEAGUE_AUDIT_ACTION_NODEGROUP_SET_ADVANCING = 104
    LEAGUE_AUDIT_ACTION_NODEGROUP_EDIT = 105
    LEAGUE_AUDIT_ACTION_NODEGROUP_POPULATE = 106
    LEAGUE_AUDIT_ACTION_NODEGROUP_COMPLETED = 107
    LEAGUE_AUDIT_ACTION_NODEGROUP_SET_SECONDARY_ADVANCING = 108
    LEAGUE_AUDIT_ACTION_NODEGROUP_SET_TERTIARY_ADVANCING = 109
    LEAGUE_AUDIT_ACTION_NODE_CREATE = 200
    LEAGUE_AUDIT_ACTION_NODE_DESTROY = 201
    LEAGUE_AUDIT_ACTION_NODE_AUTOCREATE = 202
    LEAGUE_AUDIT_ACTION_NODE_SET_TEAM = 203
    LEAGUE_AUDIT_ACTION_NODE_SET_SERIES_ID = 204
    LEAGUE_AUDIT_ACTION_NODE_SET_ADVANCING = 205
    LEAGUE_AUDIT_ACTION_NODE_SET_TIME = 206
    LEAGUE_AUDIT_ACTION_NODE_MATCH_COMPLETED = 207
    LEAGUE_AUDIT_ACTION_NODE_COMPLETED = 208
    LEAGUE_AUDIT_ACTION_NODE_EDIT = 209

class ELeagueBroadcastProvider(IntEnum):
    LEAGUE_BROADCAST_UNKNOWN = 0
    LEAGUE_BROADCAST_STEAM = 1
    LEAGUE_BROADCAST_TWITCH = 2
    LEAGUE_BROADCAST_YOUTUBE = 3
    LEAGUE_BROADCAST_OTHER = 100

class ELeagueFlags(IntEnum):
    LEAGUE_FLAGS_NONE = 0
    LEAGUE_ACCEPTED_AGREEMENT = 1
    LEAGUE_PAYMENT_EMAIL_SENT = 2
    LEAGUE_COMPENDIUM_ALLOWED = 4
    LEAGUE_COMPENDIUM_PUBLIC = 8

class ELeaguePhase(IntEnum):
    LEAGUE_PHASE_UNSET = 0
    LEAGUE_PHASE_REGIONAL_QUALIFIER = 1
    LEAGUE_PHASE_GROUP_STAGE = 2
    LEAGUE_PHASE_MAIN_EVENT = 3

class ELeagueRegion(IntEnum):
    LEAGUE_REGION_UNSET = 0
    LEAGUE_REGION_NA = 1
    LEAGUE_REGION_SA = 2
    LEAGUE_REGION_EUROPE = 3
    LEAGUE_REGION_CIS = 4
    LEAGUE_REGION_CHINA = 5
    LEAGUE_REGION_SEA = 6

class ELeagueStatus(IntEnum):
    LEAGUE_STATUS_UNSET = 0
    LEAGUE_STATUS_UNSUBMITTED = 1
    LEAGUE_STATUS_SUBMITTED = 2
    LEAGUE_STATUS_ACCEPTED = 3
    LEAGUE_STATUS_REJECTED = 4
    LEAGUE_STATUS_CONCLUDED = 5
    LEAGUE_STATUS_DELETED = 6

class ELeagueTier(IntEnum):
    LEAGUE_TIER_UNSET = 0
    LEAGUE_TIER_AMATEUR = 1
    LEAGUE_TIER_PROFESSIONAL = 2
    LEAGUE_TIER_MINOR = 3
    LEAGUE_TIER_MAJOR = 4
    LEAGUE_TIER_INTERNATIONAL = 5
    LEAGUE_TIER_DPC_QUALIFIER = 6
    LEAGUE_TIER_DPC_LEAGUE_QUALIFIER = 7
    LEAGUE_TIER_DPC_LEAGUE = 8

class ELeagueTierCategory(IntEnum):
    LEAGUE_TIER_CATEGORY_AMATEUR = 1
    LEAGUE_TIER_CATEGORY_PROFESSIONAL = 2
    LEAGUE_TIER_CATEGORY_DPC = 3

class ELobbyMemberCoachRequestState(IntEnum):
    eLobbyMemberCoachRequestState_None = 0
    eLobbyMemberCoachRequestState_Accepted = 1
    eLobbyMemberCoachRequestState_Rejected = 2

class EMatchBehaviorScoreVariance(IntEnum):
    Invalid = 0
    Low = 1
    Medium = 2
    High = 3

class EMatchGroupServerStatus(IntEnum):
    OK = 0
    LimitedAvailability = 1
    Offline = 2

class EMatchOutcome(IntEnum):
    Unknown = 0
    RadVictory = 2
    DireVictory = 3
    NotScored_PoorNetworkConditions = 64
    NotScored_Leaver = 65
    NotScored_ServerCrash = 66
    NotScored_NeverStarted = 67
    NotScored_Canceled = 68
    NotScored_Suspicious = 69

class EMobilePaymentProvider(IntEnum):
    Invalid = 0
    GooglePlay = 1
    AppleAppStore = 2

EOverwatchConviction = IntEnum('EOverwatchConviction', {
    'None': 0,
    'NotGuilty': 1,
    'GuiltUnclear': 2,
    'Guilty': 3,
    })

class EOverwatchReportReason(IntEnum):
    Unknown = 0
    Cheating = 1
    Feeding = 2
    Griefing = 3
    Suspicious = 4
    AbilityAbuse = 5

class EPartyBeaconType(IntEnum):
    Available = 0
    Joinable = 1

EPartyMatchmakingFlags = IntEnum('EPartyMatchmakingFlags', {
    'None': 0,
    'LargeRankSpread': 1,
    })

class EPlayerChallengeHistoryType(IntEnum):
    Invalid = 0
    KillEater = 1
    DotaPlusRelic = 2
    DotaPlusHeroPlayerChallenge = 3
    InGameEventChallenge = 4
    GuildContract = 5

class EProfileCardSlotType(IntEnum):
    Empty = 0
    Stat = 1
    Trophy = 2
    Item = 3
    Hero = 4
    Emoticon = 5
    Team = 6

class EPurchaseHeroRelicResult(IntEnum):
    Success = 0
    FailedToSend = 1
    NotEnoughPoints = 2
    InternalServerError = 3
    PurchaseNotAllowed = 4
    InvalidRelic = 5
    AlreadyOwned = 6
    InvalidRarity = 7

class EReadyCheckRequestResult(IntEnum):
    Success = 0
    AlreadyInProgress = 1
    NotInParty = 2
    SendError = 3
    UnknownError = 4

class EReadyCheckStatus(IntEnum):
    Unknown = 0
    NotReady = 1
    Ready = 2

class ESOMsg(IntEnum):
    Create = 21
    Update = 22
    Destroy = 23
    CacheSubscribed = 24
    CacheUnsubscribed = 25
    UpdateMultiple = 26
    CacheSubscriptionRefresh = 28
    CacheSubscribedUpToDate = 29

class ESourceEngine(IntEnum):
    ESE_Source1 = 0
    ESE_Source2 = 1

class ESpecialPingValue(IntEnum):
    NoData = 16382
    Failed = 16383

class EStartFindingMatchResult(IntEnum):
    Invalid = 0
    OK = 1
    AlreadySearching = 2
    FailGeneric = 100
    FailedIgnore = 101
    MatchmakingDisabled = 102
    RegionOffline = 103
    MatchmakingCooldown = 104
    ClientOutOfDate = 105
    CompetitiveNoLowPriority = 106
    CompetitiveNotUnlocked = 107
    GameModeNotUnlocked = 108
    CompetitiveNotEnoughPlayTime = 109
    MissingInitialSkill = 110
    CompetitiveRankSpreadTooLarge = 111
    MemberAlreadyInLobby = 112
    MemberNotVACVerified = 113
    WeekendTourneyBadPartySize = 114
    WeekendTourneyTeamBuyInTooSmall = 115
    WeekendTourneyIndividualBuyInTooLarge = 116
    WeekendTourneyTeamBuyInTooLarge = 117
    MemberMissingEventOwnership = 118
    WeekendTourneyNotUnlocked = 119
    WeekendTourneyRecentParticipation = 120
    MemberMissingAnchoredPhoneNumber = 121
    NotMemberOfClan = 122
    CoachesChallengeBadPartySize = 123
    CoachesChallengeRequirementsNotMet = 124
    InvalidRoleSelections = 125
    PhoneNumberDiscrepancy = 126
    NoQueuePoints = 127
    MemberMissingGauntletFlag = 128
    MemberGauntletTooRecent = 129
    DifficultyNotUnlocked = 130
    CoachesNotAllowedInParty = 131
    MatchmakingBusy = 132
    SteamChinaBanned = 133
    SteamChinaInvalidMixedParty = 134

class ESupportEventRequestResult(IntEnum):
    Success = 0
    Timeout = 1
    CantLockSOCache = 2
    ItemNotInInventory = 3
    InvalidItemDef = 4
    InvalidEvent = 5
    EventExpired = 6
    InvalidSupportAccount = 7
    InvalidSupportMessage = 8
    InvalidEventPoints = 9
    InvalidPremiumPoints = 10
    InvalidActionID = 11
    InvalidActionScore = 12
    TransactionFailed = 13

class ETeamFanContentStatus(IntEnum):
    TEAM_FAN_CONTENT_STATUS_INVALID = 0
    TEAM_FAN_CONTENT_STATUS_PENDING = 1
    TEAM_FAN_CONTENT_STATUS_EVALUATED = 2

class ETeamInviteResult(IntEnum):
    TEAM_INVITE_SUCCESS = 0
    TEAM_INVITE_FAILURE_INVITE_REJECTED = 1
    TEAM_INVITE_FAILURE_INVITE_TIMEOUT = 2
    TEAM_INVITE_ERROR_TEAM_AT_MEMBER_LIMIT = 3
    TEAM_INVITE_ERROR_TEAM_LOCKED = 4
    TEAM_INVITE_ERROR_INVITEE_NOT_AVAILABLE = 5
    TEAM_INVITE_ERROR_INVITEE_BUSY = 6
    TEAM_INVITE_ERROR_INVITEE_ALREADY_MEMBER = 7
    TEAM_INVITE_ERROR_INVITEE_AT_TEAM_LIMIT = 8
    TEAM_INVITE_ERROR_INVITEE_INSUFFICIENT_PLAY_TIME = 9
    TEAM_INVITE_ERROR_INVITER_INVALID_ACCOUNT_TYPE = 10
    TEAM_INVITE_ERROR_INVITER_NOT_ADMIN = 11
    TEAM_INVITE_ERROR_INCORRECT_USER_RESPONDED = 12
    TEAM_INVITE_ERROR_UNSPECIFIED = 13

ETournamentEvent = IntEnum('ETournamentEvent', {
    'None': 0,
    'TournamentCreated': 1,
    'TournamentsMerged': 2,
    'GameOutcome': 3,
    'TeamGivenBye': 4,
    'TournamentCanceledByAdmin': 5,
    'TeamAbandoned': 6,
    'ScheduledGameStarted': 7,
    'Canceled': 8,
    'TeamParticipationTimedOut_EntryFeeRefund': 9,
    'TeamParticipationTimedOut_EntryFeeForfeit': 10,
    'TeamParticipationTimedOut_GrantedVictory': 11,
    })

class ETournamentGameState(IntEnum):
    Unknown = 0
    Canceled = 1
    Scheduled = 2
    Active = 3
    RadVictory = 20
    DireVictory = 21
    RadVictoryByForfeit = 22
    DireVictoryByForfeit = 23
    ServerFailure = 40
    NotNeeded = 41

class ETournamentNodeState(IntEnum):
    Unknown = 0
    Canceled = 1
    TeamsNotYetAssigned = 2
    InBetweenGames = 3
    GameInProgress = 4
    A_Won = 5
    B_Won = 6
    A_WonByForfeit = 7
    B_WonByForfeit = 8
    A_Bye = 9
    A_Abandoned = 10
    ServerFailure = 11
    A_TimeoutForfeit = 12
    A_TimeoutRefund = 13

class ETournamentState(IntEnum):
    Unknown = 0
    CanceledByAdmin = 1
    Completed = 2
    Merged = 3
    ServerFailure = 4
    TeamAbandoned = 5
    TeamTimeoutForfeit = 6
    TeamTimeoutRefund = 7
    ServerFailureGrantedVictory = 8
    TeamTimeoutGrantedVictory = 9
    InProgress = 100
    WaitingToMerge = 101

class ETournamentTeamState(IntEnum):
    Unknown = 0
    Node1 = 1
    NodeMax = 1024
    Eliminated = 14003
    Forfeited = 14004
    Finished1st = 15001
    Finished2nd = 15002
    Finished3rd = 15003
    Finished4th = 15004
    Finished5th = 15005
    Finished6th = 15006
    Finished7th = 15007
    Finished8th = 15008
    Finished9th = 15009
    Finished10th = 15010
    Finished11th = 15011
    Finished12th = 15012
    Finished13th = 15013
    Finished14th = 15014
    Finished15th = 15015
    Finished16th = 15016

ETournamentTemplate = IntEnum('ETournamentTemplate', {
    'None': 0,
    'AutomatedWin3': 1,
    })

class ETourneyQueueDeadlineState(IntEnum):
    Normal = 0
    Missed = 1
    ExpiredOK = 2
    SeekingBye = 3
    EligibleForRefund = 4
    NA = -1
    ExpiringSoon = 101

class EUnderDraftResponse(IntEnum):
    eInternalError = 0
    eSuccess = 1
    eNoGold = 2
    eInvalidSlot = 3
    eNoBenchSpace = 4
    eNoTickets = 5
    eEventNotOwned = 6
    eInvalidReward = 7
    eHasBigReward = 8
    eNoGCConnection = 9
    eTooBusy = 10
    eCantRollBack = 11

EWeekendTourneyRichPresenceEvent = IntEnum('EWeekendTourneyRichPresenceEvent', {
    'None': 0,
    'StartedMatch': 1,
    'WonMatch': 2,
    'Eliminated': 3,
    })

class Fantasy_Roles(IntEnum):
    FANTASY_ROLE_UNDEFINED = 0
    FANTASY_ROLE_CORE = 1
    FANTASY_ROLE_SUPPORT = 2
    FANTASY_ROLE_OFFLANE = 3
    FANTASY_ROLE_MID = 4

class Fantasy_Selection_Mode(IntEnum):
    FANTASY_SELECTION_INVALID = 0
    FANTASY_SELECTION_LOCKED = 1
    FANTASY_SELECTION_SHUFFLE = 2
    FANTASY_SELECTION_FREE_PICK = 3
    FANTASY_SELECTION_ENDED = 4
    FANTASY_SELECTION_PRE_SEASON = 5
    FANTASY_SELECTION_PRE_DRAFT = 6
    FANTASY_SELECTION_DRAFTING = 7
    FANTASY_SELECTION_REGULAR_SEASON = 8
    FANTASY_SELECTION_CARD_BASED = 9

class Fantasy_Team_Slots(IntEnum):
    FANTASY_SLOT_NONE = 0
    FANTASY_SLOT_CORE = 1
    FANTASY_SLOT_SUPPORT = 2
    FANTASY_SLOT_ANY = 3
    FANTASY_SLOT_BENCH = 4

class GCConnectionStatus(IntEnum):
    HAVE_SESSION = 0
    GC_GOING_DOWN = 1
    NO_SESSION = 2
    NO_SESSION_IN_LOGON_QUEUE = 3
    NO_STEAM = 4
    SUSPENDED = 5
    STEAM_GOING_DOWN = 6

class GCProtoBufMsgSrc(IntEnum):
    Unspecified = 0
    FromSystem = 1
    FromSteamID = 2
    FromGC = 3
    ReplySystem = 4
    SpoofedSteamID = 5

class LobbyDotaPauseSetting(IntEnum):
    Unlimited = 0
    Limited = 1
    Disabled = 2

class LobbyDotaTVDelay(IntEnum):
    LobbyDotaTV_10 = 0
    LobbyDotaTV_120 = 1
    LobbyDotaTV_300 = 2
    LobbyDotaTV_900 = 3

class MatchLanguages(IntEnum):
    MATCH_LANGUAGE_INVALID = 0
    MATCH_LANGUAGE_ENGLISH = 1
    MATCH_LANGUAGE_RUSSIAN = 2
    MATCH_LANGUAGE_CHINESE = 3
    MATCH_LANGUAGE_KOREAN = 4
    MATCH_LANGUAGE_SPANISH = 5
    MATCH_LANGUAGE_PORTUGUESE = 6
    MATCH_LANGUAGE_ENGLISH2 = 7

class MatchType(IntEnum):
    MATCH_TYPE_CASUAL = 0
    MATCH_TYPE_COOP_BOTS = 1
    MATCH_TYPE_LEGACY_TEAM_RANKED = 2
    MATCH_TYPE_LEGACY_SOLO_QUEUE = 3
    MATCH_TYPE_COMPETITIVE = 4
    MATCH_TYPE_WEEKEND_TOURNEY = 5
    MATCH_TYPE_CASUAL_1V1 = 6
    MATCH_TYPE_EVENT = 7
    MATCH_TYPE_SEASONAL_RANKED = 8
    MATCH_TYPE_LOWPRI_DEPRECATED = 9
    MATCH_TYPE_STEAM_GROUP = 10
    MATCH_TYPE_MUTATION = 11
    MATCH_TYPE_COACHES_CHALLENGE = 12
    MATCH_TYPE_GAUNTLET = 13
    MATCH_TYPE_NEW_PLAYER_POOL = 14

class PartnerAccountType(IntEnum):
    PARTNER_NONE = 0
    PARTNER_PERFECT_WORLD = 1
    PARTNER_INVALID = 3

__all__ = [
    'DOTA_2013PassportSelectionIndices',
    'DOTA_BOT_MODE',
    'DOTA_CM_PICK',
    'DOTA_COMBATLOG_TYPES',
    'DOTA_GameMode',
    'DOTA_GameState',
    'DOTA_GC_TEAM',
    'DOTA_TournamentEvents',
    'DOTA_WatchReplayType',
    'DOTABotDifficulty',
    'DOTAChatChannelType_t',
    'DOTAConnectionState_t',
    'DOTAGameVersion',
    'DOTAJoinLobbyResult',
    'DOTALeaverStatus_t',
    'DOTALobbyReadyState',
    'DOTALobbyVisibility',
    'DOTALowPriorityBanType',
    'DOTAMatchVote',
    'DOTASelectionPriorityChoice',
    'DOTASelectionPriorityRules',
    'EBadgeType',
    'EBroadcastTimelineEvent',
    'EChatSpecialPrivileges',
    'ECustomGameInstallStatus',
    'ECustomGameWhitelistState',
    'EDACPlatform',
    'EDevEventRequestResult',
    'EDOTADraftTriviaAnswerResult',
    'EDOTAGCMsg',
    'EDOTAGCSessionNeed',
    'EDOTAGroupMergeResult',
    'EDOTAMMRBoostType',
    'EDOTAPlayerMMRType',
    'EDOTATriviaAnswerResult',
    'EDOTATriviaQuestionCategory',
    'EDPCFavoriteType',
    'EDPCPushNotification',
    'EEvent',
    'EEventActionScoreMode',
    'EFeaturedHeroDataType',
    'EFeaturedHeroTextField',
    'EGCBaseClientMsg',
    'EGCBaseMsg',
    'EGCBaseProtoObjectTypes',
    'EGCEconBaseMsg',
    'EGCItemMsg',
    'EGCMsgInitiateTradeResponse',
    'EGCMsgResponse',
    'EGCMsgUseItemResponse',
    'EGCPartnerRequestResponse',
    'EHeroRelicRarity',
    'EHighPriorityMMState',
    'EItemEditorReservationResult',
    'EItemPurgatoryResponse_Finalize',
    'EItemPurgatoryResponse_Refund',
    'ELaneSelection',
    'ELaneSelectionFlags',
    'ELaneType',
    'ELeagueAuditAction',
    'ELeagueBroadcastProvider',
    'ELeagueFlags',
    'ELeaguePhase',
    'ELeagueRegion',
    'ELeagueStatus',
    'ELeagueTier',
    'ELeagueTierCategory',
    'ELobbyMemberCoachRequestState',
    'EMatchBehaviorScoreVariance',
    'EMatchGroupServerStatus',
    'EMatchOutcome',
    'EMobilePaymentProvider',
    'EOverwatchConviction',
    'EOverwatchReportReason',
    'EPartyBeaconType',
    'EPartyMatchmakingFlags',
    'EPlayerChallengeHistoryType',
    'EProfileCardSlotType',
    'EPurchaseHeroRelicResult',
    'EReadyCheckRequestResult',
    'EReadyCheckStatus',
    'ESOMsg',
    'ESourceEngine',
    'ESpecialPingValue',
    'EStartFindingMatchResult',
    'ESupportEventRequestResult',
    'ETeamFanContentStatus',
    'ETeamInviteResult',
    'ETournamentEvent',
    'ETournamentGameState',
    'ETournamentNodeState',
    'ETournamentState',
    'ETournamentTeamState',
    'ETournamentTemplate',
    'ETourneyQueueDeadlineState',
    'EUnderDraftResponse',
    'EWeekendTourneyRichPresenceEvent',
    'Fantasy_Roles',
    'Fantasy_Selection_Mode',
    'Fantasy_Team_Slots',
    'GCConnectionStatus',
    'GCProtoBufMsgSrc',
    'LobbyDotaPauseSetting',
    'LobbyDotaTVDelay',
    'MatchLanguages',
    'MatchType',
    'PartnerAccountType',
    ]
