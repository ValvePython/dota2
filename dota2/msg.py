from dota2.enums import EGCBaseClientMsg, EDOTAGCMsg
from dota2.protobufs import gcsdk_gcmessages_pb2
from dota2.protobufs import dota_gcmessages_client_pb2


def get_emsg_enum(emsg):
    for enum in (EGCBaseClientMsg,
                 EDOTAGCMsg,
                 ):
        try:
            return enum(emsg)
        except ValueError:
            pass

    return emsg

def find_proto(emsg):
    if type(emsg) is int:
        return None

    if emsg == EGCBaseClientMsg.EMsgGCClientConnectionStatus:
        return gcsdk_gcmessages_pb2.CMsgConnectionStatus

    for module in (gcsdk_gcmessages_pb2,
                   dota_gcmessages_client_pb2,
                  ):

        proto = getattr(module, emsg.name.replace("EMsgGC", "CMsg"), None)

        if proto is None:
            proto = getattr(module, emsg.name.replace("EMsgGC", "CMsgDOTA"), None)

        if proto is not None:
            break

    return proto
