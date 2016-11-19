from dota2.enums import EGCBaseMsg, EDOTAGCMsg, ESOType


class Party(object):
    EVENT_PARTY_INVITE = 'party_invite'
    """When a party invite is receieved

    :param message: `CSODOTAPartyInvite <https://github.com/ValvePython/dota2/blob/ca75440adca20d852b9aec3917e4387466848d5b/protobufs/dota_gcmessages_common_match_management.proto#L83>`_
    :type  message: proto message
    """
    EVENT_NEW_PARTY = 'new_party'
    """Entered a party, either by inviting someone or accepting an invite

    :param message: `CSODOTAParty <https://github.com/ValvePython/dota2/blob/ca75440adca20d852b9aec3917e4387466848d5b/protobufs/dota_gcmessages_common_match_management.proto#L32>`_
    :type  message: proto message
    """
    EVENT_PARTY_CHANGED = 'party_changed'
    """Anything changes to the party state, leaving/entering/invites etc

    :param message: `CSODOTAParty <https://github.com/ValvePython/dota2/blob/ca75440adca20d852b9aec3917e4387466848d5b/protobufs/dota_gcmessages_common_match_management.proto#L32>`_
    :type  message: proto message
    """
    EVENT_PARTY_REMOVED = 'party_removed'
    """Left party, either left, kicked or disbanded

    :param message: `CSODOTAParty <https://github.com/ValvePython/dota2/blob/ca75440adca20d852b9aec3917e4387466848d5b/protobufs/dota_gcmessages_common_match_management.proto#L32>`_
    :type  message: proto message
    """
    EVENT_INVITATION_CREATED = 'invitation_created'
    """After inviting another user

    :param message: `CMsgInvitationCreated <https://github.com/ValvePython/dota2/blob/ca75440adca20d852b9aec3917e4387466848d5b/protobufs/base_gcmessages.proto#L93>`_
    :type  message: proto message
    """

    party = None

    def __init__(self):
        super(Party, self).__init__()
        self.on('notready', self.__party_cleanup)
        self.socache.on(('new', ESOType.CSODOTAPartyInvite), self.__handle_party_invite)
        self.socache.on(('new', ESOType.CSODOTAParty), self.__handle_party_new)
        self.socache.on(('updated', ESOType.CSODOTAParty), self.__handle_party_changed)
        self.socache.on(('removed', ESOType.CSODOTAParty), self.__handle_party_removed)

        self.on(EGCBaseMsg.EMsgGCInvitationCreated, self.__handle_invitation_created)

    def __party_cleanup(self):
        self.party = None

    def __handle_party_invite(self, message):
        self.emit('party_invite', message)

    def __handle_party_new(self, message):
        self.party = message
        self.emit('new_party', message)

    def __handle_party_changed(self, message):
        self.party = message
        self.emit('party_changed', message)

    def __handle_party_removed(self, message):
        self.party = None
        self.emit('party_removed', message)

    def __handle_invitation_created(self, message):
        self.emit('invitation_created', message)

    def respond_to_party_invite(self, party_id, accept=False):
        """
        Respond to a party invite.

        :param party_id: party id
        :param accept: accept
        """
        if self.verbose_debug:
            self._LOG.debug("Responding to party invite %s, accept: %s" % (party_id, accept))

        self.send(EGCBaseMsg.EMsgGCPartyInviteResponse, {
            "party_id": party_id,
            "accept": accept
        })

    def leave_party(self):
        """
        Leaves the current party.

        :return: job event id
        :rtype: str
        """
        if self.verbose_debug:
            self._LOG.debug("Leaving party.")

        self.send(EGCBaseMsg.EMsgGCLeaveParty, {})

    def set_party_leader(self, steam_id):
        """
        Set the new party leader.

        :param steam_id: steam_id
        :return: job event id
        :rtype: str
        """
        if not self.party: return

        if self.verbose_debug:
            self._LOG.debug("Setting party leader: %s" % steam_id)

        self.send(EDOTAGCMsg.EMsgClientToGCSetPartyLeader, {
            "new_leader_steamid": steam_id
        })

    def set_party_coach_flag(self, coach):
        """
        Set the bot's status as a coach.

        :param coach: bool
        :return: job event id
        :rtype: str

        Response event: ``party_coach``

        :param steam_id: steam_id for response
        :type  steam_id: :class:`int`

        :param message: `CMsgDOTAPartyMemberSetCoach <https://github.com/ValvePython/dota2/blob/ca75440adca20d852b9aec3917e4387466848d5b/protobufs/dota_gcmessages_client_match_management.proto#L354>`_ proto message
        """
        if not self.party or self.party.leader_id != self.steam.steam_id: return

        if self.verbose_debug:
            self._LOG.debug("Setting coach flag to: %s" % coach)

        self.send(EDOTAGCMsg.EMsgGCPartyMemberSetCoach, {
            "wants_coach": coach
        })

    def invite_to_party(self, steam_id):
        """
        Invites a player to a party. This will create a new party if you aren't in one.

        :param steam_id: steam_id
        :return: job event id
        :rtype: str

        Response event: ``invite_to_party``

        :param message: `CMsgInvitationCreated <https://github.com/ValvePython/dota2/blob/ca75440adca20d852b9aec3917e4387466848d5b/protobufs/base_gcmessages.proto#L93>`_ proto message
        """
        if self.party and self.party.leader_id != self.steam.steam_id: return

        if self.verbose_debug:
            self._LOG.debug("Inviting %s to a party." % steam_id)

        jobid = self.send_job(EGCBaseMsg.EMsgGCInviteToParty, {
            "steam_id": steam_id
        })

        @self.once(jobid)
        def wrap_invite_to_party(message):
            self.emit('invitation_created', message)

        return jobid

    def kick_from_party(self, steam_id):
        """
        Kicks a player from the party. This will create a new party
        if you aren't in one.

        :param steam_id: steam_id
        :return: job event id
        :rtype: str

        Response event: ``kick_from_party``

        :param steam_id: steam_id for response
        :type  steam_id: :class:`int`

        :param message: `CMsgKickFromParty <https://github.com/ValvePython/dota2/blob/ca75440adca20d852b9aec3917e4387466848d5b/protobufs/base_gcmessages.proto#L114>`_ proto message
        """
        if (not self.party
            or self.party.leader_id != self.steam.steam_id
            or steam_id not in self.party.memeber_ids): return

        if self.verbose_debug:
            self._LOG.debug("Kicking %s from the party." % steam_id)

        self.send(EGCBaseMsg.EMsgGCKickFromParty, {
            "steam_id": steam_id
        })
