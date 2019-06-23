#!/usr/bin/env python

import re
from keyword import kwlist
from google.protobuf.internal.enum_type_wrapper import EnumTypeWrapper

kwlist = set(kwlist + ['None'])

_proto_modules = [
    'base_gcmessages_pb2',
    'dota_client_enums_pb2',
    'dota_gcmessages_client_pb2',
    'dota_gcmessages_client_fantasy_pb2',
    'dota_gcmessages_client_match_management_pb2',
    'dota_gcmessages_client_team_pb2',
    'dota_gcmessages_client_tournament_pb2',
    'dota_gcmessages_common_pb2',
    'dota_gcmessages_common_match_management_pb2',
    'dota_gcmessages_msgid_pb2',
    'dota_shared_enums_pb2',
    'gcsdk_gcmessages_pb2',
    'gcsystemmsgs_pb2',
    'steammessages_pb2',
    'econ_gcmessages_pb2',
    'econ_shared_enums_pb2',
]

_proto_module = __import__("dota2.protobufs", globals(), locals(), _proto_modules, 0)

classes = []

print("from enum import IntEnum")

for name in _proto_modules:

    proto = getattr(_proto_module, name)
    gvars = globals()

    for class_name, value in proto.__dict__.items():
        if not isinstance(value, EnumTypeWrapper):
            continue

        classes.append(class_name)
        attrs_starting_with_number = False
        attrs = {}

        for ikey, ivalue in value.items():
            ikey = re.sub(r'^(k_)?(%s_)?' % class_name, '', ikey)
            attrs[ikey] = ivalue

            if ikey[0:1].isdigit() or ikey in kwlist:
                attrs_starting_with_number = True

        if attrs_starting_with_number:
            print("\n%s = IntEnum(%r, {" % (class_name, class_name))
            for ikey, ivalue in attrs.items():
                print("    %r: %r," % (ikey, ivalue))
            print("    })")
        else:
            print("\nclass {class_name}(IntEnum):".format(class_name=class_name))
            for ikey, ivalue in attrs.items():
                print("    {} = {}".format(ikey, ivalue))

print("\n__all__ = [")

for name in classes:
    print("    %r," % name)

print("    ]")
