"""
Various utility function for dealing with messages.

"""

from dota2.enums import EGCBaseClientMsg, EDOTAGCMsg
from dota2.protobufs import gcsdk_gcmessages_pb2
from dota2.protobufs import dota_gcmessages_common_pb2
from dota2.protobufs import dota_gcmessages_client_pb2
from dota2.protobufs import dota_gcmessages_client_fantasy_pb2


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

    proto = _proto_map_why_cant_we_name_things_properly.get(emsg, None)

    if proto is not None:
        return proto

    for module in (gcsdk_gcmessages_pb2,
                   dota_gcmessages_common_pb2,
                   dota_gcmessages_client_pb2,
                   dota_gcmessages_client_fantasy_pb2,
                  ):

        proto = getattr(module, emsg.name.replace("EMsg", "CMsg"), None)

        if proto is None:
            proto = getattr(module, emsg.name.replace("EMsgGC", "CMsgDOTA"), None)
        if proto is None:
            proto = getattr(module, emsg.name.replace("EMsgGC", "CMsg"), None)


        if proto is not None:
            break

    return proto


_proto_map_why_cant_we_name_things_properly = {
    EGCBaseClientMsg.EMsgGCClientConnectionStatus: gcsdk_gcmessages_pb2.CMsgConnectionStatus,
    EDOTAGCMsg.EMsgClientToGCGetProfileCardResponse: dota_gcmessages_common_pb2.CMsgDOTAProfileCard,
    EDOTAGCMsg.EMsgClientToGCLatestConductScorecardRequest: dota_gcmessages_client_pb2.CMsgPlayerConductScorecardRequest,
    EDOTAGCMsg.EMsgClientToGCLatestConductScorecard: dota_gcmessages_client_pb2.CMsgPlayerConductScorecard,

}
