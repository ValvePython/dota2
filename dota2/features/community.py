from steam.enums import EResult
from dota2.enums import EDOTAGCMsg

class Community(object):
    def __init__(self):
        super(Community, self).__init__()

        # register our handlers
        self.on(EDOTAGCMsg.EMsgGCPlayerInfo, self.__handle_player_info)

    def request_profile(self, account_id, request_name=False):
        """
        Request profile details

        .. warning::

            This is disabled by Valve

        :param account_id: steam account_id
        :type account_id: :class:`int`
        :param request_name: whether to return name
        :type request_name: :class:`bool`
        :return: job id
        :rtype: :class:`str`

        Response event: ``profile_data``

        :param account_id: account_id from request
        :type account_id: :class:`int`
        :param eresult: result enum
        :type eresult: :class:`steam.enums.EResult`
        :param message: ``CMsgDOTAProfileResponse`` proto

        """
        jobid = self.send_job(EDOTAGCMsg.EMsgGCProfileRequest, {
                              'account_id': account_id,
                              'request_name': request_name,
                              })

        def wrap_profile_data(message):
            eresult = EResult(message.result)
            message = message if eresult == EResult.OK else None
            self.emit("profile_data", account_id, eresult, message)

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
        :param message: ``CMsgDOTAProfileCard`` proto

        """
        jobid = self.send_job(EDOTAGCMsg.EMsgClientToGCGetProfileCard, {
                              'account_id': account_id,
                              })

        def wrap_profile_card(message):
            self.emit("profile_card", account_id, message)

        self.once(jobid, wrap_profile_card)

        return jobid

    def request_player_info(self, account_ids):
        """
        Request official player information

        :param account_id: A list of account ids
        :type account_id: :class:`list`

        Response event: ``player_info``

        :param message: ``CMsgGCPlayerInfo`` proto

        """
        if not isinstance(account_ids, list):
            raise ValueError("Expected account_ids to be a list")

        self.send(EDOTAGCMsg.EMsgGCPlayerInfoRequest, {
                  'account_ids': account_ids,
                  })

    def __handle_player_info(self, message):
        self.emit("player_info", message)
