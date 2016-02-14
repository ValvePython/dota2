from dota2.features.match import Match
from dota2.features.community import Community

class FeatureBase(Match, Community):
    """
    This object is used to all high level functionality to Dota2Client.
    The features are seperated into submodules with a single class.
    """
    pass
