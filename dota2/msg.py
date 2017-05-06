"""
Various utility function for dealing with messages.

"""

from dota2.enums import EGCBaseClientMsg, EDOTAGCMsg, ESOMsg, EGCItemMsg, EGCBaseMsg
from dota2.protobufs import (
    base_gcmessages_pb2,
    gcsdk_gcmessages_pb2,
    dota_gcmessages_common_pb2,
    dota_gcmessages_client_pb2,
    dota_gcmessages_client_chat_pb2,
    dota_gcmessages_client_fantasy_pb2,
    dota_gcmessages_client_guild_pb2,
    dota_gcmessages_client_match_management_pb2,
    dota_gcmessages_client_team_pb2,
    dota_gcmessages_client_tournament_pb2,
    dota_gcmessages_client_watch_pb2,
    econ_gcmessages_pb2,
)


def get_emsg_enum(emsg):
    """
    Attempts to find the Enum for the given :class:`int`

    :param emsg: integer corresponding to a Enum
    :type emsg: :class:`int`
    :return: Enum if found, `emsg` if not
    :rtype: Enum, :class:`int`
    """
    for enum in (EGCBaseClientMsg,
                 EDOTAGCMsg,
                 ESOMsg,
                 EGCBaseMsg,
                 EGCItemMsg,
                 ):
        try:
            return enum(emsg)
        except ValueError:
            pass

    return emsg


def find_proto(emsg):
    """
    Attempts to find the protobuf message for a given Enum

    :param emsg: Enum corrensponding to a protobuf message
    :type emsg: `Enum`
    :return: protobuf message class
    """

    if type(emsg) is int:
        return None

    if emsg in _proto_lookup_map:
        return _proto_lookup_map.get(emsg)

    if isinstance(emsg, ESOMsg):
        proto = _proto_lookup_map[emsg] = getattr(gcsdk_gcmessages_pb2, "CMsgSO%s" % emsg.name, None)
        return proto

    for module in (base_gcmessages_pb2,
                   gcsdk_gcmessages_pb2,
                   dota_gcmessages_common_pb2,
                   dota_gcmessages_client_pb2,
                   dota_gcmessages_client_chat_pb2,
                   dota_gcmessages_client_fantasy_pb2,
                   dota_gcmessages_client_guild_pb2,
                   dota_gcmessages_client_match_management_pb2,
                   dota_gcmessages_client_team_pb2,
                   dota_gcmessages_client_tournament_pb2,
                   dota_gcmessages_client_watch_pb2,
                   econ_gcmessages_pb2,
                  ):

        proto = getattr(module, emsg.name.replace("EMsg", "CMsg"), None)

        if proto is None:
            proto = getattr(module, emsg.name.replace("EMsgGC", "CMsgDOTA"), None)
        if proto is None:
            proto = getattr(module, emsg.name.replace("EMsgGCToClient", "CMsgDOTA"), None)
        if proto is None:
            proto = getattr(module, emsg.name.replace("EMsgGCToClient", "CMsg"), None)
        if proto is None:
            proto = getattr(module, emsg.name.replace("EMsgGC", "CMsg"), None)
        if proto is None:
            proto = getattr(module, emsg.name.replace("EMsgDOTA", "CMsg"), None)
        if proto is None:
            proto = getattr(module, emsg.name.replace("EMsg", "CMsgDOTA"), None)

        if proto is not None:
            _proto_lookup_map[emsg] = proto
            break

    return proto


_proto_lookup_map = {
    EGCBaseClientMsg.EMsgGCClientConnectionStatus: gcsdk_gcmessages_pb2.CMsgConnectionStatus,
    EDOTAGCMsg.EMsgClientToGCGetProfileCardResponse: dota_gcmessages_common_pb2.CMsgDOTAProfileCard,
    EDOTAGCMsg.EMsgClientToGCLatestConductScorecardRequest: dota_gcmessages_client_pb2.CMsgPlayerConductScorecardRequest,
    EDOTAGCMsg.EMsgClientToGCLatestConductScorecard: dota_gcmessages_client_pb2.CMsgPlayerConductScorecard,
    ESOMsg.Create: gcsdk_gcmessages_pb2.CMsgSOSingleObject,
    ESOMsg.Update: gcsdk_gcmessages_pb2.CMsgSOSingleObject,
    ESOMsg.Destroy: gcsdk_gcmessages_pb2.CMsgSOSingleObject,
    ESOMsg.UpdateMultiple: gcsdk_gcmessages_pb2.CMsgSOMultipleObjects,
    EDOTAGCMsg.EMsgClientToGCEventGoalsRequest: dota_gcmessages_client_pb2.CMsgClientToGCGetEventGoals,
    EDOTAGCMsg.EMsgClientToGCEventGoalsResponse: dota_gcmessages_client_pb2.CMsgEventGoals,
    EDOTAGCMsg.EMsgClientToGCSetPartyLeader: dota_gcmessages_client_match_management_pb2.CMsgDOTASetGroupLeader,
    EDOTAGCMsg.EMsgGCOtherJoinedChannel: dota_gcmessages_client_chat_pb2.CMsgDOTAOtherJoinedChatChannel,
    EDOTAGCMsg.EMsgGCOtherLeftChannel: dota_gcmessages_client_chat_pb2.CMsgDOTAOtherLeftChatChannel,
}
