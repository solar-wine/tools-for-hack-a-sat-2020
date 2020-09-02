from scapy.all import *
from ccsds_base import CCSDSPacket


class MD_NOOP_CmdPkt(Packet):
    """Generate an info event message with app version

    app = MD
    command = NOOP
    msg_id = MD_CMD_MID = 0x1890 = 0x1800 + 0x090
    cmd_func_code = 0
    data_len = 0 bytes
    """
    name = "MD_NOOP_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, MD_NOOP_CmdPkt, pkttype=1, apid=144, cmd_func_code=0)


class MD_RESET_CTRS_CmdPkt(Packet):
    """Reset command counters

    app = MD
    command = RESET_CTRS
    msg_id = MD_CMD_MID = 0x1890 = 0x1800 + 0x090
    cmd_func_code = 1
    data_len = 0 bytes
    """
    name = "MD_RESET_CTRS_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, MD_RESET_CTRS_CmdPkt, pkttype=1, apid=144, cmd_func_code=1)


class MD_START_DWELL_CmdPkt(Packet):
    """Set the Enabled flag(s) specified by Table Mask argument

    app = MD
    command = START_DWELL
    msg_id = MD_CMD_MID = 0x1890 = 0x1800 + 0x090
    cmd_func_code = 2
    data_len = 2 bytes
    """
    name = "MD_START_DWELL_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER TABLE_MASK 16 UINT MIN_UINT16 MAX_UINT16 0 "0x0001=TBL1 bit, 0x0002=TBL2 bit,0x0004=TBL3 bit,0x0008=TBL4 enable bit, etc."
        ShortField("TABLE_MASK", 0),
    ]


bind_layers(CCSDSPacket, MD_START_DWELL_CmdPkt, pkttype=1, apid=144, cmd_func_code=2)


class MD_STOP_DWELL_CmdPkt(Packet):
    """Clear the Enabled flag(s) specified by Table Mask argument.

    app = MD
    command = STOP_DWELL
    msg_id = MD_CMD_MID = 0x1890 = 0x1800 + 0x090
    cmd_func_code = 3
    data_len = 2 bytes
    """
    name = "MD_STOP_DWELL_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER TABLE_MASK 16 UINT MIN_UINT16 MAX_UINT16 0 "0x0001=TBL1 bit, 0x0002=TBL2 bit,0x0004=TBL3 bit,0x0008=TBL4 enable bit, etc."
        ShortField("TABLE_MASK", 0),
    ]


bind_layers(CCSDSPacket, MD_STOP_DWELL_CmdPkt, pkttype=1, apid=144, cmd_func_code=3)


class MD_JAM_DWELL_CmdPkt(Packet):
    """Inserts dwell parameters (dwell address, dwell field length, and delay count) into specified table, at specified index.

    app = MD
    command = JAM_DWELL
    msg_id = MD_CMD_MID = 0x1890 = 0x1800 + 0x090
    cmd_func_code = 4
    data_len = 76 bytes
    """
    name = "MD_JAM_DWELL_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER TABLE_ID    16 UINT MIN_UINT16 MAX_UINT16 0 "Table Id: 1..MD_NUM_DWELL_TABLES"
        ShortField("TABLE_ID", 0),
        # APPEND_PARAMETER ENTRY_ID    16 UINT MIN_UINT16 MAX_UINT16 0 "Address index: 1..MD_DWELL_TABLE_SIZE"
        ShortField("ENTRY_ID", 0),
        # APPEND_PARAMETER FIELD_LEN   16 UINT MIN_UINT16 MAX_UINT16 0 "Length of Dwell Field : 0, 1, 2, or 4"
        ShortField("FIELD_LEN", 0),
        # APPEND_PARAMETER DELAY       16 UINT MIN_UINT16 MAX_UINT16 0 "Dwell Delay (number of task wakeup calls before following dwell)"
        ShortField("DELAY", 0),
        # APPEND_PARAMETER ADDR_OFFSET 32 UINT MIN_UINT32 MAX_UINT32 0 "Offset from symbol or absolute address if no symbol specified"
        IntField("ADDR_OFFSET", 0),
        # APPEND_PARAMETER ADDR_SYMBOL_NAME 512 STRING "default" "Symbol to be used as base address or empty string if no symbol"
        StrFixedLenField("ADDR_SYMBOL_NAME", b"default", 64),
    ]


bind_layers(CCSDSPacket, MD_JAM_DWELL_CmdPkt, pkttype=1, apid=144, cmd_func_code=4)


class MD_SET_SIGNATURE_CmdPkt(Packet):
    """Set signature text for a dwell table

    app = MD
    command = SET_SIGNATURE
    msg_id = MD_CMD_MID = 0x1890 = 0x1800 + 0x090
    cmd_func_code = 5
    data_len = 36 bytes
    """
    name = "MD_SET_SIGNATURE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER TABLE_ID   16 UINT 1 4 1 "1..MD_NUM_DWELL_TABLES"
        ShortField("TABLE_ID", 1),
        # APPEND_PARAMETER PAD_16     16 UINT MIN_UINT16 MAX_UINT16 0 "16 bit pad"
        ShortField("PAD_16", 0),
        # APPEND_PARAMETER SIGNATURE 256 STRING "undefined" "Character string to describe the dwell table"
        StrFixedLenField("SIGNATURE", b"undefined", 32),
    ]


bind_layers(CCSDSPacket, MD_SET_SIGNATURE_CmdPkt, pkttype=1, apid=144, cmd_func_code=5)
