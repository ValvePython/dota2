"""
This module contains various :class:`enum.IntEnum` generated at runtime from protobufs.
Why generate python enums? In short, protobuf's enums aren't great.
:class:`enum.IntEnum` are much more flexible and easy to work with.
"""

import re
from enum import IntEnum
from google.protobuf.internal.enum_type_wrapper import EnumTypeWrapper

_proto_modules = [
    'base_gcmessages_pb2',
    'dota_client_enums_pb2',
    'dota_gcmessages_client_pb2',
    'dota_gcmessages_client_fantasy_pb2',
    'dota_gcmessages_client_match_management_pb2',
    'dota_gcmessages_client_team_pb2',
    'dota_gcmessages_client_tournament_pb2',
    'dota_gcmessages_common_pb2',
    'dota_gcmessages_common_match_management_pb2',
    'dota_gcmessages_msgid_pb2',
    'dota_shared_enums_pb2',
    'gcsdk_gcmessages_pb2',
    'gcsystemmsgs_pb2',
    'steammessages_pb2',
]

_proto_module = __import__("dota2.protobufs", globals(), locals(), _proto_modules, 0)

for name in _proto_modules:

    proto = getattr(_proto_module, name)
    gvars = globals()

    for key, value in proto.__dict__.items():
        if not isinstance(value, EnumTypeWrapper):
            continue

        items = {}
        for ikey, ivalue in value.items():
            ikey = re.sub(r'^(k_)?(%s_)?' % key, '', ikey)
            items[ikey] = ivalue

        gvars[key] = IntEnum(key, items)


class ESOType(IntEnum):
    CSOEconItem = 1
    CSOItemRecipe = 5
    CSOEconGameAccountClient = 7
    CSOSelectedItemPreset = 35      # no longer exists in game files
    CSOEconItemPresetInstance = 36  # no longer exists in game files
    CSOEconItemDropRateBonus = 38
    CSOEconItemLeagueViewPass = 39
    CSOEconItemEventTicket = 40
    CSOEconItemTournamentPassport = 42
    CSODOTAGameAccountClient = 2002
    CSODOTAParty = 2003
    CSODOTALobby = 2004
    CSODOTAPartyInvite = 2006
    CSODOTAGameHeroFavorites = 2007
    CSODOTAMapLocationState = 2008
    CMsgDOTATournament = 2009
    CSODOTAPlayerChallenge = 2010
    CSODOTALobbyInvite = 2011

del re, IntEnum, EnumTypeWrapper, _proto_modules, _proto_module, name, proto, gvars, key, value, items, ikey, ivalue

