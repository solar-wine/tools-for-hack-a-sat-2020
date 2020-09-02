"""Packets generated and handled by Cosmos software, not forwarded to the real satellite"""
from scapy.all import *


class SYSTEM_META_TlmPkt(Packet):
    """System Meta Data Telemetry Packet

    target name: SYSTEM
    packet name: META
    """
    name = "SYSTEM_META_TlmPkt"
    fields_desc = [
        # APPEND_ID_ITEM PKTID 8 UINT 1 "Packet Id"
        ByteField("PKT_ID", 1),
        # APPEND_ITEM CONFIG 256 STRING "Configuration Name"
        StrFixedLenField("CONFIG", b"", 32),
        # APPEND_ITEM COSMOS_VERSION 240 STRING "COSMOS Version"
        StrFixedLenField("COSMOS_VERSION", b"", 30),
        # APPEND_ITEM USER_VERSION 240 STRING "User Project Version"
        StrFixedLenField("USER_VERSION", b"", 30),
        # APPEND_ITEM RUBY_VERSION 240 STRING "Ruby Version"
        StrFixedLenField("RUBY_VERSION", b"", 30),
        # APPEND_ITEM OPERATOR_NAME 512 STRING "Operator Name"
        StrFixedLenField("OPERATOR_NAME", b"", 64),
    ]


class SYSTEM_LIMITS_CHANGE_TlmPkt(Packet):
    """COSMOS limits change

    target name: SYSTEM
    packet name: LIMITS_CHANGE
    """
    name = "SYSTEM_LIMITS_CHANGE_TlmPkt"
    fields_desc = [
        # APPEND_ID_ITEM PKT_ID 8 UINT 2 "Packet Id"
        ByteField("PKT_ID", 2),
        # APPEND_ITEM TARGET 240 STRING "Target name"
        StrFixedLenField("TARGET", b"", 30),
        # APPEND_ITEM PACKET 240 STRING "Packet name"
        StrFixedLenField("PACKET", b"", 30),
        # APPEND_ITEM ITEM 240 STRING "Item that changed limits state"
        StrFixedLenField("ITEM", b"", 30),
        # APPEND_ITEM OLD_STATE 240 STRING "The old limit state"
        StrFixedLenField("OLD_STATE", b"", 30),
        # APPEND_ITEM NEW_STATE 240 STRING "The new limit state"
        StrFixedLenField("NEW_STATE", b"", 30),
    ]
