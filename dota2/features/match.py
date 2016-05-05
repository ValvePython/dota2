from steam.enums import EResult
from dota2.enums import EDOTAGCMsg

class Match(object):
    def __init__(self):
        super(Match, self).__init__()

        # register our handlers
        self.on(EDOTAGCMsg.EMsgGCMatchmakingStatsResponse, self.__handle_mmstats)
        self.on(EDOTAGCMsg.EMsgGCToClientFindTopSourceTVGamesResponse, self.__handle_top_source_tv)

    def request_matchmaking_stats(self):
        """
        Request matchmaking statistics

        Response event: ``matchmaking_stats``

        :param message: `CMsgDOTAMatchmakingStatsResponse <https://github.com/ValvePython/dota2/blob/master/protobufs/dota_gcmessages_client.proto#L1948>`_ proto message

        """
        self.send(EDOTAGCMsg.EMsgGCMatchmakingStatsRequest)

    def __handle_mmstats(self, message):
        self.emit("matchmaking_stats", message)

    def request_match_details(self, match_id):
        """
        Request match details for a specific match

        :param match_id: match id
        :return: job event id
        :rtype: str

        Response event: ``match_details``

        :param match_id: match_id for response
        :type match_id: :class:`int`
        :param eresult: result enum
        :type eresult: :class:`steam.enums.EResult`
        :param match: `CMsgDOTAMatch <https://github.com/ValvePython/dota2/blob/master/protobufs/dota_gcmessages_client.proto#L489>`_ proto message
        """
        jobid = self.send_job(EDOTAGCMsg.EMsgGCMatchDetailsRequest, {
                              'match_id': match_id,
                              })

        def wrap_match_details(message):
            eresult = EResult(message.result)
            match = message.match if eresult == EResult.OK else None
            self.emit('match_details', match_id, eresult, match)

        self.once(jobid, wrap_match_details)

        return jobid


    def request_matches(self, **kwargs):
        """
        Request matches. For arguments see `CMsgDOTARequestMatches <https://github.com/ValvePython/dota2/blob/master/protobufs/dota_gcmessages_client.proto#L658>`_

        .. warning::
            Some of the arguments don't work even if you set them. Ask Valve.

        :return: job event id
        :rtype: str

        Response event: ``matches``

        :param message: `CMsgDOTARequestMatchesResponse <https://github.com/ValvePython/dota2/blob/master/protobufs/dota_gcmessages_client.proto#L682>`_ proto message
        """
        jobid = self.send_job(EDOTAGCMsg.EMsgGCRequestMatches, kwargs)

        def wrap_matches(message):
            self.emit('matches', message)
        self.once(jobid, wrap_matches)

        return jobid

    def request_matches_minimal(self, match_ids):
        """
        Request matches with only minimal data.

        :param match_ids: match ids
        :type match_ids: :class:`list`
        :return: job event id
        :rtype: str

        Response event: ``matches_minimal``

        :param matches: list of `CMsgDOTAMatchMinimal <https://github.com/SteamRE/SteamKit/blob/master/Resources/Protobufs/dota/dota_gcmessages_client.proto#L621>`_ proto message
        :type matches: :class:`list`

        """
        jobid = self.send_job(EDOTAGCMsg.EMsgClientToGCMatchesMinimalRequest, {
                              'match_ids': match_ids,
                              })

        def wrap_matches_minimal(message):
            self.emit('matches_minimal', message.matches)
        self.once(jobid, wrap_matches_minimal)

        return jobid

    def request_top_source_tv_games(self, **kwargs):
        """
        Find top source TV games.

        Response event: ``top_source_tv_games``

        :param response: `CMsgClientToGCFindTopSourceTVGames <https://github.com/ValvePython/dota2/blob/master/protobufs/dota_gcmessages_client.proto#L136>`_ proto message
        """
        self.send(EDOTAGCMsg.EMsgClientToGCFindTopSourceTVGames, kwargs)

    def __handle_top_source_tv(self, message):
        self.emit("top_source_tv_games", message)
