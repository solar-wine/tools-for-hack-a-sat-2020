#!/usr/bin/env python3
"""
doc: https://raw.githubusercontent.com/nasa/SC/master/docs/users_guide/CFS%20SC%20User%20Guide%20Doc%20No%20582-2012-003%20Ver%201.1%202014_12-18.pdf

Table specifications: https://github.com/nasa/SC/tree/master/fsw/tables

Table image examples: https://github.com/solar-wine/flatsat_data_firmware/tree/master/upgrade/cFS/modules
"""

from scapy.all import *
from ccsds_base import CCSDSPacket
from packets_eyassat_if_cmd import *


class ATC(Packet):
    """
    Absolute Time Command
    """
    fields_desc = [
        # unique number
        LEShortField("ID", 0),

        # seconds
        IntField("TimeTag", 0),
        ConditionalField(
            FCSField("Padding", 0, fmt="B"),
            lambda pkt: len(pkt.payload) % 2 != 0  # XXX check
        ),
    ]

    def extract_padding(self, s):
        tmp = CCSDSPacket(s)
        length = 8  # len(CCSDSPacket())
        length += tmp.pkt_length - 1
        if tmp.haslayer(Raw):
            print(f"Warning: unknown command apid={hex(tmp.apid)}")
        return s[:length], s[length:]


bind_layers(ATC, CCSDSPacket)


class ATSFile(Packet):
    name = "ATSFile"
    fields_desc = [
        # table name: SC.ATS_TBL1 or SC.ATS_TBL2
        # CFE_FS_Header_t from
        # https://github.com/nasa/cFE/blob/v6.7.0/fsw/cfe-core/src/inc/cfe_fs.h#L84
        StrFixedLenField('ContentType', 'cFE1', 4),
        IntField('SubType', 8),  # 8 is used
        IntField('Length', 0x40),  # Header length
        IntField('SpacecraftID', 0),
        IntField('ProcessorID', 0),
        IntField('ApplicationID', 0),
        IntField('TimeSeconds', 0),
        IntField('TimeSubSeconds', 0),
        StrFixedLenField('Description', 'SC Sample ATS_TBL1', 32),

        # CFE_TBL_File_Hdr_t from https://github.com/nasa/cFE/blob/v6.7.0/fsw/cfe-core/src/inc/cfe_tbl_filedef.h
        IntField('Reserved', 0),
        IntField('Offset', 0),
        IntField('NumBytes', 0),
        StrFixedLenField('TableName', 'SC.ATS_TBL1', 40),  # guess

        PacketListField("ATS", None, cls=ATC),
    ]


class RTC(Packet):
    """
    Relative Time Command
    doc: sc_rts*.c (https://github.com/nasa/SC/tree/master/fsw/tables)
    """
    fields_desc = [
        # seconds
        ShortField("TimeTag", 0),
    ]

    def extract_padding(self, s):
        tmp = CCSDSPacket(s)
        length = 8  # len(CCSDSPacket())
        length += tmp.pkt_length - 1
        if tmp.haslayer(Raw):
            print(f"Warning: unknown command apid={hex(tmp.apid)}")
        return s[:length], s[length:]


bind_layers(RTC, CCSDSPacket)


class RTSFile(Packet):
    name = "RTSFile"
    fields_desc = [
        # CFE_FS_Header_t from
        # https://github.com/nasa/cFE/blob/v6.7.0/fsw/cfe-core/src/inc/cfe_fs.h#L84
        StrFixedLenField('ContentType', 'cFE1', 4),
        IntField('SubType', 8),  # 8 is used
        IntField('Length', 0x40),  # Header length
        IntField('SpacecraftID', 0),
        IntField('ProcessorID', 0),
        IntField('ApplicationID', 0),
        IntField('TimeSeconds', 0),
        IntField('TimeSubSeconds', 0),
        StrFixedLenField('Description', 'SC Sample RTS_TBL001', 32),

        # CFE_TBL_File_Hdr_t from https://github.com/nasa/cFE/blob/v6.7.0/fsw/cfe-core/src/inc/cfe_tbl_filedef.h
        IntField('Reserved', 0),
        IntField('Offset', 0),
        IntField('NumBytes', 300),
        StrFixedLenField('TableName', 'SC.RTS_TBL001', 40),  # guess

        PacketListField("RTS", None, cls=RTC),
    ]


if __name__ == '__main__':
    RTCs = [
        # EYASSAT_IF_ADCS_PWM_BASELINE_CmdPkt
        RTC(TimeTag=0) / CCSDSPacket(apid=469, cmd_func_code=5) / EYASSAT_IF_ADCS_PWM_BASELINE_CmdPkt(PWM=0),
    ]
    image = RTSFile(RTS=RTCs)
    with open('stop_flywheel-rts.tbl', 'wb') as f:
        f.write(bytes(image))
        f.write(b'\x00' * 1000)
