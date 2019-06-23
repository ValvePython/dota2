
from enum import IntEnum


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
    CSODOTAGameAccountPlus = 2012


class EServerRegion(IntEnum):
    Unspecified = 0
    USWest = 1
    USEast = 2
    Europe = 3  # EU West
    Korea = 4
    Singapore = 5
    Dubai = 6
    PerfectWorldTelecom = 12            # china
    PerfectWorldTelecomGuangdong = 17   #
    PerfectWorldTelecomZhejiang = 18    #
    PerfectWorldTelecomWuhan = 20       #
    PerfectWorldUnicom = 13             #
    PerfectWorldUnicomTianjin = 25      #
    Stockholm = 8  # Russia
    Brazil = 10
    Austria = 9  # EU East
    Australia = 7
    SouthAfrica = 11
    Chile = 14
    Peru = 15
    India = 16
    Japan = 19


# Do not remove
from sys import modules
from enum import EnumMeta

__all__ = [obj.__name__
           for obj in modules[__name__].__dict__.values()
           if obj.__class__ is EnumMeta and obj.__name__ != 'IntEnum'
           ]

del modules, EnumMeta
