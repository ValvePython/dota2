__version__ = "0.1.0a"
__author__ = "Rossen Georgiev"

version_info = (0, 1, 0, 'alpha')


# proxy object
# avoids importing dota2.enums unless it's needed
class Dota2Client(object):
    def __new__(cls, *args, **kwargs):
        from dota2.client import Dota2Client as D2C
        return D2C(*args, **kwargs)
