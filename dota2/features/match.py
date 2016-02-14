from steam.enums import EResult
from dota2.enums import EDOTAGCMsg

class Match(object):
    def __init__(self):
        super(Match, self).__init__()

        # register our handlers
        self.on(EDOTAGCMsg.EMsgGCMatchmakingStatsResponse, self.__handle_mmstats)
        self.on(EDOTAGCMsg.EMsgGCMatchDetailsResponse, self.__handle_match_details)

    def request_matchmaking_stats(self):
        """
        Request matchmaking statistics

        Response event: ``matchmaking_stats``

        """
        self.send(EDOTAGCMsg.EMsgGCMatchmakingStatsRequest)

    def __handle_mmstats(self, message):
        self.emit("matchmaking_stats", {
          'searching_players_by_group_source2': message.searching_players_by_group_source2,
          'legacy_disabled_groups_source2': message.legacy_disabled_groups_source2,
          'raw': message,
          })

    def request_match_details(self, match_id):
        """
        Request match details for a specific match

        :param match_id: match id
        :return: job event id
        :rtype: str

        Succesful response event: ``match_details``
        """
        return self.send_job(EDOTAGCMsg.EMsgGCMatchDetailsRequest, {
                             'match_id': match_id,
                             })

    def __handle_match_details(self, message):
        if message.result != EResult.OK:
            self._logger.error("Got %s for match_details" % repr(EResult(message.result)))
            return

        self.emit('match_details', message)
