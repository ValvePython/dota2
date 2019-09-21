from enum import IntEnum

class DOTA_2013PassportSelectionIndices(IntEnum):
    PP13_SEL_EVENTPRED_41 = 85
    PP13_SEL_EVENTPRED_40 = 84
    PP13_SEL_EVENTPRED_43 = 87
    PP13_SEL_EVENTPRED_42 = 86
    PP13_SEL_TEAMCUP_PLAYER_LOCK = 43
    PP13_SEL_QUALPRED_EAST_1 = 26
    PP13_SEL_QUALPRED_EAST_0 = 25
    PP13_SEL_QUALPRED_EAST_3 = 28
    PP13_SEL_QUALPRED_EAST_2 = 27
    PP13_SEL_QUALPRED_EAST_5 = 30
    PP13_SEL_QUALPRED_EAST_4 = 29
    PP13_SEL_QUALPRED_EAST_7 = 32
    PP13_SEL_QUALPRED_EAST_6 = 31
    PP13_SEL_QUALPRED_EAST_9 = 34
    PP13_SEL_QUALPRED_EAST_8 = 33
    PP13_SEL_SOLO_0 = 88
    PP13_SEL_TEAMCUP_TEAM_LOCK = 42
    PP13_SEL_TEAMCUP_TEAM = 40
    PP13_SEL_QUALPRED_EAST_11 = 36
    PP13_SEL_QUALPRED_EAST_10 = 35
    PP13_SEL_QUALPRED_EAST_13 = 38
    PP13_SEL_QUALPRED_EAST_12 = 37
    PP13_SEL_QUALPRED_EAST_14 = 39
    PP13_SEL_QUALPRED_WEST_14 = 24
    PP13_SEL_QUALPRED_WEST_13 = 23
    PP13_SEL_QUALPRED_WEST_12 = 22
    PP13_SEL_QUALPRED_WEST_11 = 21
    PP13_SEL_QUALPRED_WEST_10 = 20
    PP13_SEL_QUALPRED_WEST_9 = 19
    PP13_SEL_SOLO_3 = 91
    PP13_SEL_SOLO_2 = 90
    PP13_SEL_SOLO_1 = 89
    PP13_SEL_QUALPRED_WEST_8 = 18
    PP13_SEL_SOLO_7 = 95
    PP13_SEL_SOLO_6 = 94
    PP13_SEL_SOLO_5 = 93
    PP13_SEL_SOLO_4 = 92
    PP13_SEL_QUALPRED_WEST_3 = 13
    PP13_SEL_QUALPRED_WEST_2 = 12
    PP13_SEL_EVENTPRED_18 = 62
    PP13_SEL_EVENTPRED_19 = 63
    PP13_SEL_EVENTPRED_12 = 56
    PP13_SEL_EVENTPRED_13 = 57
    PP13_SEL_EVENTPRED_10 = 54
    PP13_SEL_EVENTPRED_11 = 55
    PP13_SEL_EVENTPRED_16 = 60
    PP13_SEL_EVENTPRED_17 = 61
    PP13_SEL_EVENTPRED_14 = 58
    PP13_SEL_EVENTPRED_15 = 59
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
    PP13_SEL_QUALPRED_WEST_1 = 11
    PP13_SEL_QUALPRED_WEST_0 = 10
    PP13_SEL_QUALPRED_WEST_7 = 17
    PP13_SEL_QUALPRED_WEST_6 = 16
    PP13_SEL_QUALPRED_WEST_5 = 15
    PP13_SEL_QUALPRED_WEST_4 = 14
    PP13_SEL_TEAMCUP_PLAYER = 41
    PP13_SEL_EVENTPRED_27 = 71
    PP13_SEL_EVENTPRED_26 = 70
    PP13_SEL_EVENTPRED_25 = 69
    PP13_SEL_EVENTPRED_24 = 68
    PP13_SEL_EVENTPRED_23 = 67
    PP13_SEL_EVENTPRED_22 = 66
    PP13_SEL_EVENTPRED_21 = 65
    PP13_SEL_EVENTPRED_20 = 64
    PP13_SEL_EVENTPRED_29 = 73
    PP13_SEL_EVENTPRED_28 = 72
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
    PP13_SEL_ALLSTAR_PLAYER_9 = 9
    PP13_SEL_ALLSTAR_PLAYER_8 = 8
    PP13_SEL_ALLSTAR_PLAYER_3 = 3
    PP13_SEL_ALLSTAR_PLAYER_2 = 2
    PP13_SEL_ALLSTAR_PLAYER_1 = 1
    PP13_SEL_ALLSTAR_PLAYER_0 = 0
    PP13_SEL_ALLSTAR_PLAYER_7 = 7
    PP13_SEL_ALLSTAR_PLAYER_6 = 6
    PP13_SEL_ALLSTAR_PLAYER_5 = 5
    PP13_SEL_ALLSTAR_PLAYER_4 = 4

class DOTA_BOT_MODE(IntEnum):
    PUSH_TOWER_TOP = 8
    EVASIVE_MANEUVERS = 19
    NONE = 0
    PUSH_TOWER_BOT = 10
    DEFEND_TOWER_BOT = 13
    ROSHAN = 20
    FARM = 17
    RUNE = 7
    ROAM = 3
    DEFEND_ALLY = 18
    ASSEMBLE_WITH_HUMANS = 15
    RETREAT = 4
    TEAM_ROAM = 16
    DEFEND_TOWER_TOP = 11
    SECRET_SHOP = 5
    LANING = 1
    MINION = 25
    DEFEND_TOWER_MID = 12
    TUTORIAL_BOSS = 24
    ASSEMBLE = 14
    WARD = 22
    COMPANION = 23
    ITEM = 21
    ATTACK = 2
    SIDE_SHOP = 6
    PUSH_TOWER_MID = 9

class DOTA_CM_PICK(IntEnum):
    DOTA_CM_BAD_GUYS = 2
    DOTA_CM_GOOD_GUYS = 1
    DOTA_CM_RANDOM = 0

class DOTA_COMBATLOG_TYPES(IntEnum):
    DOTA_COMBATLOG_MODIFIER_STACK_EVENT = 19
    DOTA_COMBATLOG_XP = 10
    DOTA_COMBATLOG_BLOODSTONE_CHARGE = 38
    DOTA_COMBATLOG_HERO_LEVELUP = 25
    DOTA_COMBATLOG_UNIT_SUMMONED = 33
    DOTA_COMBATLOG_PICKUP_RUNE = 21
    DOTA_COMBATLOG_HEAL = 1
    DOTA_COMBATLOG_PLAYERSTATS = 14
    DOTA_COMBATLOG_INVALID = -1
    DOTA_COMBATLOG_REVEALED_INVISIBLE = 22
    DOTA_COMBATLOG_ITEM = 6
    DOTA_COMBATLOG_MODIFIER_ADD = 2
    DOTA_COMBATLOG_ABILITY_TRIGGER = 13
    DOTA_COMBATLOG_MANA_RESTORED = 24
    DOTA_COMBATLOG_KILLSTREAK = 16
    DOTA_COMBATLOG_SUCCESSFUL_SCAN = 36
    DOTA_COMBATLOG_MANA_DAMAGE = 31
    DOTA_COMBATLOG_FIRST_BLOOD = 18
    DOTA_COMBATLOG_MODIFIER_REMOVE = 3
    DOTA_COMBATLOG_INTERRUPT_CHANNEL = 28
    DOTA_COMBATLOG_PURCHASE = 11
    DOTA_COMBATLOG_ATTACK_EVADE = 34
    DOTA_COMBATLOG_ENDGAME_STATS = 27
    DOTA_COMBATLOG_MULTIKILL = 15
    DOTA_COMBATLOG_GOLD = 8
    DOTA_COMBATLOG_DEATH = 4
    DOTA_COMBATLOG_NEUTRAL_CAMP_STACK = 20
    DOTA_COMBATLOG_END_KILLSTREAK = 37
    DOTA_COMBATLOG_ALLIED_GOLD = 29
    DOTA_COMBATLOG_HERO_SAVED = 23
    DOTA_COMBATLOG_SPELL_ABSORB = 40
    DOTA_COMBATLOG_CRITICAL_DAMAGE = 39
    DOTA_COMBATLOG_TREE_CUT = 35
    DOTA_COMBATLOG_UNIT_TELEPORTED = 41
    DOTA_COMBATLOG_TEAM_BUILDING_KILL = 17
    DOTA_COMBATLOG_LOCATION = 7
    DOTA_COMBATLOG_GAME_STATE = 9
    DOTA_COMBATLOG_AEGIS_TAKEN = 30
    DOTA_COMBATLOG_ABILITY = 5
    DOTA_COMBATLOG_DAMAGE = 0
    DOTA_COMBATLOG_KILL_EATER_EVENT = 42
    DOTA_COMBATLOG_BOTTLE_HEAL_ALLY = 26
    DOTA_COMBATLOG_PHYSICAL_DAMAGE_PREVENTED = 32
    DOTA_COMBATLOG_BUYBACK = 12

class DOTA_GameMode(IntEnum):
    DOTA_GAMEMODE_COACHES_CHALLENGE = 25
    DOTA_GAMEMODE_CUSTOM = 15
    DOTA_GAMEMODE_RD = 3
    DOTA_GAMEMODE_TUTORIAL = 10
    DOTA_GAMEMODE_NONE = 0
    DOTA_GAMEMODE_LP = 12
    DOTA_GAMEMODE_EVENT = 19
    DOTA_GAMEMODE_HW = 7
    DOTA_GAMEMODE_BD = 17
    DOTA_GAMEMODE_ABILITY_DRAFT = 18
    DOTA_GAMEMODE_ARDM = 20
    DOTA_GAMEMODE_INTRO = 6
    DOTA_GAMEMODE_FH = 14
    DOTA_GAMEMODE_TURBO = 23
    DOTA_GAMEMODE_MO = 11
    DOTA_GAMEMODE_SD = 4
    DOTA_GAMEMODE_MUTATION = 24
    DOTA_GAMEMODE_AP = 1
    DOTA_GAMEMODE_CD = 16
    DOTA_GAMEMODE_POOL1 = 13
    DOTA_GAMEMODE_REVERSE_CM = 8
    DOTA_GAMEMODE_CM = 2
    DOTA_GAMEMODE_AR = 5
    DOTA_GAMEMODE_ALL_DRAFT = 22
    DOTA_GAMEMODE_XMAS = 9
    DOTA_GAMEMODE_1V1MID = 21

class DOTA_GameState(IntEnum):
    DOTA_GAMERULES_STATE_TEAM_SHOWCASE = 8
    DOTA_GAMERULES_STATE_CUSTOM_GAME_SETUP = 9
    DOTA_GAMERULES_STATE_WAIT_FOR_PLAYERS_TO_LOAD = 1
    DOTA_GAMERULES_STATE_GAME_IN_PROGRESS = 5
    DOTA_GAMERULES_STATE_POST_GAME = 6
    DOTA_GAMERULES_STATE_STRATEGY_TIME = 3
    DOTA_GAMERULES_STATE_WAIT_FOR_MAP_TO_LOAD = 10
    DOTA_GAMERULES_STATE_HERO_SELECTION = 2
    DOTA_GAMERULES_STATE_PRE_GAME = 4
    DOTA_GAMERULES_STATE_LAST = 11
    DOTA_GAMERULES_STATE_DISCONNECT = 7
    DOTA_GAMERULES_STATE_INIT = 0

class DOTA_GC_TEAM(IntEnum):
    BAD_GUYS = 1
    BROADCASTER = 2
    GOOD_GUYS = 0
    SPECTATOR = 3
    PLAYER_POOL = 4
    NOTEAM = 5

class DOTA_LobbyMemberXPBonus(IntEnum):
    DEFAULT = 0
    BATTLE_BOOSTER = 1
    RECRUITMENT = 4
    PARTY = 3
    SHARE_BONUS = 2
    PCBANG = 5

class DOTA_TournamentEvents(IntEnum):
    TE_AEGIS_DENY = 4
    TE_EARLY_ROSHAN = 10
    TE_BLACK_HOLE = 11
    TE_FIRST_BLOOD = 0
    TE_GODLIKE = 6
    TE_AEGIS_STOLEN = 5
    TE_GAME_END = 1
    TE_ECHOSLAM = 8
    TE_RAPIER = 9
    TE_MULTI_KILL = 2
    TE_HERO_DENY = 3
    TE_COURIER_KILL = 7

class DOTA_WatchReplayType(IntEnum):
    DOTA_WATCH_REPLAY_NORMAL = 0
    DOTA_WATCH_REPLAY_HIGHLIGHTS = 1

class DOTABotDifficulty(IntEnum):
    BOT_DIFFICULTY_MEDIUM = 2
    BOT_DIFFICULTY_PASSIVE = 0
    BOT_DIFFICULTY_HARD = 3
    BOT_DIFFICULTY_EXTRA3 = 8
    BOT_DIFFICULTY_EXTRA2 = 7
    BOT_DIFFICULTY_EXTRA1 = 6
    BOT_DIFFICULTY_UNFAIR = 4
    BOT_DIFFICULTY_INVALID = 5
    BOT_DIFFICULTY_EASY = 1

class DOTAChatChannelType_t(IntEnum):
    DOTAChannelType_Team = 4
    DOTAChannelType_CustomGame = 16
    DOTAChannelType_BattleCup = 19
    DOTAChannelType_Party = 2
    DOTAChannelType_Invalid = 10
    DOTAChannelType_Trivia = 22
    DOTAChannelType_Console = 8
    DOTAChannelType_Tab = 9
    DOTAChannelType_PostGame = 18
    DOTAChannelType_Regional = 0
    DOTAChannelType_Lobby = 3
    DOTAChannelType_Custom = 1
    DOTAChannelType_Private = 17
    DOTAChannelType_Guild = 5
    DOTAChannelType_Whisper = 7
    DOTAChannelType_Fantasy = 6
    DOTAChannelType_GameAllies = 12
    DOTAChannelType_HLTVSpectator = 20
    DOTAChannelType_Cafe = 15
    DOTAChannelType_GameAll = 11
    DOTAChannelType_GameSpectator = 13
    DOTAChannelType_GameEvents = 21

class DOTAConnectionState_t(IntEnum):
    DOTA_CONNECTION_STATE_NOT_YET_CONNECTED = 1
    DOTA_CONNECTION_STATE_DISCONNECTED = 3
    DOTA_CONNECTION_STATE_CONNECTED = 2
    DOTA_CONNECTION_STATE_UNKNOWN = 0
    DOTA_CONNECTION_STATE_FAILED = 6
    DOTA_CONNECTION_STATE_LOADING = 5
    DOTA_CONNECTION_STATE_ABANDONED = 4

class DOTAGameVersion(IntEnum):
    GAME_VERSION_STABLE = 1
    GAME_VERSION_CURRENT = 0

class DOTAJoinLobbyResult(IntEnum):
    DOTA_JOIN_RESULT_INCORRECT_VERSION = 6
    DOTA_JOIN_RESULT_BUSY = 13
    DOTA_JOIN_RESULT_CUSTOM_GAME_COOLDOWN = 12
    DOTA_JOIN_RESULT_SUCCESS = 0
    DOTA_JOIN_RESULT_GENERIC_ERROR = 5
    DOTA_JOIN_RESULT_TIMEOUT = 11
    DOTA_JOIN_RESULT_CUSTOM_GAME_INCORRECT_VERSION = 10
    DOTA_JOIN_RESULT_INVALID_LOBBY = 2
    DOTA_JOIN_RESULT_LOBBY_FULL = 9
    DOTA_JOIN_RESULT_ACCESS_DENIED = 4
    DOTA_JOIN_RESULT_IN_TEAM_PARTY = 7
    DOTA_JOIN_RESULT_NO_LOBBY_FOUND = 8
    DOTA_JOIN_RESULT_ALREADY_IN_GAME = 1
    DOTA_JOIN_RESULT_INCORRECT_PASSWORD = 3

class DOTALeaverStatus_t(IntEnum):
    DOTA_LEAVER_DECLINED = 8
    DOTA_LEAVER_FAILED_TO_READY_UP = 7
    DOTA_LEAVER_NEVER_CONNECTED_TOO_LONG = 6
    DOTA_LEAVER_ABANDONED = 3
    DOTA_LEAVER_NONE = 0
    DOTA_LEAVER_AFK = 4
    DOTA_LEAVER_DISCONNECTED_TOO_LONG = 2
    DOTA_LEAVER_NEVER_CONNECTED = 5
    DOTA_LEAVER_DISCONNECTED = 1

class DOTALobbyReadyState(IntEnum):
    UNDECLARED = 0
    ACCEPTED = 1
    DECLINED = 2

class DOTALobbyVisibility(IntEnum):
    Friends = 1
    Public = 0
    Unlisted = 2

class DOTALowPriorityBanType(IntEnum):
    DOTA_LOW_PRIORITY_BAN_SECONDARY_ABANDON = 2
    DOTA_LOW_PRIORITY_BAN_REPORTS = 1
    DOTA_LOW_PRIORITY_BAN_ABANDON = 0

class DOTAMatchVote(IntEnum):
    POSITIVE = 1
    NEGATIVE = 2
    INVALID = 0

class DOTASelectionPriorityChoice(IntEnum):
    Radiant = 3
    Dire = 4
    FirstPick = 1
    SecondPick = 2
    Invalid = 0

class DOTASelectionPriorityRules(IntEnum):
    Automatic = 1
    Manual = 0

class EBadgeType(IntEnum):
    TI8_AllEvent = 6
    TI8_Finals = 5
    TI7_Midweek = 1
    TI7_AllEvent = 3
    TI7_Finals = 2
    TI8_Midweek = 4

class EBroadcastTimelineEvent(IntEnum):
    BarracksDeath = 4
    AncientDeath = 5
    MatchStarted = 1
    HeroDeath = 7
    FirstBlood = 9
    RoshanDeath = 6
    TeamFight = 8
    GameStateChanged = 2
    TowerDeath = 3

ECoachTeammateRating = IntEnum('ECoachTeammateRating', {
    'Positive': 1,
    'None': 0,
    'Negative': 2,
    'Abusive': 3,
    })

class ECustomGameInstallStatus(IntEnum):
    Busy = 2
    CRCMismatch = 105
    Unknown = 0
    FailedCanceled = 107
    FailedInternalError = 102
    FailedGeneric = 101
    RequestedTimestampTooNew = 104
    RequestedTimestampTooOld = 103
    Ready = 1
    FailedSteam = 106

class ECustomGameWhitelistState(IntEnum):
    CUSTOM_GAME_WHITELIST_STATE_REJECTED = 2
    CUSTOM_GAME_WHITELIST_STATE_APPROVED = 1
    CUSTOM_GAME_WHITELIST_STATE_UNKNOWN = 0

class EDACPlatform(IntEnum):
    eDACPlatform_Android = 4
    eDACPlatform_iOS = 5
    eDACPlatform_Mac = 2
    eDACPlatform_Linux = 3
    eDACPlatform_PC = 1
    eDACPlatform_None = 0

class EDevEventRequestResult(IntEnum):
    Success = 0
    NotAllowed = 1
    SqlFailure = 3
    SDOLoadFailure = 6
    Timeout = 4
    LockFailure = 5
    InvalidEvent = 2

class EDOTAGCMsg(IntEnum):
    EMsgClientToGCRecyclePlayerCard = 8174
    EMsgGCToClientAutomatedTournamentStateChange = 8117
    EMsgSignOutReleaseEventPointHolds = 7597
    EMsgGCToGCEmoticonUnlockNoRollback = 7594
    EMsgSQLGCToGCGrantAllHeroProgress = 7520
    EMsgClientToGCPrivateChatDemote = 8090
    EMsgGCFantasyLivePlayerStats = 7308
    EMsgClientToGCRequestSocialFeedComments = 8305
    EMsgGCToGCSignoutAwardEventPoints = 7390
    EMsgGetRecentPlayTimeFriendsRequest = 8265
    EMsgUpgradeLeagueItemResponse = 7204
    EMsgClientToGCOpenPlayerCardPackResponse = 8169
    EMsgGCToGCReconcilePlusStatus = 8281
    EMsgGCToGCGetAccountPartnerResponse = 7461
    EMsgServerToGCHoldEventPoints = 7596
    EMsgGCFantasyScheduledMatchesResponse = 7440
    EMsgGCToGCReconcilePlusAutoGrantItems = 8284
    EMsgTeamFanfare = 7156
    EMsgGCFantasyTeamScoreResponse = 7313
    EMsgClientToGCSubmitCoachTeammateRating = 8341
    EMsgDOTALeagueAvailableLobbyNodesRequest = 7650
    EMsgGCPracticeLobbyKick = 7081
    EMsgClientToGCApplyGemCombiner = 7603
    EMsgGCCreateTeam = 7115
    EMsgGCFantasyTeamInfoResponse = 7306
    EMsgDOTALeagueNodeResponse = 7649
    EMsgClientToGCGetGiftPermissionsResponse = 8127
    EMsgGCQuickJoinCustomLobby = 7470
    EMsgClientToGCWageringRequest = 8099
    EMsgGCToClientQuestProgressUpdated = 8153
    EMsgGCToClientSocialMatchPostCommentResponse = 8026
    EMsgDevGrantEventActionResponse = 8322
    EMsgGCToGCGrantPlusPrepaidTime = 8278
    EMsgGCToGCGrantAutograph = 8315
    EMsgDOTAChatGetUserListResponse = 7404
    EMsgGCToClientManageFavoritesResponse = 7673
    EMsgClientToGCRequestLinaPlaysRemaining = 8146
    EMsgGCToClientTopLeagueMatchesResponse = 8061
    EMsgGCLeaveTeam = 7130
    EMsgUnanchorPhoneNumberResponse = 8225
    EMsgGCToGCCheckPlusStatus = 8282
    EMsgGCGetPlayerCardItemInfo = 8187
    EMsgAnchorPhoneNumberResponse = 8223
    EMsgGCBanStatusRequest = 7093
    EMsgDOTAFrostivusTimeElapsed = 7398
    EMsgGCToServerUpdateSteamBroadcasting = 8312
    EMsgClientToGCGetFavoriteAllStarPlayerRequest = 8357
    EMsgSQLGCToGCGrantBadgePoints = 7608
    EMsgGCJoinableCustomGameModesRequest = 7466
    EMsgGCFantasyTeamRosterAddDropRequest = 7361
    EMsgGCFantasyLeagueCreateResponse = 7337
    EMsgGCToGCRevokeEventOwnership = 7621
    EMsgGameAutographReward = 8244
    EMsgClientToGCSetAdditionalEquips = 7513
    EMsgGCToGCUpdateMatchManagementStats = 7414
    EMsgClientToGCClaimEventActionUsingItem = 8260
    EMsgGCToGCLeagueNodeGroupResponse = 7655
    EMsgClientToGCRequestContestVotes = 8347
    EMsgGCToGCGetServersForClients = 8045
    EMsgClientToGCTopFriendMatchesRequest = 8037
    EMsgAnchorPhoneNumberRequest = 8222
    EMsgGCTransferTeamAdmin = 7144
    EMsgGCToClientBattlePassRollupListResponse = 8206
    EMsgGCToGCCanInviteUserToTeamResponse = 7235
    EMsgClientToGCRequestSlarkGameResultResponse = 8228
    EMsgGCTeamData = 7121
    EMsgGCFantasyLeagueDraftStatusRequest = 7349
    EMsgClientToGCMarkNotificationListRead = 7542
    EMsgGCToGCLeagueNodeGroupRequest = 7654
    EMsgGCWatchDownloadedReplay = 7206
    EMsgSQLProcessTournamentGameOutcome = 7525
    EMsgGCFantasyLeagueInfo = 7299
    EMsgClientToGCRequestEventPointLogV2 = 8298
    EMsgClientToGCRequestArcanaVotesRemaining = 8130
    EMsgGCStopFindingMatch = 7036
    EMsgGCToClientTeamInfo = 8135
    EMsgGCPlayerHeroesFavoritesRemove = 7134
    EMsgGCToGCCheckLeaguePermission = 7189
    EMsgClientToGCGetAdditionalEquips = 7514
    EMsgClientToGCGetFavoritePlayers = 7676
    EMsgGCToClientRequestLaneSelection = 7623
    EMsgGCBroadcastNotification = 7056
    EMsgDOTAFriendRecruitsResponse = 7395
    EMsgGCOtherJoinedChannel = 7013
    EMsgGCGameMatchSignOutResponse = 7005
    EMsgClientToGCGetAllHeroProgressResponse = 7522
    EMsgServerToGCGetAdditionalEquipsResponse = 7517
    EMsgClientToGCTopLeagueMatchesRequest = 8036
    EMsgDOTAFantasyLeagueFindRequest = 7482
    EMsgPurchaseHeroRandomRelic = 8258
    EMsgSignOutConsumableUsage = 8317
    EMsgGCGameBotMatchSignOut = 7530
    EMsgGCFantasyLeagueInfoResponse = 7298
    EMsgGCJoinOpenGuildPartyRequest = 7269
    EMsgClientToGCPrivateChatKick = 8088
    EMsgGCStartFindingMatchResponse = 8055
    EMsgGCToGCGetTopMatchesResponse = 7661
    EMsgGCBotGameCreate = 7199
    EMsgGCToClientLeaguePredictionsResponse = 8107
    EMsgClientToGCGetQuestProgress = 8078
    EMsgGCToClientPlaytestStatus = 8200
    EMsgDOTALeagueNodeRequest = 7648
    EMsgClientToGCRequestSocialFeed = 8303
    EMsgGCJoinOpenGuildPartyResponse = 7270
    EMsgGCToGCLeagueResponse = 7653
    EMsgGCToClientEventStatusChanged = 7565
    EMsgGCFantasyTeamRosterAddDropResponse = 7362
    EMsgGCGetPlayerCardItemInfoResponse = 8188
    EMsgGCToClientWageringResponse = 8100
    EMsgGCAbandonCurrentGame = 7035
    EMsgClientToGCMyTeamInfoRequest = 8137
    EMsgGCLobbyListResponse = 8012
    EMsgClientToGCGetAllHeroOrder = 7606
    EMsgGCToServerPingRequest = 7416
    EMsgClientToGCRecycleHeroRelicResponse = 7620
    EMsgClientToGCGetAllHeroProgress = 7521
    EMsgGCToGCGetCustomGameTicketsResponse = 7574
    EMsgGCToGCSetEventMMPanicFlushTime = 7578
    EMsgGCGetHeroTimedStats = 8252
    EMsgGCRequestOfferingsResponse = 7425
    EMsgGCToGCUnlockEventPointSpending = 7622
    EMsgGCRewardTutorialPrizes = 7289
    EMsgGCEditFantasyTeamRequest = 7302
    EMsgGCToClientPrivateChatInfoResponse = 8093
    EMsgGCApplyTeamToPracticeLobby = 7142
    EMsgServerToGCCloseCompendiumInGamePredictionVoting = 8167
    EMsgGameserverCrashReport = 7579
    EMsgGCGetHeroStandingsResponse = 7275
    EMsgGCGuildmatePracticeLobbyListRequest = 7281
    EMsgGCToClientCavernCrawlMapUpdated = 8329
    EMsgGCLobbyList = 8011
    EMsgServerToGCMatchDetailsRequest = 8069
    EMsgGCGuildSetAccountRoleResponse = 7225
    EMsgGCEventGameCreate = 7443
    EMsgGCWatchGameResponse = 7092
    EMsgGCGeneralResponse = 7001
    EMsgGCFantasyLeagueDraftPlayerRequest = 7351
    EMsgGCToClientRequestLaneSelectionResponse = 7624
    EMsgClientToGCGetTrophyListResponse = 7528
    EMsgGCLastHitChallengeHighScorePost = 7290
    EMsgGCToGCGetServerForClient = 7523
    EMsgGCToServerIngameEventData_OraclePA = 7553
    EMsgClientToGCUpdatePartyBeacon = 7669
    EMsgGCReportsRemainingResponse = 7077
    EMsgClientToGCSpectatorLobbyListResponse = 8162
    EMsgClientToGCSocialFeedPostMessageRequest = 8050
    EMsgGCToClientMatchGroupsVersion = 8075
    EMsgGCTeamInvite_GCImmediateResponseToInviter = 7123
    EMsgDOTAFriendRecruitsRequest = 7394
    EMsgGCFantasyLeagueDraftPlayerResponse = 7352
    EMsgGCCancelWatchGame = 7097
    EMsgGCToClientPartySearchInvites = 7680
    EMsgGCToClientPartySearchInvite = 7668
    EMsgDOTAWeekendTourneySchedule = 7465
    EMsgGCToGCReconcilePlusAutoGrantItemsUnreliable = 8310
    EMsgPresentedClientTerminateDlg = 7363
    EMsgGCToGCGetUserChatInfoResponse = 7219
    EMsgGCClearPracticeLobbyTeam = 8008
    EMsgClientToGCRequestPlayerRecentAccomplishments = 8332
    EMsgGCFlipLobbyTeams = 7320
    EMsgClientToGCSetPartyBuilderOptions = 8198
    EMsgGCToGCSignoutSpendRankWager = 8229
    EMsgClientToGCGetUnderlordsCDKeyRequest = 8351
    EMsgClientToGCRequestEventTipsSummary = 8300
    EMsgServerToGCSignoutAwardAdditionalDrops = 7563
    EMsgGCPracticeLobbySetCoach = 7346
    EMsgClientToGCEventGoalsResponse = 8104
    EMsgPrivateMetadataKeyRequest = 8279
    EMsgGCPracticeLobbyList = 7042
    EMsgCastMatchVote = 7152
    EMsgGCToGCLeagueNodeRequest = 7656
    EMsgClientToGCJoinPlaytestResponse = 8202
    EMsgGCTransferTeamAdminResponse = 8132
    EMsgClientToGCSetProfileCardSlots = 7538
    EMsgGCNotificationsMarkReadRequest = 7435
    EMsgClientToGCCustomGamePlayerCountRequest = 8014
    EMsgGCToGCLeagueMatchStarted = 7645
    EMsgGCJoinableCustomGameModesResponse = 7467
    EMsgGCToServerMatchDetailsResponse = 8070
    EMsgClientToGCPlayerStatsRequest = 8006
    EMsgClientToGCVoteForArcanaResponse = 8129
    EMsgHeroGlobalDataResponse = 8275
    EMsgGCIsProQuery = 8207
    EMsgGCToClientProfileCardStatsUpdated = 8040
    EMsgGCFantasyLeagueInfoRequest = 7297
    EMsgGCFantasyPlayerStandingsResponse = 7319
    EMsgDOTAGetEventPoints = 7387
    EMsgGCSetMatchHistoryAccess = 7200
    EMsgGCProTeamListResponse = 7169
    EMsgClientToGCVoteForArcana = 8128
    EMsgGCToClientWageringUpdate = 8154
    EMsgGCBalancedShuffleLobby = 7188
    EMsgClientToGCQuickStatsResponse = 8239
    EMsgGCFantasyLeagueCreateInfoRequest = 7331
    EMsgClientToGCRecordContestVote = 8313
    EMsgGCNotInGuildData = 7251
    EMsgClientToGCMVPVoteTimeoutResponse = 8350
    EMsgClientToGCSetPlayerCardRosterRequest = 8180
    EMsgDOTAGetPeriodicResource = 8211
    EMsgGCMatchmakingStatsRequest = 7197
    EMsgSQLDelayedGrantLeagueDrop = 7496
    EMsgGCToGCGetAccountMatchStatus = 7609
    EMsgSignOutCommunityGoalProgress = 8150
    EMsgServerToGCMatchStateHistory = 8255
    EMsgClientToGCCreateSpectatorLobbyResponse = 8160
    EMsgGCCompendiumDataResponse = 7407
    EMsgGCPlayerInfo = 7455
    EMsgGCItemEditorReserveItemDef = 7285
    EMsgGCPracticeLobbyKickFromTeam = 8047
    EMsgGCTeamMemberProfileRequest = 7205
    EMsgPrivateMetadataKeyResponse = 8280
    EMsgGCToGCGetUserRankResponse = 7237
    EMsgGCGameBotMatchSignOutPermissionRequest = 7531
    EMsgGCFantasyLeagueFriendJoinListRequest = 7340
    EMsgGCSetMatchHistoryAccessResponse = 7201
    EMsgClientToGCGetProfileCardStatsResponse = 8035
    EMsgGCChatMessage = 7273
    EMsgGCToGCProcessReportSuccess = 7325
    EMsgClientToGCCreatePlayerCardPack = 8176
    EMsgClientToGCWeekendTourneyLeave = 8120
    EMsgGCFantasyLeagueCreateInfoResponse = 7332
    EMsgGCKickTeamMemberResponse = 7129
    EMsgGCToClientRemoveFilteredPlayerResponse = 7665
    EMsgGCToClientEmoticonData = 7504
    EMsgGCGCToRelayConnectresponse = 7090
    EMsgClientToGCMatchesMinimalRequest = 8063
    EMsgGCToServerRealtimeStatsStartStop = 8042
    EMsgDevGrantEventAction = 8321
    EMsgGCFantasyTeamScoreRequest = 7312
    EMsgClientToGCPlayerCardSpecificPurchaseRequest = 7627
    EMsgPurchaseItemWithEventPoints = 8248
    EMsgGCFantasyLeagueEditInvitesRequest = 7344
    EMsgGCToGCGetCompendiumFanfare = 7595
    EMsgClientToGCMergePartyResponse = 8032
    EMsgGCToGCGrantTournamentItem = 7372
    EMsgGCPracticeLobbySetDetails = 7046
    EMsgGCToClientVerifyFavoritePlayersResponse = 7679
    EMsgGCToGCGetAccountMatchStatusResponse = 7610
    EMsgClientToGCGetQuestProgressResponse = 8079
    EMsgClientToGCCavernCrawlUseItemOnPathResponse = 8294
    EMsgSuccessfulHero = 8273
    EMsgDestroyLobbyRequest = 8246
    EMsgServerToGCLockCharmTrading = 8004
    EMsgDOTAFantasyLeagueFindResponse = 7483
    EMsgClientToGCSetSpectatorLobbyDetails = 8157
    EMsgGCHallOfFameResponse = 7173
    EMsgGCPracticeLobbySetTeamSlot = 7047
    EMsgGCGuildUpdateDetailsRequest = 7232
    EMsgDOTAGetPlayerMatchHistory = 7408
    EMsgServerToGCCavernCrawlIsHeroActive = 7625
    EMsgGCPartyMemberSetCoach = 7343
    EMsgClientToGCH264Unsupported = 8076
    EMsgClientToGCSetPartyOpen = 8029
    EMsgClientToGCHasPlayerVotedForMVP = 8111
    EMsgGCLastHitChallengeHighScoreResponse = 7292
    EMsgClientToGCSelectCompendiumInGamePrediction = 8170
    EMsgSQLGrantTrophyToAccount = 7526
    EMsgGCRequestPlayerResourcesResponse = 7069
    EMsgSubmitTriviaQuestionAnswer = 8216
    EMsgGetRecentPlayTimeFriendsResponse = 8266
    EMsgGCProTeamListRequest = 7168
    EMsgGCToGCSetCompendiumSelection = 7478
    EMsgGCRequestPlayerResources = 7068
    EMsgGCKickedFromMatchmakingQueue = 7071
    EMsgGCToClientFindTopSourceTVGamesResponse = 8010
    EMsgGCDev_GrantWarKill = 8001
    EMsgGCClientIgnoredUser = 7335
    EMsgGCItemEditorReserveItemDefResponse = 7286
    EMsgGCToGCGetAccountFlagsResponse = 8059
    EMsgGCToGCGrantEventPointAction = 7472
    EMsgDOTALiveLeagueGameUpdate = 7402
    EMsgGCToGCProcessPlayerReportForTarget = 7324
    EMsgGCGameMatchSignOut = 7004
    EMsgGCToGCReplayMonitorValidateReplay = 7569
    EMsgClientToGCRecyclePlayerCardResponse = 8175
    EMsgClientToGCGiveTipResponse = 8219
    EMsgGCToGCAddUserToPostGameChat = 8110
    EMsgGCPracticeLobbyJoinBroadcastChannel = 7149
    EMsgGCToGCFantasySetMatchLeague = 7557
    EMsgSpectatorLobbyGameDetails = 8163
    EMsgClientToGCCavernCrawlUseItemOnRoom = 8291
    EMsgGCFriendPracticeLobbyListRequest = 7111
    EMsgGCRequestLeaguePrizePool = 7258
    EMsgGCPlayerFailedToConnect = 7088
    EMsgGCGuildCancelInviteRequest = 7230
    EMsgClientToGCRequestActiveBeaconParties = 7670
    EMsgClientToGCRequestPlayerCoachMatch = 8345
    EMsgClientToGCCreateHeroStatue = 7547
    EMsgGCToGCSendAccountsEventPoints = 7583
    EMsgServerToGCGetProfileCardResponse = 7537
    EMsgSQLGrantLeagueMatchToTicketHolders = 7592
    EMsgDOTAGetWeekendTourneySchedule = 7464
    EMsgDetailedGameStats = 8353
    EMsgGCToGCGetAccountLevelResponse = 7459
    EMsgGCToClientPlayerBeaconState = 7666
    EMsgGCLobbyUpdateBroadcastChannelInfo = 7367
    EMsgClientToGCAddTI6TreeProgress = 8156
    EMsgGCJoinChatChannel = 7009
    EMsgClientToGCGetUnderlordsCDKeyResponse = 8352
    EMsgClientToGCSetSpectatorLobbyDetailsResponse = 8158
    EMsgGCRequestMatchesResponse = 7065
    EMsgClientToGCGetFavoriteAllStarPlayerResponse = 8358
    EMsgGCEditFantasyTeamResponse = 7303
    EMsgGCTeamInvite_GCRequestToInvitee = 7124
    EMsgGCSetMapLocationState = 7207
    EMsgGCToGCGrantEventPointActionMsg = 7488
    EMsgGCPracticeLobbyJoinResponse = 7113
    EMsgGCMakeOffering = 7423
    EMsgClientToGCJoinPartyFromBeacon = 7674
    EMsgGCLastHitChallengeHighScoreRequest = 7291
    EMsgGCToClientTipNotification = 8226
    EMsgGCPlayerHeroesFavoritesAdd = 7133
    EMsgServerGetEventPoints = 7473
    EMsgAllStarStats = 8356
    EMsgGCEditTeamDetails = 7166
    EMsgGCRewardDiretidePrizes = 7176
    EMsgGCFantasyMessagesRequest = 7437
    EMsgClientToGCRequestPlayerHeroRecentAccomplishments = 8334
    EMsgClientToGCRequestPlusWeeklyChallengeResultResponse = 8277
    EMsgLobbyPlayerPlusSubscriptionData = 8254
    EMsgClientToGCSelectCompendiumInGamePredictionResponse = 8171
    EMsgGCToGCSubtractEventPointsFromUser = 8240
    EMsgGCFantasyLeagueMatchupsRequest = 7353
    EMsgClientToGCTransferSeasonalMMRResponse = 8194
    EMsgGCToClientMergeGroupInviteReply = 8031
    EMsgGCFantasyPlayerScoreRequest = 7316
    EMsgServerToGCRequestPlayerRecentAccomplishmentsResponse = 8331
    EMsgGCToGCGetAccountPartner = 7460
    EMsgGCTeamInvite_GCResponseToInvitee = 7127
    EMsgClientToGCCancelPartyInvites = 7589
    EMsgPurchaseHeroRandomRelicResponse = 8259
    EMsgClientToGCGetFilteredPlayers = 7662
    EMsgGCToGCMasterReloadAccount = 7590
    EMsgGCTeamInvite_GCResponseToInviter = 7126
    EMsgGCToGCUpdateIngameEventDataBroadcast = 7552
    EMsgClientToGCRequestArcanaVotesRemainingResponse = 8131
    EMsgClientToGCSetPlayerCardRosterResponse = 8181
    EMsgGCFantasyLeaveLeagueRequest = 7490
    EMsgGCFantasyMessagesResponse = 7438
    EMsgGCDiretidePrizesRewardedResponse = 7177
    EMsgGCToGCUpdateOpenGuildPartyResponse = 7262
    EMsgGCConsumeFantasyTicket = 7486
    EMsgGCToGCCheckLeaguePermissionResponse = 7190
    EMsgUnanchorPhoneNumberRequest = 8224
    EMsgClientToGCRequestPlayerRecentAccomplishmentsResponse = 8333
    EMsgClientToGCSocialFeedPostCommentRequest = 8016
    EMsgSignOutBotInfo = 7532
    EMsgGCSpectateFriendGame = 7073
    EMsgClientToGCRecycleHeroRelic = 7619
    EMsgClientToGCGiveTip = 8218
    EMsgSubmitTriviaQuestionAnswerResponse = 8217
    EMsgGCSuggestTeamMatchmaking = 7132
    EMsgGCGetHeroStatsHistoryResponse = 8083
    EMsgClientToGCTransferSeasonalMMRRequest = 8193
    EMsgClientToGCVerifyFavoritePlayers = 7678
    EMsgGCRequestChatChannelListResponse = 7061
    EMsgDOTALeagueInfoListAdminsReponse = 7634
    EMsgGCPracticeLobbyToggleBroadcastChannelCameramanStatus = 7505
    EMsgGCToGCMatchCompleted = 7186
    EMsgGCSubmitLobbyMVPVoteResponse = 8145
    EMsgServerToGCRequestStatus = 7026
    EMsgGCFantasyPlayerScoreDetailsRequest = 7499
    EMsgGCToClientTopFriendMatchesResponse = 8062
    EMsgGCFantasyRemoveOwner = 7448
    EMsgClientToGCSetAdditionalEquipsResponse = 7593
    EMsgGCToClientBattlePassRollupListRequest = 8205
    EMsgGameserverCrashReportResponse = 7580
    EMsgServerToGCVictoryPredictions = 7540
    EMsgDOTALeagueInfoListAdminsRequest = 7633
    EMsgDOTARedeemItemResponse = 7519
    EMsgServerToGCCavernCrawlIsHeroActiveResponse = 7626
    EMsgClientToGCRequestPlayerCoachMatchesResponse = 8338
    EMsgServerGCUpdateSpectatorCount = 7497
    EMsgGCToGCSignoutSpendWager = 8141
    EMsgGCGuildmatePracticeLobbyListResponse = 7282
    EMsgGCToGCCustomGamePlayed = 7576
    EMsgGCHalloweenHighScoreResponse = 7179
    EMsgGCToGCGetLiveLeagueMatches = 7631
    EMsgGCNotificationsResponse = 7428
    EMsgClientToGCGetProfileTicketsResponse = 8074
    EMsgGCToGCGetLeagueAdmin = 7255
    EMsgGCToClientGetFilteredPlayersResponse = 7663
    EMsgGCItemEditorReleaseReservation = 7287
    EMsgGCToGCDestroyOpenGuildPartyResponse = 7264
    EMsgGCRequestLeaguePrizePoolResponse = 7259
    EMsgGCPerfectWorldUserLookupResponse = 7445
    EMsgClientToGCManageFavorites = 7672
    EMsgRefreshPartnerAccountLink = 7216
    EMsgPartyReadyCheckRequest = 8262
    EMsgGCToGCGrantPlusHeroMatchResults = 8251
    EMsgClientToGCRequestSteamDatagramTicket = 8189
    EMsgGCReportCountsResponse = 7083
    EMsgGCFantasyTeamTradesResponse = 7369
    EMsgClientToGCVerifyIntegrity = 8359
    EMsgGCRequestOfferings = 7424
    EMsgClientToGCWeekendTourneyOptsResponse = 8119
    EMsgGCLeaveTeamResponse = 7131
    EMsgGCGetHeroStatsHistory = 8082
    EMsgServerToGCRequestPlayerRecentAccomplishments = 8330
    EMsgClientToGCSpectatorLobbyList = 8161
    EMsgGCFantasyTeamRosterResponse = 7358
    EMsgServerGetEventPointsResponse = 7474
    EMsgGCGetHeroStandings = 7274
    EMsgGCToGCCanInviteUserToTeam = 7234
    EMsgClientToGCRequestLinaGameResultResponse = 8149
    EMsgGCToGCGetCustomGameTickets = 7573
    EMsgGCToClientJoinPartyFromBeaconResponse = 7675
    EMsgGCToGCGetLeagueAdminResponse = 7256
    EMsgGCHasItemResponse = 7485
    EMsgGCRequestSaveGames = 7084
    EMsgDOTAChatGetMemberCount = 8048
    EMsgGCToGCGetPlayerPennantCounts = 7379
    EMsgGCToGCGetAccountLevel = 7458
    EMsgGCGameMatchSignOutPermissionResponse = 7382
    EMsgGCToClientSocialFeedPostCommentResponse = 8017
    EMsgClientToGCRequestPlayerCoachMatchResponse = 8346
    EMsgClientToGCGetProfileCardResponse = 7535
    EMsgDOTAGetEventPointsResponse = 7388
    EMsgClientToGCGetPlayerCardRosterResponse = 8179
    EMsgGCGuildCreateResponse = 7223
    EMsgGCGCToLANServerRelayConnect = 7549
    EMsgDevGrantEventPoints = 8319
    EMsgClientToGCCavernCrawlClaimRoomResponse = 8290
    EMsgGCTeamInvite_InviterToGC = 7122
    EMsgDestroyLobbyResponse = 8247
    EMsgGCGuildInviteData = 7254
    EMsgServerToGCPostMatchTip = 8097
    EMsgGCPCBangTimedRewardMessage = 7366
    EMsgClientToGCLatestConductScorecardRequest = 8095
    EMsgDOTAClaimEventActionResponse = 8210
    EMsgGCRequestSaveGamesServer = 7085
    EMsgGCToGCLeagueMatchStartedResponse = 7647
    EMsgGCDOTABase = 7000
    EMsgClientToGCCustomGamesFriendsPlayedRequest = 8018
    EMsgClientToGCTeammateStatsResponse = 8125
    EMsgHeroGlobalDataAllHeroes = 8302
    EMsgGCToClientGetFavoritePlayersResponse = 7677
    EMsgDOTAPeriodicResourceUpdated = 8213
    EMsgClientToGCMVPVoteTimeout = 8349
    EMsgGCFantasyPlayerScoreDetailsResponse = 7500
    EMsgClientToGCRequestSteamDatagramTicketResponse = 8190
    EMsgProfileUpdateResponse = 8271
    EMsgCustomGameClientFinishedLoading = 8053
    EMsgGCFantasyTeamCreateResponse = 7339
    EMsgGCFantasyLeagueInviteInfoRequest = 7333
    EMsgGCPracticeLobbyLeave = 7040
    EMsgClientToGCCavernCrawlUseItemOnPath = 8293
    EMsgClientToGCRequestEventTipsSummaryResponse = 8301
    EMsgDOTAGetPlayerMatchHistoryResponse = 7409
    EMsgClientToGCRequestContestVotesResponse = 8348
    EMsgProfileResponse = 8269
    EMsgRetrieveMatchVote = 7154
    EMsgGCPlayerInfoSubmit = 7456
    EMsgGCGetRecentMatches = 7027
    EMsgDOTAGetPeriodicResourceResponse = 8212
    EMsgGCToGCPublicChatCommunicationBan = 8195
    EMsgGCInitialQuestionnaireResponse = 7049
    EMsgGCToGCEnsureAccountInParty = 8071
    EMsgGCKickTeamMember = 7128
    EMsgGCWatchGame = 7091
    EMsgGCNotificationsRequest = 7427
    EMsgResponseTeamFanfare = 7157
    EMsgGCHallOfFameRequest = 7172
    EMsgClientToGCVoteForMVP = 8113
    EMsgGCToGCSignoutAwardAdditionalDrops = 7564
    EMsgCustomGameListenServerStartedLoading = 8052
    EMsgGCItemEditorReleaseReservationResponse = 7288
    EMsgGCPartySetOpenGuildResponse = 7267
    EMsgGCFantasyPlayerStandingsRequest = 7318
    EMsgGCToServerPingResponse = 7417
    EMsgClientToGCHasPlayerVotedForMVPResponse = 8112
    EMsgClientToGCGetGiftPermissions = 8126
    EMsgGCToGCCheckOwnsEntireEmoticonRangeResponse = 7612
    EMsgLobbyBattleCupVictory = 8186
    EMsgClientToGCRequestSlarkGameResult = 8227
    EMsgClientToGCRequestPlayerHeroRecentAccomplishmentsResponse = 8335
    EMsgGCPlayerReports = 7075
    EMsgClientToGCDOTACreateStaticRecipe = 7604
    EMsgGCMatchmakingStatsResponse = 7198
    EMsgGCToGCLeaguePredictionsUpdate = 8108
    EMsgPurchaseHeroRelicResponse = 8257
    EMsgGCToGCGrantAutographResponse = 8316
    EMsgGCToGCEnsureAccountInPartyResponse = 8072
    EMsgGCToGCUpdateTI4HeroQuest = 7480
    EMsgClientToGCCavernCrawlGetClaimedRoomCount = 8308
    EMsgGCFantasyMatch = 7310
    EMsgGCPracticeLobbyCreate = 7038
    EMsgGCTopCustomGamesList = 8024
    EMsgGCToClientClaimEventActionUsingItemCompleted = 8328
    EMsgClientToGCClaimEventActionUsingItemResponse = 8261
    EMsgGCBanStatusResponse = 7094
    EMsgClientToGCLeaguePredictions = 8106
    EMsgGCFantasyPlayerScoreResponse = 7317
    EMsgGCLeaverDetectedResponse = 7087
    EMsgGCQuickJoinCustomLobbyResponse = 7471
    EMsgClientToGCRequestEventPointLogResponseV2 = 8299
    EMsgClientToGCCreateSpectatorLobby = 8159
    EMsgGCProcessFantasyScheduledEvent = 7373
    EMsgGC_TournamentItemEvent = 7150
    EMsgGCFantasyLeagueDraftStatus = 7350
    EMsgServerToGCCloseCompendiumInGamePredictionVotingResponse = 8183
    EMsgGCToGCGetCompendiumSelectionsResponse = 7493
    EMsgGCToGCUpdateProfileCards = 7533
    EMsgGCToClientCustomGamesFriendsPlayedResponse = 8019
    EMsgGCPracticeLobbyJoin = 7044
    EMsgGCFantasyTeamInfoRequestByOwnerAccountID = 7305
    EMsgGCToClientAllStarVotesSubmit = 8236
    EMsgGCPlayerInfoSubmitResponse = 7457
    EMsgServerToGCGetProfileCard = 7536
    EMsgGCResetMapLocationsResponse = 7210
    EMsgClientToGCFriendsPlayedCustomGameRequest = 8020
    EMsgGCToClientCavernCrawlMapPathCompleted = 8288
    EMsgServerToGCCompendiumInGamePredictionResultsResponse = 8185
    EMsgGCToGCGetProfileBadgePointsResponse = 8066
    EMsgClientToGCGetProfileCardStats = 8034
    EMsgGCRequestMatches = 7064
    EMsgGCCreateFantasyTeamResponse = 7301
    EMsgClientToGCSetPartyBuilderOptionsResponse = 8199
    EMsgClientToGCSocialMatchDetailsRequest = 8027
    EMsgGC_GameServerUploadSaveGame = 7158
    EMsgGCPracticeLobbyResponse = 7055
    EMsgGCReportsRemainingRequest = 7076
    EMsgGCFantasyPlayerHisoricalStatsResponse = 7365
    EMsgGCToClientCoachTeammateRatingsChanged = 8343
    EMsgGCToClientRecordContestVoteResponse = 8314
    EMsgGCToClientNewNotificationAdded = 7543
    EMsgGCToGCRealtimeStatsTerseRequest = 7658
    EMsgPurchaseHeroRelic = 8256
    EMsgConsumeEventSupportGrantItemResponse = 8327
    EMsgSQLSetIsLeagueAdmin = 7630
    EMsgGCToGCGetCompendiumSelections = 7492
    EMsgClientToGCGetTrophyList = 7527
    EMsgGCToGCGetProfileBadgePoints = 8065
    EMsgGCCreateTeamResponse = 7116
    EMsgGCToGCGetFavoriteTeamResponse = 8231
    EMsgGCGuildEditLogoResponse = 7280
    EMsgGCToGCGrantEventOwnership = 7582
    EMsgServerGrantSurveyPermission = 7475
    EMsgGCHasItemDefsResponse = 7567
    EMsgGCToClientBattlePassRollupResponse = 8192
    EMsgGCToGCMatchmakingRemoveParty = 7411
    EMsgGCToClientMergePartyResponseReply = 8033
    EMsgGCLeagueAdminList = 7434
    EMsgSelectionPriorityChoiceRequest = 8241
    EMsgGCToGCUpdateAccountPublicChatBan = 8196
    EMsgSignOutWagerStats = 8060
    EMsgServerToGCRealtimeStats = 8041
    EMsgGCToClientCustomGamePlayerCountResponse = 8015
    EMsgProfileUpdate = 8270
    EMsgClientToGCSetFavoriteAllStarPlayer = 8354
    EMsgClientToGCEmoticonDataRequest = 7503
    EMsgGC_GameServerGetLoadGame = 7160
    EMsgServerToGCPostMatchTipResponse = 8098
    EMsgGCGuildInviteAccountResponse = 7229
    EMsgGCToGCSetNewNotifications = 7430
    EMsgClientToGCRequestH264Support = 8077
    EMsgGCToGCReportKillSummaries = 7555
    EMsgDOTAChatGetMemberCountResponse = 8049
    EMsgGC_TournamentItemEventResponse = 7151
    EMsgDOTAFriendRecruitInviteAcceptDecline = 7396
    EMsgGCToGCReconcilePlusStatusUnreliable = 8285
    EMsgGCToGCUpdatePlayerPredictions = 7561
    EMsgRetrieveMatchVoteResponse = 7155
    EMsgGCToGCGetLiveLeagueMatchesResponse = 7632
    EMsgGCToClientLobbyMVPAwarded = 8152
    EMsgGCPartyLeaderWatchGamePrompt = 7397
    EMsgGCFantasyTeamStandingsResponse = 7315
    EMsgGCToGCMatchmakingMatchFound = 7413
    EMsgGCStorePromoPagesRequest = 7182
    EMsgDOTAChatChannelMemberUpdate = 7383
    EMsgGCJoinableCustomLobbiesResponse = 7469
    EMsgGCToClientSteamDatagramTicket = 7581
    EMsgGCNotifyAccountFlagsChange = 7326
    EMsgClientToGCPrivateChatInfoRequest = 8092
    EMsgClientToGCCavernCrawlClaimRoom = 8289
    EMsgStartTriviaSession = 8220
    EMsgClientToGCRequestLinaGameResult = 8148
    EMsgGCItemEditorReservationsResponse = 7284
    EMsgGCSubmitPlayerReport = 7078
    EMsgGCToClientSocialFeedPostMessageResponse = 8051
    EMsgGCToClientPlayerStatsResponse = 8007
    EMsgGCToGCCheckOwnsEntireEmoticonRange = 7611
    EMsgClientToGCRerollPlayerChallenge = 7584
    EMsgClientToGCWeekendTourneyLeaveResponse = 8121
    EMsgGCMatchHistoryList = 7017
    EMsgClientsRejoinChatChannels = 7217
    EMsgGCConnectedPlayers = 7034
    EMsgClientToGCPrivateChatInvite = 8084
    EMsgSignOutCommunicationSummary = 7545
    EMsgGCToGCCreateWeekendTourneyResponse = 7507
    EMsgGCToGCLeagueRequest = 7652
    EMsgGCReadyUpStatus = 7170
    EMsgGCToGCUpdateAssassinMinigame = 7556
    EMsgGCRerollPlayerChallengeResponse = 7586
    EMsgDOTAChatGetUserList = 7403
    EMsgGCCompendiumSetSelectionResponse = 7453
    EMsgGCFantasyLeagueInviteInfoResponse = 7334
    EMsgGCToGCGetUserRank = 7236
    EMsgGCToGCSignoutSpendWagerToken = 8215
    EMsgGCCompendiumDataChanged = 7481
    EMsgGCFantasyTeamTradesRequest = 7368
    EMsgServerToGCGetIngameEventData = 7551
    EMsgClientToGCPingData = 8068
    EMsgGCToClientHeroStatueCreateResult = 7548
    EMsgGCToClientChatRegionsEnabled = 8067
    EMsgGCHasItemDefsQuery = 7566
    EMsgGCGuildData = 7227
    EMsgClientToGCMergePartyInvite = 8030
    EMsgGCToGCCreateWeekendTourneyRequest = 7506
    EMsgGCPlayerInfoRequest = 7454
    EMsgGCChatReportPublicSpam = 8197
    EMsgServerToGCSuspiciousActivity = 7544
    EMsgGCFantasyLeagueEditInvitesResponse = 7345
    EMsgGCToGCLeagueNodeResponse = 7657
    EMsgGCFantasyLeagueCreateRequest = 7336
    EMsgGCToGCValidateTeam = 7241
    EMsgGCPassportDataRequest = 7248
    EMsgGCPassportDataResponse = 7249
    EMsgGCReadyUp = 7070
    EMsgGCJoinableCustomLobbiesRequest = 7468
    EMsgGCStartFindingMatch = 7033
    EMsgClientToGCGetProfileCard = 7534
    EMsgGCToGCUpgradeTwitchViewerItems = 7375
    EMsgGCCompendiumDataRequest = 7406
    EMsgConsumeEventSupportGrantItem = 8326
    EMsgGCToGCRealtimeStatsTerseResponse = 7659
    EMsgGCLeaverDetected = 7072
    EMsgClientToGCGetAdditionalEquipsResponse = 7515
    EMsgClientToGCQuickStatsRequest = 8238
    EMsgGCGuildUpdateDetailsResponse = 7233
    EMsgGCRequestSaveGamesResponse = 7086
    EMsgGCToClientFriendsPlayedCustomGameResponse = 8021
    EMsgClientToGCGetTicketCodesRequest = 8339
    EMsgGCToGCGetUserChatInfo = 7218
    EMsgGCFantasyTeamRosterSwapRequest = 7355
    EMsgGCToGCUpdateMatchmakingStats = 7415
    EMsgGCCustomGameCreate = 7321
    EMsgGCToGCLeagueMatchCompleted = 7646
    EMsgActivatePlusFreeTrialResponse = 8287
    EMsgClientToGCCreatePlayerCardPackResponse = 8177
    EMsgServerToGCReportKillSummaries = 7554
    EMsgDOTARedeemItem = 7518
    EMsgDevResetEventStateResponse = 8324
    EMsgClientToGCPublishUserStat = 8140
    EMsgGCSetMapLocationStateResponse = 7208
    EMsgGCToGCCompendiumInGamePredictionResults = 8243
    EMsgGCMatchDetailsResponse = 7096
    EMsgGCFantasyRemoveOwnerResponse = 7449
    EMsgGCToClientTrophyAwarded = 7529
    EMsgGameAutographRewardResponse = 8245
    EMsgGCLeaveChatChannel = 7272
    EMsgGC_GameServerGetLoadGameResult = 7161
    EMsgGCSetProfilePrivacyResponse = 7328
    EMsgGCToGCEmoticonUnlock = 7501
    EMsgGCPerfectWorldUserLookupRequest = 7444
    EMsgClientToGCGetPlayerCardRosterRequest = 8178
    EMsgClientToGCWeekendTourneyOpts = 8118
    EMsgGCToGCGetPlayerPennantCountsResponse = 7380
    EMsgGCHallOfFame = 7171
    EMsgGCGuildEditLogoRequest = 7279
    EMsgClientToGCMatchesMinimalResponse = 8064
    EMsgGCToClientAllStarVotesRequest = 8233
    EMsgDOTASendFriendRecruits = 7393
    EMsgLobbyPlaytestDetails = 8203
    EMsgGCToClientProfileCardUpdated = 7539
    EMsgGCToClientTeamsInfo = 8136
    EMsgClientToGCCavernCrawlRequestMapState = 8295
    EMsgClientToGCCavernCrawlGetClaimedRoomCountResponse = 8309
    EMsgClientToGCRequestLinaPlaysRemainingResponse = 8147
    EMsgClientToGCSuspiciousActivity = 8109
    EMsgProfileRequest = 8268
    EMsgGCGuildSetAccountRoleRequest = 7224
    EMsgGC_GameServerSaveGameResult = 7159
    EMsgGCReportCountsRequest = 7082
    EMsgGCCreateFantasyLeagueRequest = 7293
    EMsgGCToGCMatchmakingRemoveAllParties = 7412
    EMsgGCHalloweenHighScoreRequest = 7178
    EMsgGCGuildCreateRequest = 7222
    EMsgDOTALeagueAvailableLobbyNodes = 7651
    EMsgGCToGCGetFavoriteTeam = 8230
    EMsgGCToClientTournamentItemDrop = 7495
    EMsgGCToGCLeaveAllChatChannels = 7220
    EMsgGCToClientAllStarVotesReply = 8234
    EMsgGCToGCCheckPlusStatusResponse = 8283
    EMsgServerToGCCompendiumInGamePredictionResults = 8166
    EMsgGCFantasyLeagueEditInfoResponse = 7348
    EMsgClientToGCSetFavoriteAllStarPlayerResponse = 8355
    EMsgServerGrantSurveyPermissionResponse = 7476
    EMsgGCRequestBatchPlayerResources = 7450
    EMsgDevGrantEventPointsResponse = 8320
    EMsgGCMatchDetailsRequest = 7095
    EMsgStartTriviaSessionResponse = 8221
    EMsgGCFantasyFinalPlayerStats = 7309
    EMsgClientToGCPrivateChatPromote = 8089
    EMsgGCToClientLobbyMVPNotifyRecipient = 8151
    EMsgClientEconNotification_Job = 7114
    EMsgGCPracticeLobbyLaunch = 7041
    EMsgGCFantasyTeamStandingsRequest = 7314
    EMsgGCToServerConsoleCommand = 7418
    EMsgGCFantasyTeamTradeCancelResponse = 7371
    EMsgGCGuildOpenPartyRefresh = 7268
    EMsgGCHasItemQuery = 7484
    EMsgLobbyEventPoints = 7572
    EMsgGCToClientRequestActiveBeaconPartiesResponse = 7671
    EMsgGCPracticeLobbyCloseBroadcastChannel = 8054
    EMsgGCToGCGetEventOwnership = 8115
    EMsgGCPopup = 7102
    EMsgGCOtherLeftChannel = 7014
    EMsgSignOutXPCoins = 8080
    EMsgGCFantasyTeamInfoRequestByFantasyLeagueID = 7304
    EMsgClientToGCJoinPlaytest = 8201
    EMsgServerToGCAddBroadcastTimelineEvent = 8311
    EMsgServerToGCRerollPlayerChallenge = 7585
    EMsgDOTASetFavoriteTeam = 8204
    EMsgGCRequestBatchPlayerResourcesResponse = 7451
    EMsgClientToGCCavernCrawlUseItemOnRoomResponse = 8292
    EMsgGCJoinChatChannelResponse = 7010
    EMsgGCToClientSocialMatchDetailsResponse = 8028
    EMsgGCConsumeFantasyTicketFailure = 7487
    EMsgDOTAAwardEventPoints = 7384
    EMsgGCToGCGetLiveMatchAffiliates = 7376
    EMsgGCRequestGuildData = 7226
    EMsgGCGuildUpdateMessage = 7265
    EMsgGCToClientPrivateChatResponse = 8091
    EMsgPurchaseItemWithEventPointsResponse = 8249
    EMsgClientToGCRequestPlayerCoachMatches = 8337
    EMsgGCGuildInviteAccountRequest = 7228
    EMsgGCFantasyTeamRosterSwapResponse = 7356
    EMsgGCToClientCommendNotification = 8267
    EMsgClientToGCWeekendTourneyGetPlayerStats = 8172
    EMsgGCToGCDestroyOpenGuildPartyRequest = 7263
    EMsgClientToGCVoteForMVPResponse = 8114
    EMsgSignOutDraftInfo = 7502
    EMsgGCGameMatchSignOutPermissionRequest = 7381
    EMsgClientToGCVoteForLeagueGameMVP = 8344
    EMsgServerToGCMatchConnectionStats = 7494
    EMsgDOTAClaimEventAction = 8209
    EMsgGCFantasyTeamInfo = 7307
    EMsgGCGetHeroTimedStatsResponse = 8253
    EMsgSignOutUpdatePlayerChallenge = 7587
    EMsgGCToGCGetTopMatchesRequest = 7660
    EMsgGCClientSuspended = 7342
    EMsgGCEditTeamDetailsResponse = 7167
    EMsgClientProvideSurveyResult = 7477
    EMsgClientToGCLatestConductScorecard = 8096
    EMsgGCToGCUpdatePlayerPennantCounts = 7378
    EMsgGCGuildCancelInviteResponse = 7231
    EMsgClientToGCRequestSocialFeedCommentsResponse = 8306
    EMsgGCToGCGetLiveMatchAffiliatesResponse = 7377
    EMsgClientToGCWeekendTourneyGetPlayerStatsResponse = 8173
    EMsgHeroGlobalDataRequest = 8274
    EMsgGCFantasyTeamTradeCancelRequest = 7370
    EMsgSignOutEventActionGrants = 8336
    EMsgGCToGCValidateTeamResponse = 7242
    EMsgGCResetMapLocations = 7209
    EMsgPartyReadyCheckAcknowledge = 8264
    EMsgGCPartySetOpenGuildRequest = 7266
    EMsgClientToGCRemoveFilteredPlayer = 7664
    EMsgLobbyEventGameDetails = 8318
    EMsgGCStorePromoPagesResponse = 7183
    EMsgGCRequestChatChannelList = 7060
    EMsgClientToGCFindTopSourceTVGames = 8009
    EMsgClientToGCGetAllHeroOrderResponse = 7607
    EMsgGCFriendPracticeLobbyListResponse = 7112
    EMsgSignOutTips = 8297
    EMsgGCSubmitLobbyMVPVote = 8144
    EMsgClientToGCPlayerCardSpecificPurchaseResponse = 7628
    EMsgCastMatchVoteResponse = 7153
    EMsgPartyReadyCheckResponse = 8263
    EMsgGCToGCUpdateOpenGuildPartyRequest = 7261
    EMsgGCToServerPredictionResult = 7562
    EMsgGCtoServerTensorflowInstance = 7629
    EMsgClientToGCGetProfileTickets = 8073
    EMsgServerToGCRequestStatus_Response = 7546
    EMsgSelectionPriorityChoiceResponse = 8242
    EMsgGCSpectateFriendGameResponse = 7074
    EMsgGCToGCGetServerForClientResponse = 7524
    EMsgClientToGCRequestPlusWeeklyChallengeResult = 8276
    EMsgGCDOTAClearNotifySuccessfulReport = 7104
    EMsgGCFantasyLeaveLeagueResponse = 7491
    EMsgServerToGCMatchPlayerItemPurchaseHistory = 8250
    EMsgGCToGCSendUpdateLeagues = 7452
    EMsgGCToGCModifyNotification = 7429
    EMsgGCPlayerStatsMatchSignOut = 8013
    EMsgClientToGCRequestSocialFeedResponse = 8304
    EMsgGCPracticeLobbyListResponse = 7043
    EMsgGCToGCGetAccountFlags = 8058
    EMsgDevResetEventState = 8323
    EMsgServerToGCGetAdditionalEquips = 7516
    EMsgClientToGCSetPartyLeader = 7588
    EMsgGCSubmitPlayerReportResponse = 7079
    EMsgClientToGCCavernCrawlRequestMapStateResponse = 8296
    EMsgGCToClientPartyBeaconUpdate = 7667
    EMsgClientToGCTeammateStatsRequest = 8124
    EMsgGCToGCUpdateTeamStats = 7240
    EMsgGCCompendiumSetSelection = 7405
    EMsgGCTeamInvite_InviteeResponseToGC = 7125
    EMsgGCIsProResponse = 8208
    EMsgUpgradeLeagueItem = 7203
    EMsgSQLGCToGCGrantAccountFlag = 8057
    EMsgGCToGCGetEventOwnershipResponse = 8116
    EMsgGCGenerateDiretidePrizeListResponse = 7180
    EMsgGCFantasyLeagueMatchupsResponse = 7354
    EMsgGCFantasyTeamRosterRequest = 7357
    EMsgGCCreateFantasyTeamRequest = 7300
    EMsgGCGCToRelayConnect = 7089
    EMsgGCItemEditorReservationsRequest = 7283
    EMsgClientToGCEventGoalsRequest = 8103
    EMsgGCToGCReconcileEventOwnership = 8325
    EMsgGCFantasyLeagueEditInfoRequest = 7347
    EMsgGCToClientAllStarVotesSubmitReply = 8237
    EMsgGCToClientBattlePassRollupRequest = 8191
    EMsgGCFantasyScheduledMatchesRequest = 7439
    EMsgGCFantasyLeagueFriendJoinListResponse = 7341
    EMsgGCToGCUpdateAccountChatBan = 7221
    EMsgGCToGCGrantEventPointsToUser = 7577
    EMsgGCToGCGetServersForClientsResponse = 8046
    EMsgGCGenerateDiretidePrizeList = 7174
    EMsgGCFantasyMessageAdd = 7436
    EMsgClientToGCSocialMatchPostCommentRequest = 8025
    EMsgGCRecentMatchesResponse = 7028
    EMsgGCFantasyPlayerHisoricalStatsRequest = 7364
    EMsgServerToGCSpendWager = 8214
    EMsgSignOutEventGameData = 8232
    EMsgGCToGCMatchmakingAddParty = 7410
    EMsgClientToGCGetTicketCodesResponse = 8340
    EMsgGCFantasyTeamCreateRequest = 7338
    EMsgGCToGCProcessMatchLeaver = 7426
    EMsgGCToClientArcanaVotesUpdate = 8155
    EMsgGCToGCChatNewUserSession = 7598
    EMsgGCToClientMatchSignedOut = 8081
    EMsgActivatePlusFreeTrialRequest = 8286
    EMsgClientToGCSubmitCoachTeammateRatingResponse = 8342
    EMsgClientToGCOpenPlayerCardPack = 8168
    EMsgGCLiveScoreboardUpdate = 7057
    EMsgClientToGCTrackDialogResult = 7489
    EMsgGCCreateFantasyLeagueResponse = 7294
    EMsgGCSetProfilePrivacy = 7327
    EMsgClientToGCDOTACreateStaticRecipeResponse = 7605

class EDOTAGCSessionNeed(IntEnum):
    UserInUIWasConnectedIdle = 106
    Unknown = 0
    UserTutorials = 105
    UserInLocalGame = 102
    GameServerIdle = 202
    UserNoSessionNeeded = 100
    UserInUINeverConnectedIdle = 107
    GameServerOnline = 200
    GameServerLocalUpload = 204
    GameServerLocal = 201
    GameServerRelay = 203
    UserInOnlineGame = 101
    UserInUIWasConnected = 103
    UserInUINeverConnected = 104

class EDOTAGroupMergeResult(IntEnum):
    OTHER_GROUP_NOT_OPEN = 7
    OK = 0
    FAILED_GENERIC = 1
    NOT_LEADER = 2
    NO_SUCH_GROUP = 6
    TOO_MANY_COACHES = 4
    NOT_INVITED = 9
    TOO_MANY_PLAYERS = 3
    ENGINE_MISMATCH = 5
    ALREADY_INVITED = 8

EDOTAPlayerMMRType = IntEnum('EDOTAPlayerMMRType', {
    'GeneralSeasonalRanked': 6,
    '1v1Competitive_UNUSED': 5,
    'Competitive_Core': 8,
    'GeneralCompetitive2019': 3,
    'SoloCompetitive2019': 4,
    'Invalid': 0,
    'Competitive_Support': 9,
    'SoloSeasonalRanked': 7,
    'GeneralHidden': 1,
    })

class EDOTATriviaAnswerResult(IntEnum):
    TriviaDisabled = 5
    Success = 0
    InvalidQuestion = 1
    InvalidAnswer = 2
    QuestionLocked = 3
    AlreadyAnswered = 4

class EDOTATriviaQuestionCategory(IntEnum):
    HeroMovementSpeed = 3
    AbilityManaCost = 9
    HeroStats = 5
    AbilityIcon = 0
    AbilitySound = 7
    HeroAttackSound = 10
    HeroAttributes = 2
    ItemPrice = 6
    TalentTree = 4
    ItemLore = 13
    ItemComponents = 12
    AbilityName = 11
    AbilityCooldown = 1
    InvokerSpells = 8
    ItemPassives = 14

class EDPCFavoriteType(IntEnum):
    FAVORITE_TYPE_ALL = 0
    FAVORITE_TYPE_TEAM = 2
    FAVORITE_TYPE_PLAYER = 1
    FAVORITE_TYPE_LEAGUE = 3

class EDPCPushNotification(IntEnum):
    DPC_PUSH_NOTIFICATION_LEAGUE_RESULT = 20
    DPC_PUSH_NOTIFICATION_PLAYER_LEFT_TEAM = 10
    DPC_PUSH_NOTIFICATION_FANTASY_PLAYER_CLEARED = 40
    DPC_PUSH_NOTIFICATION_FANTASY_FINAL_RESULTS = 42
    DPC_PUSH_NOTIFICATION_PREDICTION_RESULT = 31
    DPC_PUSH_NOTIFICATION_PREDICTION_MATCHES_AVAILABLE = 30
    DPC_PUSH_NOTIFICATION_MATCH_STARTING = 1
    DPC_PUSH_NOTIFICATION_FANTASY_DAILY_SUMMARY = 41
    DPC_PUSH_NOTIFICATION_PLAYER_JOINED_TEAM = 11

class EEvent(IntEnum):
    EVENT_ID_FROSTIVUS = 12
    EVENT_ID_COUNT = 26
    EVENT_ID_SPRING_FESTIVAL = 2
    EVENT_ID_NEXON_PC_BANG = 5
    EVENT_ID_FROSTIVUS_2018 = 23
    EVENT_ID_FROSTIVUS_2017 = 21
    EVENT_ID_FROSTIVUS_2013 = 3
    EVENT_ID_PLUS_SUBSCRIPTION = 19
    EVENT_ID_WINTER_MAJOR_2016 = 13
    EVENT_ID_WINTER_MAJOR_2017 = 16
    EVENT_ID_NONE = 0
    EVENT_ID_SINGLES_DAY_2017 = 20
    EVENT_ID_DIRETIDE = 1
    EVENT_ID_INTERNATIONAL_2016 = 14
    EVENT_ID_INTERNATIONAL_2017 = 18
    EVENT_ID_INTERNATIONAL_2015 = 8
    EVENT_ID_PWRD_DAC_2015 = 6
    EVENT_ID_NEW_BLOOM_2015 = 7
    EVENT_ID_COMPENDIUM_2014 = 4
    EVENT_ID_NEW_BLOOM_2017 = 17
    EVENT_ID_FALL_MAJOR_2015 = 9
    EVENT_ID_FALL_MAJOR_2016 = 15
    EVENT_ID_INTERNATIONAL_2018 = 22
    EVENT_ID_INTERNATIONAL_2019 = 25
    EVENT_ID_ORACLE_PA = 10
    EVENT_ID_NEW_BLOOM_2019 = 24
    EVENT_ID_NEW_BLOOM_2015_PREBEAST = 11

class EFeaturedHeroDataType(IntEnum):
    ExpireTimestamp = 4
    HeroWins = 5
    HeroLosses = 6
    StartTimestamp = 3
    HypeString = 2
    ContainerItemDef = 8
    SaleDiscount = 7
    HeroID = 0
    ItemDef = 1

class EFeaturedHeroTextField(IntEnum):
    ItemSetDescription = 2
    SaleDiscount = 10
    PopularItem = 8
    SaleItem = 9
    NewHero = 0
    ItemDescription = 3
    HeroWinLoss = 5
    Hype = 4
    FeaturedItem = 7
    FrequentlyPlayedHero = 6
    NewItem = 1
    Container = 11

class EGCBaseClientMsg(IntEnum):
    EMsgGCClientHello = 4006
    EMsgGCToClientPollConvarRequest = 3003
    EMsgGCToClientPollConvarResponse = 3004
    EMsgGCServerHello = 4007
    EMsgGCCompressedMsgToClient = 3005
    EMsgGCPingRequest = 3001
    EMsgGCPingResponse = 3002
    EMsgGCClientWelcome = 4004
    EMsgGCClientConnectionStatus = 4009
    EMsgGCServerWelcome = 4005
    EMsgGCServerConnectionStatus = 4010
    EMsgGCCompressedMsgToClient_Legacy = 523
    EMsgGCToClientRequestDropped = 3006

class EGCBaseMsg(IntEnum):
    EMsgGCLeaveParty = 4505
    EMsgGCConVarUpdated = 4003
    EMsgGCToClientPollFileResponse = 4515
    EMsgGCToClientPollFileRequest = 4514
    EMsgGCInviteToLobby = 4512
    EMsgGCInvitationCreated = 4502
    EMsgGCToGCPerformManualOp = 4516
    EMsgGCServerAvailable = 4506
    EMsgGCReplicateConVars = 4002
    EMsgGCLANServerAvailable = 4511
    EMsgGCLobbyInviteResponse = 4513
    EMsgGCKickFromParty = 4504
    EMsgGCPartyInviteResponse = 4503
    EMsgGCToGCReloadServerRegionSettings = 4518
    EMsgGCGameServerInfo = 4508
    EMsgGCToGCPerformManualOpCompleted = 4517
    EMsgGCError = 4509
    EMsgGCSystemMessage = 4001
    EMsgGCClientConnectToServer = 4507
    EMsgGCInviteToParty = 4501

class EGCBaseProtoObjectTypes(IntEnum):
    EProtoObjectPartyInvite = 1001
    EProtoObjectLobbyInvite = 1002

class EGCEconBaseMsg(IntEnum):
    EMsgGCGenericResult = 2579

class EGCItemMsg(IntEnum):
    EMsgGCAddSocketToItemResponse_DEPRECATED = 1018
    EMsgGCBase = 1000
    EMsgGCAddItemToSocketResponse = 1089
    EMsgGCPresets_SetItemPosition = 1064
    EMsgGCServerBrowser_BlacklistServer = 1602
    EMsgGCPresets_SelectPresetForClass = 1063
    EMsgGCToGCStoreProcessSettlementResponse = 2589
    EMsgGCCustomizeItemTextureResponse = 1024
    EMsgGCToGCDevRevokeUserItems = 2583
    EMsgGCToGCGetInfuxIntervalStats = 2606
    EMsgGCGoldenWrenchBroadcast = 1011
    EMsgGCTrading_StartSession = 1503
    EMsgGCItemPurgatory_FinalizePurchase = 2531
    EMsgGCToGCPingResponse = 2540
    EMsgGCToGCApplyLocalizationDiff = 2550
    EMsgGCToGCBannedWordListUpdated = 2515
    EMsgGCAddItemToSocket_DEPRECATED = 1014
    EMsgClientToGCNameItem = 1006
    EMsgGCMOTDRequest = 1012
    EMsgGCRemoveUniqueCraftIndexResponse = 1056
    EMsgGCUseItemRequest = 1025
    EMsgGCRequestStoreSalesDataUpToDateResponse = 2538
    EMsgGCResetStrangeGemCountResponse = 1095
    EMsgGCRequestCrateItems = 1092
    EMsgGCToGCItemConsumptionRollback = 2564
    EMsgGCToGCBroadcastMessageFromSub = 2598
    EMsgGCMOTDRequestResponse = 1013
    EMsgGCToGCGetUserSessionServer = 2541
    EMsgClientToGCRemoveItemName = 1110
    EMsgGCServerUseItemRequest = 1103
    EMsgGCPartnerBalanceResponse = 2558
    EMsgClientToGCNameItemResponse = 1068
    EMsgGCGetAccountSubscriptionItemResponse = 2596
    EMsgGCSetItemStyle_DEPRECATED = 1039
    EMsgGCDev_UnlockAllItemStylesResponse = 2004
    EMsgGCToGCSelfPing = 2605
    EMsgGCStorePurchaseInit = 2510
    EMsgGCFulfillDynamicRecipeComponentResponse = 1083
    EMsgGCAddGiftItem = 1104
    EMsgGCDev_NewItemRequestResponse = 2002
    EMsgGCTrading_InitiateTradeRequestResponse = 1514
    EMsgGCAdjustItemEquippedState = 1059
    EMsgSQLGCToGCGrantBackpackSlots = 2580
    EMsgGCAddSocket = 1087
    EMsgGCToClientCurrencyPricePoints = 2599
    EMsgGCToGCCanUseDropRateBonus = 2547
    EMsgGCRemoveItemGifterAccountId = 1107
    EMsgClientToGCRemoveItemAttributeResponse = 1112
    EMsgGCToGCRefreshSOCache = 2549
    EMsgGCRemoveItemGiftMessage = 1105
    EMsgGCClientRequestMarketDataResponse = 1085
    EMsgGCAddSocketResponse = 1090
    EMsgClientToGCWrapAndDeliverGiftResponse = 2566
    EMsgGCSaxxyBroadcast = 1057
    EMsgGC_IncrementKillCountResponse = 1075
    EMsgGCToGCFlushSteamInventoryCache = 2601
    EMsgGCRemoveItemPaint = 1031
    EMsgGCRemoveUniqueCraftIndex = 1055
    EMsgGCRemoveItemName = 1030
    EMsgGCGetAccountSubscriptionItem = 2595
    EMsgGCRemoveCustomTextureResponse = 1052
    EMsgClientToGCEquipItems = 2569
    EMsgGCDev_UnlockAllItemStylesRequest = 2003
    EMsgClientToGCLookupAccountName = 2581
    EMsgGCToGCUpdateSQLKeyValue = 2518
    EMsgGCRemoveCustomTexture = 1051
    EMsgGCToGCBroadcastConsoleCommand = 2521
    EMsgGCGiftedItems = 1027
    EMsgClientToGCCreateStaticRecipeResponse = 2585
    EMsgGCDelete = 1004
    EMsgGC_RevolvingLootList_DEPRECATED = 1042
    EMsgGCItemPurgatory_RefundPurchase = 2533
    EMsgGCApplyAutograph = 2523
    EMsgGCToGCConsoleOutput = 2590
    EMsgGCApplyConsumableEffects = 1069
    EMsgGCPresets_SelectPresetForClassReply = 1067
    EMsgGCToGCGetUserServerMembersResponse = 2544
    EMsgGCRemoveSocketItemResponse_DEPRECATED = 1022
    EMsgGCToGCAddSubscriptionTime = 2600
    EMsgGCItemAcknowledged = 1062
    EMsgGCTrading_InitiateTradeRequest = 1501
    EMsgGCToGCStoreProcessCDKeyTransactionResponse = 2587
    EMsgClientToGCUnlockCrate = 2574
    EMsgGCAddItemToSocketResponse_DEPRECATED = 1015
    EMsgGCUnwrapGiftRequest = 1037
    EMsgGCToGCGetInfuxIntervalStatsResponse = 2607
    EMsgClientToGCEquipItemsResponse = 2570
    EMsgGCBackpackSortFinished = 1058
    EMsgGCToGCGetUserPCBangNoResponse = 2546
    EMsgGCRequestCrateEscalationLevelResponse = 2603
    EMsgGCPaintItem = 1009
    EMsgGCCustomizeItemTexture = 1023
    EMsgGCToGCApplyLocalizationDiffResponse = 2551
    EMsgGCRemoveItemGiftMessageResponse = 1106
    EMsgClientToGCRemoveItemDescription = 1111
    EMsgGCApplyStrangePart = 1073
    EMsgGCNameEggEssenceResponse = 1079
    EMsgGCServerRentalsBase = 1700
    EMsgGCFulfillDynamicRecipeComponent = 1082
    EMsgGCToGCPingRequest = 2539
    EMsgGCRemoveMakersMark = 1053
    EMsgGCToClientStoreTransactionCompleted = 2568
    EMsgGCSetItemPositions_RateLimited = 1096
    EMsgGCToGCPlayerStrangeCountAdjustments = 2535
    EMsgGCVerifyCacheSubscription = 1005
    EMsgGCToGCGetUserServerMembers = 2543
    EMsgGCShowItemsPickedUp = 1071
    EMsgGCTradingBase = 1500
    EMsgClientToGCUnlockItemStyle = 2571
    EMsgSQLAddDropRateBonus = 2548
    EMsgGCStorePurchaseCancel = 2506
    EMsgGCToGCClientServerVersionsUpdated = 2593
    EMsgGCServerBrowser_FavoriteServer = 1601
    EMsgGCToGCStoreProcessSettlement = 2588
    EMsgClientToGCUnlockItemStyleResponse = 2572
    EMsgGCExtractGemsResponse = 1094
    EMsgGCClientRequestMarketData = 1084
    EMsgGCToGCDirtySDOCache = 2516
    EMsgGCStorePurchaseCancelResponse = 2507
    EMsgGCTrading_SessionClosed = 1509
    EMsgGCResetStrangeGemCount = 1091
    EMsgGCRedeemCode = 2562
    EMsgGCToGCUpdateSubscriptionItems = 2604
    EMsgGCStatueCraft = 2561
    EMsgGCToClientItemAges = 2591
    EMsgGCRequestStoreSalesDataResponse = 2537
    EMsgGCClientVersionUpdated = 2528
    EMsgGCItemPurgatory_FinalizePurchaseResponse = 2532
    EMsgGCStorePurchaseFinalizeResponse = 2505
    EMsgClientToGCSetItemStyleResponse = 2578
    EMsgGCNameBaseItemResponse = 1020
    EMsgGCPartnerRechargeRedirectURLResponse = 2560
    EMsgGCToGCWebAPIAccountChanged = 2524
    EMsgGCSortItems = 1041
    EMsgGCRequestCrateItemsResponse = 1093
    EMsgGCToGCGetUserSessionServerResponse = 2542
    EMsgGCToGCStoreProcessCDKeyTransaction = 2586
    EMsgClientToGCWrapAndDeliverGift = 2565
    EMsgClientToGCLookupAccountNameResponse = 2582
    EMsgGCRequestCrateEscalationLevel = 2602
    EMsgGCTrading_InitiateTradeResponse = 1502
    EMsgGCStorePurchaseInitResponse = 2511
    EMsgGCSetItemPosition = 1001
    EMsgClientToGCUnlockCrateResponse = 2575
    EMsgGCRemoveItemGifterAccountIdResponse = 1108
    EMsgGCServerVersionUpdated = 2522
    EMsgGCNameBaseItem = 1019
    EMsgGCDev_NewItemRequest = 2001
    EMsgGCStorePurchaseFinalize = 2504
    EMsgGCAddSocketToItem_DEPRECATED = 1017
    EMsgGCToGCGrantAccountRolledItems = 2554
    EMsgGCToGCGetUserPCBangNo = 2545
    EMsgGCUseItemResponse = 1026
    EMsgGCUpdateItemSchema = 1049
    EMsgGCToGCDirtyMultipleSDOCache = 2517
    EMsgGCToGCGrantSelfMadeItemToAccount = 2555
    EMsgGCAddItemToSocket = 1088
    EMsgClientToGCRemoveItemGifterAttributes = 1109
    EMsgGCToGCInternalTestMsg = 2592
    EMsgGCUsedClaimCodeItem = 1040
    EMsgGCApplyPennantUpgrade = 1076
    EMsgGCApplyEggEssence = 1078
    EMsgGCUnwrapGiftResponse = 1038
    EMsgGCRedeemCodeResponse = 2563
    EMsgGCItemPurgatory_RefundPurchaseResponse = 2534
    EMsgClientToGCCreateStaticRecipe = 2584
    EMsgGCPaintItemResponse = 1010
    EMsgGCCollectItem = 1061
    EMsgGCClientDisplayNotification = 1072
    EMsgGCToGCCheckAccountTradeStatusResponse = 2553
    EMsgGCAddSocketToBaseItem_DEPRECATED = 1016
    EMsgGCToGCCheckAccountTradeStatus = 2552
    EMsgGCPartnerBalanceRequest = 2557
    EMsgGCRemoveSocketItem_DEPRECATED = 1021
    EMsgGCSetItemPositions = 1077
    EMsgClientToGCUnpackBundle = 2576
    EMsgClientToGCSetItemInventoryCategory = 2573
    EMsgClientToGCSetItemStyle = 2577
    EMsgGCUseMultipleItemsRequest = 2594
    EMsgGCRequestStoreSalesData = 2536
    EMsgGCExtractGems = 1086
    EMsgGCRemoveMakersMarkResponse = 1054
    EMsgGCPartnerRechargeRedirectURLRequest = 2559
    EMsgClientToGCUnpackBundleResponse = 2567

class EGCMsgInitiateTradeResponse(IntEnum):
    SteamGuardDuration = 18
    Using_New_Device = 21
    Target_Already_Trading = 4
    TooSoon = 8
    VAC_Banned_Initiator = 2
    Shared_Account_Initiator = 13
    Target_Blocked = 15
    Free_Account_Initiator_DEPRECATED = 12
    TooSoonPenalty = 9
    Trade_Banned_Initiator = 10
    Accepted = 0
    Service_Unavailable = 14
    Recent_Password_Reset = 20
    NeedVerifiedEmail = 16
    TheyCannotTrade = 19
    VAC_Banned_Target = 3
    Sent_Invalid_Cookie = 22
    TooRecentFriend = 23
    NotLoggedIn = 6
    Disabled = 5
    NeedSteamGuard = 17
    Cancel = 7
    WalledFundsNotTrusted = 24
    Trade_Banned_Target = 11
    Declined = 1

class EGCMsgResponse(IntEnum):
    EGCMsgResponseServerError = 2
    EGCMsgResponseDenied = 1
    EGCMsgFailedToCreate = 8
    EGCMsgResponseUnknownError = 6
    EGCMsgResponseInvalid = 4
    EGCMsgResponseTimeout = 3
    EGCMsgResponseNoMatch = 5
    EGCMsgResponseOK = 0
    EGCMsgResponseNotLoggedOn = 7

class EGCMsgUseItemResponse(IntEnum):
    ItemUsed_EventPointsGranted = 9
    GiftNoOtherPlayers = 1
    NotHighEnoughLevel = 7
    EventNotActive = 8
    ItemUsed = 0
    EmoticonUnlock_Complete = 12
    NotInLowPriorityPool = 6
    ItemUsed_ItemsGranted = 4
    DropRateBonusAlreadyGranted = 5
    ItemUsed_Compendium = 13
    MiniGameAlreadyStarted = 3
    EmoticonUnlock_NoNew = 11
    MissingRequirement = 10
    ServerError = 2

class EGCPartnerRequestResponse(IntEnum):
    EPartnerRequestNotLinked = 3
    EPartnerRequestUnsupportedPartnerType = 4
    EPartnerRequestOK = 1
    EPartnerRequestBadAccount = 2

class EItemEditorReservationResult(IntEnum):
    AlreadyExists = 2
    TimedOut = 4
    OK = 1
    Reserved = 3

class EItemPurgatoryResponse_Finalize(IntEnum):
    ItemPurgatoryResponse_Finalize_Succeeded = 0
    ItemPurgatoryResponse_Finalize_BackpackFull = 5
    ItemPurgatoryResponse_Finalize_Failed_CouldNotFindItems = 3
    ItemPurgatoryResponse_Finalize_Failed_NoSOCache = 4
    ItemPurgatoryResponse_Finalize_Failed_Incomplete = 1
    ItemPurgatoryResponse_Finalize_Failed_ItemsNotInPurgatory = 2

class EItemPurgatoryResponse_Refund(IntEnum):
    ItemPurgatoryResponse_Refund_Succeeded = 0
    ItemPurgatoryResponse_Refund_Failed_NoDetail = 4
    ItemPurgatoryResponse_Refund_Failed_NoSOCache = 3
    ItemPurgatoryResponse_Refund_Failed_CouldNotFindItem = 2
    ItemPurgatoryResponse_Refund_Failed_ItemNotInPurgatory = 1

class ELaneSelection(IntEnum):
    OFFLANE = 1
    SUPPORT_HARD = 4
    SUPPORT_SOFT = 3
    SAFELANE = 0
    MIDLANE = 2

ELaneSelectionFlags = IntEnum('ELaneSelectionFlags', {
    'CORE': 7,
    'None': 0,
    'MIDLANE': 4,
    'SUPPORT': 24,
    'SUPPORT_SOFT': 8,
    'OFFLANE': 2,
    'SAFELANE': 1,
    'SUPPORT_HARD': 16,
    })

class ELaneType(IntEnum):
    LANE_TYPE_SAFE = 1
    LANE_TYPE_JUNGLE = 4
    LANE_TYPE_OFF = 2
    LANE_TYPE_MID = 3
    LANE_TYPE_ROAM = 5
    LANE_TYPE_UNKNOWN = 0

class ELeagueAuditAction(IntEnum):
    LEAGUE_AUDIT_ACTION_LEAGUE_IMAGE_UPDATED = 9
    LEAGUE_AUDIT_ACTION_NODEGROUP_CREATE = 100
    LEAGUE_AUDIT_ACTION_NODEGROUP_REMOVE_TEAM = 103
    LEAGUE_AUDIT_ACTION_NODE_EDIT = 209
    LEAGUE_AUDIT_ACTION_LEAGUE_REMOVE_INVITED_TEAM = 18
    LEAGUE_AUDIT_ACTION_LEAGUE_STREAM_EDIT = 20
    LEAGUE_AUDIT_ACTION_LEAGUE_STATUS_CHANGED = 19
    LEAGUE_AUDIT_ACTION_NODE_SET_SERIES_ID = 204
    LEAGUE_AUDIT_ACTION_LEAGUE_ADD_PRIZE_POOL_ITEM = 13
    LEAGUE_AUDIT_ACTION_NODE_CREATE = 200
    LEAGUE_AUDIT_ACTION_NODEGROUP_POPULATE = 106
    LEAGUE_AUDIT_ACTION_LEAGUE_REMOVE_PRIZE_POOL_ITEM = 14
    LEAGUE_AUDIT_ACTION_NODE_SET_TIME = 206
    LEAGUE_AUDIT_ACTION_LEAGUE_STREAM_ADD = 7
    LEAGUE_AUDIT_ACTION_LEAGUE_MATCH_END = 16
    LEAGUE_AUDIT_ACTION_NODEGROUP_DESTROY = 101
    LEAGUE_AUDIT_ACTION_NODE_MATCH_COMPLETED = 207
    LEAGUE_AUDIT_ACTION_LEAGUE_SET_PRIZE_POOL = 12
    LEAGUE_AUDIT_ACTION_NODEGROUP_ADD_TEAM = 102
    LEAGUE_AUDIT_ACTION_NODEGROUP_EDIT = 105
    LEAGUE_AUDIT_ACTION_NODE_DESTROY = 201
    LEAGUE_AUDIT_ACTION_INVALID = 0
    LEAGUE_AUDIT_ACTION_NODEGROUP_SET_ADVANCING = 104
    LEAGUE_AUDIT_ACTION_LEAGUE_MESSAGE_ADDED = 10
    LEAGUE_AUDIT_ACTION_LEAGUE_ADMIN_ADD = 4
    LEAGUE_AUDIT_ACTION_LEAGUE_ADD_INVITED_TEAM = 17
    LEAGUE_AUDIT_ACTION_LEAGUE_ADMIN_REVOKE = 5
    LEAGUE_AUDIT_ACTION_LEAGUE_EDIT = 2
    LEAGUE_AUDIT_ACTION_NODEGROUP_COMPLETED = 107
    LEAGUE_AUDIT_ACTION_NODE_SET_ADVANCING = 205
    LEAGUE_AUDIT_ACTION_LEAGUE_STREAM_REMOVE = 8
    LEAGUE_AUDIT_ACTION_NODE_SET_TEAM = 203
    LEAGUE_AUDIT_ACTION_LEAGUE_CREATE = 1
    LEAGUE_AUDIT_ACTION_LEAGUE_DELETE = 3
    LEAGUE_AUDIT_ACTION_LEAGUE_SUBMITTED = 11
    LEAGUE_AUDIT_ACTION_LEAGUE_ADMIN_PROMOTE = 6
    LEAGUE_AUDIT_ACTION_NODE_AUTOCREATE = 202
    LEAGUE_AUDIT_ACTION_NODE_COMPLETED = 208
    LEAGUE_AUDIT_ACTION_LEAGUE_MATCH_START = 15

class ELeagueBroadcastProvider(IntEnum):
    LEAGUE_BROADCAST_UNKNOWN = 0
    LEAGUE_BROADCAST_STEAM = 1
    LEAGUE_BROADCAST_TWITCH = 2
    LEAGUE_BROADCAST_YOUTUBE = 3
    LEAGUE_BROADCAST_OTHER = 100

class ELeagueFantasyPhase(IntEnum):
    LEAGUE_FANTASY_PHASE_QUALIFIER_CIS = 5
    LEAGUE_FANTASY_PHASE_QUALIFIER_EUROPE = 4
    LEAGUE_FANTASY_PHASE_UNSET = 0
    LEAGUE_FANTASY_PHASE_QUALIFIER_CHINA = 6
    LEAGUE_FANTASY_PHASE_QUALIFIER_SA = 3
    LEAGUE_FANTASY_PHASE_QUALIFIER_NA = 2
    LEAGUE_FANTASY_PHASE_MAIN = 1
    LEAGUE_FANTASY_PHASE_QUALIFIER_SEA = 7

class ELeagueFlags(IntEnum):
    LEAGUE_COMPENDIUM_PUBLIC = 8
    LEAGUE_FLAGS_NONE = 0
    LEAGUE_COMPENDIUM_ALLOWED = 4
    LEAGUE_ACCEPTED_AGREEMENT = 1
    LEAGUE_PAYMENT_EMAIL_SENT = 2

class ELeaguePhase(IntEnum):
    LEAGUE_PHASE_REGIONAL_QUALIFIER = 1
    LEAGUE_PHASE_UNSET = 0
    LEAGUE_PHASE_GROUP_STAGE = 2
    LEAGUE_PHASE_MAIN_EVENT = 3

class ELeagueRegion(IntEnum):
    LEAGUE_REGION_NA = 1
    LEAGUE_REGION_UNSET = 0
    LEAGUE_REGION_SEA = 6
    LEAGUE_REGION_SA = 2
    LEAGUE_REGION_EUROPE = 3
    LEAGUE_REGION_CHINA = 5
    LEAGUE_REGION_CIS = 4

class ELeagueStatus(IntEnum):
    LEAGUE_STATUS_REJECTED = 4
    LEAGUE_STATUS_ACCEPTED = 3
    LEAGUE_STATUS_DELETED = 6
    LEAGUE_STATUS_UNSUBMITTED = 1
    LEAGUE_STATUS_CONCLUDED = 5
    LEAGUE_STATUS_UNSET = 0
    LEAGUE_STATUS_SUBMITTED = 2

class ELeagueTier(IntEnum):
    LEAGUE_TIER_INTERNATIONAL = 5
    LEAGUE_TIER_AMATEUR = 1
    LEAGUE_TIER_MINOR = 3
    LEAGUE_TIER_UNSET = 0
    LEAGUE_TIER_MAJOR = 4
    LEAGUE_TIER_PROFESSIONAL = 2

class ELeagueTierCategory(IntEnum):
    LEAGUE_TIER_CATEGORY_DPC = 3
    LEAGUE_TIER_CATEGORY_PROFESSIONAL = 2
    LEAGUE_TIER_CATEGORY_AMATEUR = 1

class EMatchGroupServerStatus(IntEnum):
    LimitedAvailability = 1
    Offline = 2
    OK = 0

class EMatchOutcome(IntEnum):
    Unknown = 0
    NotScored_NeverStarted = 67
    NotScored_ServerCrash = 66
    NotScored_PoorNetworkConditions = 64
    NotScored_Leaver = 65
    RadVictory = 2
    NotScored_Canceled = 68
    DireVictory = 3

class EPartyBeaconType(IntEnum):
    Available = 0
    Joinable = 1

class EPlayerCoachMatchFlag(IntEnum):
    EligibleForRewards = 1

class EProfileCardSlotType(IntEnum):
    Trophy = 2
    Emoticon = 5
    Stat = 1
    Hero = 4
    Item = 3
    Team = 6
    Empty = 0

class EPurchaseHeroRelicResult(IntEnum):
    AlreadyOwned = 6
    Success = 0
    PurchaseNotAllowed = 4
    FailedToSend = 1
    InternalServerError = 3
    InvalidRelic = 5
    NotEnoughPoints = 2

class EReadyCheckRequestResult(IntEnum):
    NotInParty = 2
    SendError = 3
    AlreadyInProgress = 1
    Success = 0
    UnknownError = 4

class EReadyCheckStatus(IntEnum):
    NotReady = 1
    Unknown = 0
    Ready = 2

class ESOMsg(IntEnum):
    CacheSubscribedUpToDate = 29
    Create = 21
    Update = 22
    CacheSubscribed = 24
    UpdateMultiple = 26
    Destroy = 23
    CacheUnsubscribed = 25
    CacheSubscriptionRefresh = 28

class ESourceEngine(IntEnum):
    ESE_Source2 = 1
    ESE_Source1 = 0

class ESpecialPingValue(IntEnum):
    Failed = 16383
    NoData = 16382

class EStartFindingMatchResult(IntEnum):
    WeekendTourneyBadPartySize = 114
    WeekendTourneyIndividualBuyInTooLarge = 116
    CompetitiveNotEnoughPlayTime = 109
    Invalid = 0
    InvalidRoleSelections = 125
    MatchmakingCooldown = 104
    WeekendTourneyRecentParticipation = 120
    MemberAlreadyInLobby = 112
    FailedIgnore = 101
    NotMemberOfClan = 122
    MemberMissingAnchoredPhoneNumber = 121
    CompetitiveRankSpreadTooLarge = 111
    CompetitiveNotUnlocked = 107
    RegionOffline = 103
    WeekendTourneyNotUnlocked = 119
    FailGeneric = 100
    MatchmakingDisabled = 102
    MemberMissingEventOwnership = 118
    AlreadySearching = 2
    CoachesChallengeRequirementsNotMet = 124
    WeekendTourneyTeamBuyInTooLarge = 117
    MemberNotVACVerified = 113
    ClientOutOfDate = 105
    OK = 1
    CoachesChallengeBadPartySize = 123
    WeekendTourneyTeamBuyInTooSmall = 115
    MissingInitialSkill = 110
    CompetitiveNoLowPriority = 106
    GameModeNotUnlocked = 108

class ESupportEventRequestResult(IntEnum):
    InvalidActionID = 11
    InvalidSupportAccount = 7
    Success = 0
    InvalidPremiumPoints = 10
    EventExpired = 6
    InvalidSupportMessage = 8
    InvalidEventPoints = 9
    TransactionFailed = 13
    Timeout = 1
    InvalidActionScore = 12
    ItemNotInInventory = 3
    InvalidEvent = 5
    CantLockSOCache = 2
    InvalidItemDef = 4

class ETeamInviteResult(IntEnum):
    TEAM_INVITE_FAILURE_INVITE_REJECTED = 1
    TEAM_INVITE_ERROR_INVITEE_NOT_AVAILABLE = 5
    TEAM_INVITE_SUCCESS = 0
    TEAM_INVITE_ERROR_INVITEE_BUSY = 6
    TEAM_INVITE_ERROR_TEAM_LOCKED = 4
    TEAM_INVITE_ERROR_INCORRECT_USER_RESPONDED = 12
    TEAM_INVITE_ERROR_INVITEE_AT_TEAM_LIMIT = 8
    TEAM_INVITE_ERROR_INVITER_NOT_ADMIN = 11
    TEAM_INVITE_ERROR_TEAM_AT_MEMBER_LIMIT = 3
    TEAM_INVITE_ERROR_INVITEE_ALREADY_MEMBER = 7
    TEAM_INVITE_FAILURE_INVITE_TIMEOUT = 2
    TEAM_INVITE_ERROR_UNSPECIFIED = 13
    TEAM_INVITE_ERROR_INVITEE_INSUFFICIENT_PLAY_TIME = 9
    TEAM_INVITE_ERROR_INVITER_INVALID_ACCOUNT_TYPE = 10

ETournamentEvent = IntEnum('ETournamentEvent', {
    'TournamentCanceledByAdmin': 5,
    'None': 0,
    'TournamentCreated': 1,
    'TeamParticipationTimedOut_GrantedVictory': 11,
    'GameOutcome': 3,
    'TeamAbandoned': 6,
    'TeamGivenBye': 4,
    'TeamParticipationTimedOut_EntryFeeForfeit': 10,
    'Canceled': 8,
    'TeamParticipationTimedOut_EntryFeeRefund': 9,
    'TournamentsMerged': 2,
    'ScheduledGameStarted': 7,
    })

class ETournamentGameState(IntEnum):
    Scheduled = 2
    ServerFailure = 40
    Unknown = 0
    DireVictoryByForfeit = 23
    RadVictoryByForfeit = 22
    Canceled = 1
    RadVictory = 20
    Active = 3
    DireVictory = 21
    NotNeeded = 41

class ETournamentNodeState(IntEnum):
    ServerFailure = 11
    InBetweenGames = 3
    A_Bye = 9
    A_TimeoutRefund = 13
    Unknown = 0
    A_Abandoned = 10
    Canceled = 1
    GameInProgress = 4
    A_TimeoutForfeit = 12
    TeamsNotYetAssigned = 2
    A_Won = 5
    B_Won = 6
    A_WonByForfeit = 7
    B_WonByForfeit = 8

class ETournamentState(IntEnum):
    ServerFailure = 4
    WaitingToMerge = 101
    Unknown = 0
    Completed = 2
    TeamTimeoutRefund = 7
    TeamAbandoned = 5
    ServerFailureGrantedVictory = 8
    CanceledByAdmin = 1
    InProgress = 100
    TeamTimeoutForfeit = 6
    TeamTimeoutGrantedVictory = 9
    Merged = 3

class ETournamentTeamState(IntEnum):
    Finished3rd = 15003
    Finished2nd = 15002
    Finished13th = 15013
    Finished15th = 15015
    Finished8th = 15008
    Unknown = 0
    Finished14th = 15014
    Forfeited = 14004
    Finished5th = 15005
    Finished4th = 15004
    Finished12th = 15012
    Finished9th = 15009
    Finished11th = 15011
    Finished1st = 15001
    Finished6th = 15006
    Node1 = 1
    NodeMax = 1024
    Eliminated = 14003
    Finished16th = 15016
    Finished10th = 15010
    Finished7th = 15007

ETournamentTemplate = IntEnum('ETournamentTemplate', {
    'None': 0,
    'AutomatedWin3': 1,
    })

class ETourneyQueueDeadlineState(IntEnum):
    Missed = 1
    Normal = 0
    NA = -1
    ExpiringSoon = 101
    SeekingBye = 3
    ExpiredOK = 2
    EligibleForRefund = 4

EWeekendTourneyRichPresenceEvent = IntEnum('EWeekendTourneyRichPresenceEvent', {
    'None': 0,
    'WonMatch': 2,
    'Eliminated': 3,
    'StartedMatch': 1,
    })

class Fantasy_Roles(IntEnum):
    FANTASY_ROLE_CORE = 1
    FANTASY_ROLE_MID = 4
    FANTASY_ROLE_SUPPORT = 2
    FANTASY_ROLE_UNDEFINED = 0
    FANTASY_ROLE_OFFLANE = 3

class Fantasy_Selection_Mode(IntEnum):
    FANTASY_SELECTION_DRAFTING = 7
    FANTASY_SELECTION_INVALID = 0
    FANTASY_SELECTION_LOCKED = 1
    FANTASY_SELECTION_REGULAR_SEASON = 8
    FANTASY_SELECTION_PRE_DRAFT = 6
    FANTASY_SELECTION_FREE_PICK = 3
    FANTASY_SELECTION_SHUFFLE = 2
    FANTASY_SELECTION_ENDED = 4
    FANTASY_SELECTION_CARD_BASED = 9
    FANTASY_SELECTION_PRE_SEASON = 5

class Fantasy_Team_Slots(IntEnum):
    FANTASY_SLOT_CORE = 1
    FANTASY_SLOT_ANY = 3
    FANTASY_SLOT_NONE = 0
    FANTASY_SLOT_BENCH = 4
    FANTASY_SLOT_SUPPORT = 2

class GCConnectionStatus(IntEnum):
    NO_STEAM = 4
    HAVE_SESSION = 0
    STEAM_GOING_DOWN = 6
    GC_GOING_DOWN = 1
    NO_SESSION = 2
    SUSPENDED = 5
    NO_SESSION_IN_LOGON_QUEUE = 3

class GCProtoBufMsgSrc(IntEnum):
    FromSystem = 1
    ReplySystem = 4
    SpoofedSteamID = 5
    FromSteamID = 2
    Unspecified = 0
    FromGC = 3

class LobbyDotaPauseSetting(IntEnum):
    Disabled = 2
    Limited = 1
    Unlimited = 0

class LobbyDotaTVDelay(IntEnum):
    LobbyDotaTV_120 = 1
    LobbyDotaTV_300 = 2
    LobbyDotaTV_10 = 0

class MatchLanguages(IntEnum):
    MATCH_LANGUAGE_ENGLISH2 = 7
    MATCH_LANGUAGE_KOREAN = 4
    MATCH_LANGUAGE_SPANISH = 5
    MATCH_LANGUAGE_RUSSIAN = 2
    MATCH_LANGUAGE_CHINESE = 3
    MATCH_LANGUAGE_INVALID = 0
    MATCH_LANGUAGE_ENGLISH = 1
    MATCH_LANGUAGE_PORTUGUESE = 6

class MatchType(IntEnum):
    MATCH_TYPE_CASUAL = 0
    MATCH_TYPE_SEASONAL_RANKED = 8
    MATCH_TYPE_LOWPRI_DEPRECATED = 9
    MATCH_TYPE_LEGACY_TEAM_RANKED = 2
    MATCH_TYPE_COMPETITIVE = 4
    MATCH_TYPE_LEGACY_SOLO_QUEUE = 3
    MATCH_TYPE_CASUAL_1V1 = 6
    MATCH_TYPE_MUTATION = 11
    MATCH_TYPE_COOP_BOTS = 1
    MATCH_TYPE_COACHES_CHALLENGE = 12
    MATCH_TYPE_WEEKEND_TOURNEY = 5
    MATCH_TYPE_STEAM_GROUP = 10
    MATCH_TYPE_EVENT = 7

class PartnerAccountType(IntEnum):
    PARTNER_PERFECT_WORLD = 1
    PARTNER_INVALID = 3
    PARTNER_NONE = 0

__all__ = [
    'DOTA_2013PassportSelectionIndices',
    'DOTA_BOT_MODE',
    'DOTA_CM_PICK',
    'DOTA_COMBATLOG_TYPES',
    'DOTA_GameMode',
    'DOTA_GameState',
    'DOTA_GC_TEAM',
    'DOTA_LobbyMemberXPBonus',
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
    'ECoachTeammateRating',
    'ECustomGameInstallStatus',
    'ECustomGameWhitelistState',
    'EDACPlatform',
    'EDevEventRequestResult',
    'EDOTAGCMsg',
    'EDOTAGCSessionNeed',
    'EDOTAGroupMergeResult',
    'EDOTAPlayerMMRType',
    'EDOTATriviaAnswerResult',
    'EDOTATriviaQuestionCategory',
    'EDPCFavoriteType',
    'EDPCPushNotification',
    'EEvent',
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
    'EItemEditorReservationResult',
    'EItemPurgatoryResponse_Finalize',
    'EItemPurgatoryResponse_Refund',
    'ELaneSelection',
    'ELaneSelectionFlags',
    'ELaneType',
    'ELeagueAuditAction',
    'ELeagueBroadcastProvider',
    'ELeagueFantasyPhase',
    'ELeagueFlags',
    'ELeaguePhase',
    'ELeagueRegion',
    'ELeagueStatus',
    'ELeagueTier',
    'ELeagueTierCategory',
    'EMatchGroupServerStatus',
    'EMatchOutcome',
    'EPartyBeaconType',
    'EPlayerCoachMatchFlag',
    'EProfileCardSlotType',
    'EPurchaseHeroRelicResult',
    'EReadyCheckRequestResult',
    'EReadyCheckStatus',
    'ESOMsg',
    'ESourceEngine',
    'ESpecialPingValue',
    'EStartFindingMatchResult',
    'ESupportEventRequestResult',
    'ETeamInviteResult',
    'ETournamentEvent',
    'ETournamentGameState',
    'ETournamentNodeState',
    'ETournamentState',
    'ETournamentTeamState',
    'ETournamentTemplate',
    'ETourneyQueueDeadlineState',
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
