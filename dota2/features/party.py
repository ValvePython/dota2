from dota2.enums import EGCBaseMsg, EDOTAGCMsg


class Party(object):

    def __init__(self):
        super(Party, self).__init__()
        self.party = None
        self.on(EGCBaseMsg.EMsgGCInvitationCreated,
                self.__handle_invitation_created)

    def __handle_invitation_created(self, message):
        self.emit('invitation_created', message)

    def response_party_invite(self, party_id=None, accept=False):
        """
        Responds to an incoming party invite.

        :param party_id: party id
        :param accept: accept
        :return: job event id
        :rtype: str

        Response event: ``response_party_invite``

        :param party_id: party_id for response
        :type party_id: :class:`int`
        :param accept: accept for response
        :type accept: :class:`bool`

        :param message: `CMsgPartyInviteResponse <https://github.com/ValvePython/dota2/blob/master/protobufs/base_gcmessages.proto#L99>`_ proto message
        """
        if not party_id:
            if self.verbose_debug:
                self._LOG.debug("Party ID required to respond to an invite.")
            return False

        if self.verbose_debug:
            self._LOG.debug(
                "Responding to party invite %s, accept: %s" %
                (party_id, accept))

        jobid = self.send_job(EGCBaseMsg.EMsgGCPartyInviteResponse, {
            "party_id": party_id,
            "accept": accept
        })

        @self.once(jobid)
        def wrap_response_party_invite(message):
            self.emit('response_party_invite', party_id, accept, message)

        return jobid

    def leave_party(self):
        """
        Leaves the current party.

        :return: job event id
        :rtype: str

        Response event: ``leave_party``

        :param message: `CMsgLeaveParty <https://github.com/ValvePython/dota2/blob/master/protobufs/base_gcmessages.proto#L118>`_ proto message
        """
        if self.verbose_debug:
            self._LOG.debug("Leaving party.")

        self.party = None

        jobid = self.send_job(EGCBaseMsg.EMsgGCLeaveParty, {})

        @self.once(jobid)
        def wrap_leave_party(message):
            self.emit('leave_party', message)

        return jobid

    def set_party_leader(self, steam_id=None):
        """
        Set the new party leader.

        :param steam_id: steam_id
        :return: job event id
        :rtype: str

        Response event: ``set_party_leader``

        :param steam_id: steam_id for response
        :type steam_id: :class:`int`

        :param message: `CMsgDOTASetGroupLeader <https://github.com/ValvePython/dota2/blob/master/protobufs/dota_gcmessages_client_match_management.proto#L345>`_ proto message
        """
        if not self.party:
            if self.verbose_debug:
                self._LOG.debug(
                    "set_party_leader called when not in a party!.")
            return False

        if not steam_id:
            if self.verbose_debug:
                self._LOG.debug("Steam ID required to set party leader.")
            return False

        if self.verbose_debug:
            self._LOG.debug("Setting party leader: %s" % steam_id)

        jobid = self.send_job(EDOTAGCMsg.EMsgClientToGCSetPartyLeader, {
            "new_leader_steamid": steam_id
        })

        @self.once(jobid)
        def wrap_set_party_leader(message):
            self.emit('set_party_leader', steam_id, message)

        return jobid

    def set_party_coach(self, coach=False):
        """
        Set the bot's status as a coach.

        :param coach: bool
        :return: job event id
        :rtype: str

        Response event: ``party_coach``

        :param steam_id: steam_id for response
        :type steam_id: :class:`int`

        :param message: `CMsgDOTAPartyMemberSetCoach <https://github.com/ValvePython/dota2/blob/master/protobufs/dota_gcmessages_client_match_management.proto#L341>`_ proto message
        """
        if not self.party:
            if self.verbose_debug:
                self._LOG.debug("set_party_coach called when not in a party!")
            return False

        if self.verbose_debug:
            self._LOG.debug("Setting coach slot: %s" % coach)

        jobid = self.send_job(EDOTAGCMsg.EMsgGCPartyMemberSetCoach, {
            "wants_coach": coach
        })

        @self.once(jobid)
        def wrap_party_coach(message):
            self.emit('party_coach', coach, message)

        return jobid

    def invite_to_party(self, steam_id=None):
        """
        Invites a player to a party. This will create a new party
        if you aren't in one.

        :param steam_id: steam_id
        :return: job event id
        :rtype: str

        Response event: ``invite_to_party``

        :param steam_id: steam_id for response
        :type steam_id: :class:`int`

        :param message: `CMsgInviteToParty <https://github.com/ValvePython/dota2/blob/master/protobufs/base_gcmessages.proto#L80>`_ proto message
        """
        if not steam_id:
            if self.verbose_debug:
                self._LOG.debug("Steam ID required to create a party invite.")
            return False

        if self.verbose_debug:
            self._LOG.debug("Inviting %s to a party." % steam_id)

        jobid = self.send_job(EGCBaseMsg.EMsgGCInviteToParty, {
            "steam_id": steam_id
        })

        @self.once(jobid)
        def wrap_invite_to_party(message):
            self.emit('invite_to_party', steam_id, message)

        return jobid

    def kick_from_party(self, steam_id=None):
        """
        Kicks a player from the party. This will create a new party
        if you aren't in one.

        :param steam_id: steam_id
        :return: job event id
        :rtype: str

        Response event: ``kick_from_party``

        :param steam_id: steam_id for response
        :type steam_id: :class:`int`

        :param message: `CMsgKickFromParty <https://github.com/ValvePython/dota2/blob/master/protobufs/base_gcmessages.proto#L114>`_ proto message
        """
        if not steam_id:
            if self.verbose_debug:
                self._LOG.debug("Steam ID required to kick from the party.")
            return False

        if self.verbose_debug:
            self._LOG.debug("Kicking %s from the party." % steam_id)

        jobid = self.send_job(EGCBaseMsg.EMsgGCKickFromParty, {
            "steam_id": steam_id
        })

        @self.once(jobid)
        def wrap_kick_from_party(message):
            self.emit('kick_from_party', steam_id, message)

        return jobid
