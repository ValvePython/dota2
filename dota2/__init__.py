__version__ = "0.2.0"
__author__ = "Rossen Georgiev"

version_info = (0, 2, 0)


# proxy object
# avoids importing dota2.enums unless it's needed
class Dota2Client(object):
    def __new__(cls, *args, **kwargs):
        from dota2.client import Dota2Client as D2C
        return D2C(*args, **kwargs)
