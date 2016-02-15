from steam.enums import EResult
from dota2.enums import EDOTAGCMsg

class Community(object):
    def __init__(self):
        super(Community, self).__init__()
        self.__profile_map = {}
        self.__profile_card_map = {}

        # register our handlers
        self.on(None, self.__handle_jobs)
        self.on(EDOTAGCMsg.EMsgGCPlayerInfo, self.__handle_player_info)

    def __handle_jobs(self, event, *args):
        if event in self.__profile_map:
            self.__handle_profile(event, *args)
        elif event in self.__profile_card_map:
            self.__handle_profile_card(event, *args)

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

        self.__profile_map[jobid] = account_id
        return jobid

    def __handle_profile(self, message):
        account_id = self.__profile_map.pop(event)
        eresult = EResult(message.result)
        message = message if eresult == EResult.OK else None

        self.emit("profile_data", account_id, eresult, message)

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

        self.__profile_card_map[jobid] = account_id
        return jobid

    def __handle_profile_card(self, event, message):
        account_id = self.__profile_card_map.pop(event)
        self.emit("profile_card", account_id, message)

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
