from steam.enums import EResult
from dota2.enums import EGCBaseMsg


class Party(object):

    def __init__(self):
        super(Party, self).__init__()

    def invite_to_party(self, steam_id=None):
        if not steam_id:
            self._LOG.debug("Steam ID required to create a party invite.")
            return False

        if self.verbose_debug:
            self._LOG.info("Inviting %s to a party." % steam_id)

        jobid = self.send_job(EGCBaseMsg.EMsgGCInviteToParty, {
            "steam_id": steam_id
        })

        def wrap_invite(message):
            self.emit('party_invite', message)
        self.once(jobid, wrap_invite)

        return jobid

    def kick_from_party(self, steam_id=None):
        if not steam_id:
            self._LOG.debug("Steam ID required to kick from the party.")
            return False

        if self.verbose_debug:
            self._LOG.info("Kicking %s from the party." % steam_id)

        jobid = self.send_job(EGCBaseMsg.EMsgGCKickFromParty, {
            "steam_id": steam_id
        })

        def wrap_kick(message):
            self.emit('party_kick', message)
        self.once(jobid, wrap_kick)

        return jobid
