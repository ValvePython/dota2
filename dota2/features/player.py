from steam.enums import EResult
from dota2.enums import EDOTAGCMsg

class Player(object):
    def __init__(self):
        super(Player, self).__init__()

        # register our handlers
        self.on(EDOTAGCMsg.EMsgGCPlayerInfo, self.__handle_player_info)
        self.on(EDOTAGCMsg.EMsgClientToGCLatestConductScorecard, self.__handle_conduct_scorecard)
        self.on(EDOTAGCMsg.EMsgGCGetHeroStandingsResponse, self.__handle_hero_standings)

    def request_profile(self, account_id):
        """
        Request profile details

        :param account_id: steam account_id
        :type account_id: :class:`int`
        :return: job id
        :rtype: :class:`str`

        Response event: ``profile_data``

        :param account_id: account_id from request
        :type account_id: :class:`int`
        :param message: `CMsgProfileResponse <https://github.com/ValvePython/dota2/blob/98763e7b748a588462387469db65ea1a3e19a3af/protobufs/dota_gcmessages_client.proto#L2519-L2539>`_
        :type  message: proto message

        """
        jobid = self.send_job(EDOTAGCMsg.EMsgProfileRequest, {
                              'account_id': account_id,
                              })

        def wrap_profile_data(message):
            self.emit("profile_data", account_id, message)

        self.once(jobid, wrap_profile_data)

        return jobid

    def request_gc_profile(self, account_id, request_name=False):
        """
        Request profile details

        .. warning::
            Disabled by Valve

        :param account_id: steam account_id
        :type account_id: :class:`int`
        :param request_name: whether to return name
        :type request_name: :class:`bool`
        :return: job id
        :rtype: :class:`str`

        Response event: ``gc_profile_data``

        :param account_id: account_id from request
        :type account_id: :class:`int`
        :param eresult: result enum
        :type eresult: :class:`steam.enums.common.EResult`
        :param message: `CMsgDOTAProfileResponse <https://github.com/ValvePython/dota2/blob/e06c81c03579a912fcca829766ee590075ae97dc/protobufs/dota_gcmessages_client.proto#L282-L323>`_
        :type  message: proto message

        """
        jobid = self.send_job(EDOTAGCMsg.EMsgGCProfileRequest, {
                              'account_id': account_id,
                              'request_name': request_name,
                              })

        def wrap_profile_data(message):
            eresult = EResult(message.result)
            message = message if eresult == EResult.OK else None
            self.emit("gc_profile_data", account_id, eresult, message)

        self.once(jobid, wrap_profile_data)

        return jobid

    def request_profile_card(self, account_id):
        """
        Request profile card

        :param account_id: steam account_id
        :type account_id: :class:`int`
        :return: job id
        :rtype: :class:`str`

        Response event: ``profile_card``

        :param account_id: account_id from request
        :type account_id: :class:`int`
        :param message: `CMsgDOTAProfileCard <https://github.com/ValvePython/dota2/blob/e06c81c03579a912fcca829766ee590075ae97dc/protobufs/dota_gcmessages_common.proto#L375-L426>`_
        :type  message: proto message

        """
        jobid = self.send_job(EDOTAGCMsg.EMsgClientToGCGetProfileCard, {
                              'account_id': account_id,
                              })

        def wrap_profile_card(message):
            self.emit("profile_card", account_id, message)

        self.once(jobid, wrap_profile_card)

        return jobid

    def request_player_stats(self, account_id):
        """
        Request players stats. These are located in the ``play style`` box on a player profie.

        :param account_id: steam account_id
        :type account_id: :class:`int`
        :return: job id
        :rtype: :class:`str`

        Response event: ``player_stats``

        :param account_id: account_id from request
        :type account_id: :class:`int`
        :param message: `CMsgGCToClientPlayerStatsResponse <https://github.com/ValvePython/dota2/blob/e06c81c03579a912fcca829766ee590075ae97dc/protobufs/dota_gcmessages_client.proto#L1159-L1179>`_
        :type  message: proto message

        """
        jobid = self.send_job(EDOTAGCMsg.EMsgClientToGCPlayerStatsRequest, {
                              'account_id': account_id,
                              })

        def wrap_player_stats(message):
            self.emit("player_stats", account_id, message)

        self.once(jobid, wrap_player_stats)

        return jobid

    def request_player_info(self, account_ids):
        """
        .. warning::
            Disabled by Valve

        Request official player information

        :param account_id: A list of account ids
        :type account_id: :class:`list`

        Response event: ``player_info``

        :param message: `CMsgGCPlayerInfo <https://github.com/ValvePython/dota2/blob/e06c81c03579a912fcca829766ee590075ae97dc/protobufs/dota_gcmessages_client_fantasy.proto#L106-L129>`_
        :type  message: proto message
        """
        if not isinstance(account_ids, list):
            raise ValueError("Expected account_ids to be a list")

        self.send(EDOTAGCMsg.EMsgGCPlayerInfoRequest, {
                  'player_infos': map(lambda x: {'account_id': x}, account_ids),
                  })

    def __handle_player_info(self, message):
        self.emit("player_info", message)

    def request_conduct_scorecard(self):
        """
        Request conduct scorecard, otherwise knows as conduct summary

        :return: job id
        :rtype: :class:`str`

        Response event: ``conduct_scorecard``

        :param message: `CMsgPlayerConductScorecard <https://github.com/ValvePython/dota2/blob/e06c81c03579a912fcca829766ee590075ae97dc/protobufs/dota_gcmessages_client.proto#L1415-L1429>`_
        :type  message: proto message
        """
        return self.send_job(EDOTAGCMsg.EMsgClientToGCLatestConductScorecardRequest)

    def __handle_conduct_scorecard(self, message):
        self.emit("conduct_scorecard", message)

    def request_hero_standings(self):
        """
        Request hero stands for the currently logged on account.
        This is the data from the ``stats`` tab on your profile.

        Response event: ``hero_standings``

        :param message: `CMsgGCGetHeroStandingsResponse <https://github.com/ValvePython/dota2/blob/e06c81c03579a912fcca829766ee590075ae97dc/protobufs/dota_gcmessages_client.proto#L721-L741>`_
        :type  message: proto message
        """
        return self.send_job(EDOTAGCMsg.EMsgGCGetHeroStandings)

    def __handle_hero_standings(self, message):
        self.emit("hero_standings", message)
