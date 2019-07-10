from steam.enums import EResult
from dota2.enums import EDOTAGCMsg

class Match(object):
    def __init__(self):
        super(Match, self).__init__()

        # register our handlers
        self.on(EDOTAGCMsg.EMsgGCMatchmakingStatsResponse,             self.__handle_mmstats)
        self.on(EDOTAGCMsg.EMsgGCToClientFindTopSourceTVGamesResponse, self.__handle_top_source_tv)
        self.on(EDOTAGCMsg.EMsgDOTAGetPlayerMatchHistoryResponse,      self.__handle_player_match_history)
        self.on(EDOTAGCMsg.EMsgGCRequestMatches,                       self.__handle_matches)
        self.on(EDOTAGCMsg.EMsgClientToGCMatchesMinimalResponse,       self.__handle_matches_minimal)

    def request_matchmaking_stats(self):
        """
        Request matchmaking statistics

        Response event: ``matchmaking_stats``

        :param message: `CMsgDOTAMatchmakingStatsResponse <https://github.com/ValvePython/dota2/blob/e06c81c03579a912fcca829766ee590075ae97dc/protobufs/dota_gcmessages_client.proto#L607-L611>`_
        :type  message: proto message
        """
        self.send(EDOTAGCMsg.EMsgGCMatchmakingStatsRequest)

    def __handle_mmstats(self, message):
        self.emit("matchmaking_stats", message)

    def request_match_details(self, match_id):
        """Request match details for a specific match

        .. note::
            Rate limited to 100 requests/day

        :param match_id: match id
        :type  match_id: :class:`int`
        :return: job event id
        :rtype: :class:`str`

        Response event: ``match_details``

        :param match_id: match_id for response
        :type  match_id: :class:`int`
        :param eresult: result enum
        :type  eresult: :class:`steam.enums.common.EResult`
        :param match: `CMsgDOTAMatch <https://github.com/ValvePython/dota2/blob/e06c81c03579a912fcca829766ee590075ae97dc/protobufs/dota_gcmessages_common.proto#L866-L1001>`_
        :type  match: proto message
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
        """Request matches. For arguments see `CMsgDOTARequestMatches <https://github.com/ValvePython/dota2/blob/e06c81c03579a912fcca829766ee590075ae97dc/protobufs/dota_gcmessages_client.proto#L81-L103>`_

        .. note::
            Rate limited to 50 requests/day

        .. warning::
            Some of the arguments don't work. Ask Valve

        :return: job event id
        :rtype: :class:`str`

        Response event: ``matches``

        :param message: `CMsgDOTARequestMatchesResponse <https://github.com/ValvePython/dota2/blob/e06c81c03579a912fcca829766ee590075ae97dc/protobufs/dota_gcmessages_client.proto#L105-L117>`_
        :type  message: proto message
        """
        return self.send_job(EDOTAGCMsg.EMsgGCRequestMatches, kwargs)

    def __handle_matches(self, message):
        self.emit('matches', message)

    def request_matches_minimal(self, match_ids):
        """
        Request matches with only minimal data.

        :param match_ids: match ids
        :type  match_ids: :class:`list`
        :return: job event id
        :rtype: :class:`str`

        Response event: ``matches_minimal``

        :param matches: list of `CMsgDOTAMatchMinimal <https://github.com/ValvePython/dota2/blob/ca75440adca20d852b9aec3917e4387466848d5b/protobufs/dota_gcmessages_client_watch.proto#L120-L154>`_
        :type  matches: :class:`list`

        """
        return self.send_job(EDOTAGCMsg.EMsgClientToGCMatchesMinimalRequest, {'match_ids': match_ids})

    def __handle_matches_minimal(self, message):
        self.emit('matches_minimal', message.matches)

    def request_top_source_tv_games(self, **kwargs):
        """
        Find top source TV games. For arguments see `CMsgClientToGCFindTopSourceTVGames <https://github.com/ValvePython/dota2/blob/ca75440adca20d852b9aec3917e4387466848d5b/protobufs/dota_gcmessages_client_watch.proto#L42-L49>`_

        Response event: ``top_source_tv_games``

        :param response: `CMsgGCToClientFindTopSourceTVGamesResponse <https://github.com/ValvePython/dota2/blob/ca75440adca20d852b9aec3917e4387466848d5b/protobufs/dota_gcmessages_client_watch.proto#L51-L60>`_
        :type  response: proto message
        """
        self.send(EDOTAGCMsg.EMsgClientToGCFindTopSourceTVGames, kwargs)

    def __handle_top_source_tv(self, message):
        self.emit("top_source_tv_games", message)

    def request_player_match_history(self, **kwargs):
        """Request player match history

        :param account_id: account id
        :type  account_id: :class:`int`
        :param start_at_match_id: matches from before this match id (``0`` for latest)
        :type  start_at_match_id: :class:`int`
        :param matches_requested: number of matches to return
        :type  matches_requested: :class:`int`
        :param hero_id: filter by hero id
        :type  hero_id: :class:`int`
        :param request_id: request id to match with the response with the request
        :type  request_id: :class:`int`
        :param include_practice_matches: whether to include practive matches
        :type  include_practice_matches: :class:`bool`
        :param include_custom_games: whether to include custom matches
        :type  include_custom_games: :class:`bool`

        Response event: ``player_match_history``

        :param request_id: request id from the reuqest
        :type  request_id: :class:`int`
        :param matches: `CMsgDOTAGetPlayerMatchHistoryResponse.matches <https://github.com/ValvePython/dota2/blob/15729f58ac4ebbfad90414d43ef593eadd355b25/protobufs/dota_gcmessages_client.proto#L907-L934>`_
        :type  matches: :class:`list`

        """
        self.send(EDOTAGCMsg.EMsgDOTAGetPlayerMatchHistory, kwargs)

    def __handle_player_match_history(self, message):
        self.emit('player_match_history', message.request_id, message.matches)

