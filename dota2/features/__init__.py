from dota2.features.player import Player
from dota2.features.match import Match
from dota2.features.sharedobjects import SOBase

class FeatureBase(Player, Match, SOBase):
    """
    This object is used to all high level functionality to Dota2Client.
    The features are seperated into submodules with a single class.
    """
    pass
