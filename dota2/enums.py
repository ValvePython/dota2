"""
This module contains various :class:`enum.IntEnum` generated at runtime from protobufs.
Why generate python enums? In short, protobuf's enums aren't great.
:class:`enum.IntEnum` are much more flexible and easy to work with.
"""

import re
from enum import IntEnum
from google.protobuf.internal.enum_type_wrapper import EnumTypeWrapper

_proto_modules = ['gcsystemmsgs_pb2',
                 'gcsdk_gcmessages_pb2',
                 'dota_gcmessages_common_pb2',
                 'dota_gcmessages_client_pb2',
                  ]

_proto_module = __import__("dota2.protobufs", globals(), locals(), _proto_modules, -1)

for name in _proto_modules:

    proto = getattr(_proto_module, name)
    gvars = globals()

    for key, value in proto.__dict__.items():
        if not isinstance(value, EnumTypeWrapper):
            continue

        items = {}
        for ikey, ivalue in value.items():
            ikey = re.sub(r'^(k_)?(%s_)?' % key, '', ikey)
            items[ikey] = ivalue

        gvars[key] = IntEnum(key, items)

del re, IntEnum, EnumTypeWrapper, _proto_modules, _proto_module, name, proto, gvars, key, value, items, ikey, ivalue
