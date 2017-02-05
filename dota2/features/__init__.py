from dota2.features.player import Player
from dota2.features.match import Match
from dota2.features.lobby import Lobby
from dota2.features.chat import ChatBase
from dota2.features.sharedobjects import SOBase
from dota2.features.party import Party


class FeatureBase(Player, Match, Lobby, Party, ChatBase, SOBase):
    """
    This object is used to all high level functionality to Dota2Client.
    The features are seperated into submodules with a single class.
    """
    pass
