from steam.enums import EResult
from dota2.enums import EDOTAGCMsg

class Match(object):
    def __init__(self):
        super(Match, self).__init__()

        # register our handlers
        self.on(EDOTAGCMsg.EMsgGCMatchmakingStatsResponse, self.__handle_mmstats)

    def request_matchmaking_stats(self):
        """
        Request matchmaking statistics

        Response event: ``matchmaking_stats``

        :param message: MatchmakingStatsResponse proto

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
        :param match: ``CMsgDOTAMatch`` proto
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
