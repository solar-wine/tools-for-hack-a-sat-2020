#!/usr/bin/env python3
from scapy.all import *
from ccsds_base import CCSDSPacket

IMP_MAGIC = bytes.fromhex("463b98fe1ee494bb")
IMP_CMD_ENUM = {
    1: "DUMP",
    2: "CHECK",
    3: "LOCK",
    4: "EXEC",
}
IMP_EXEC_SUBCMD_FLAGS_ENUM = {
    0: "memcpy type 0",
    1: "memcpy type 1",
    2: "memcpy type 2",
    3: "exec (3)"
}


class IMP_CmdPkt(Packet):
    name = "IMP_CmdPkt"
    fields_desc = [
        StrFixedLenField("MAGIC", IMP_MAGIC, len(IMP_MAGIC)),
        LEIntEnumField("IMP_CMD", 0, IMP_CMD_ENUM)
    ]


bind_layers(CCSDSPacket, IMP_CmdPkt, pkttype=1, apid=52)


class IMP_DUMP_SubPkt(Packet):
    fields_desc = [
        StrFixedLenField("SYMBOL", b'SCHEDULER_Execute', 64),
        XIntField("address", 0),
        IntField("size", 58),
    ]


bind_layers(IMP_CmdPkt, IMP_DUMP_SubPkt, IMP_CMD=1)


class IMP_CHECK_SubPkt(Packet):
    fields_desc = [
        StrFixedLenField("password", b'', 64),
    ]


bind_layers(IMP_CmdPkt, IMP_CHECK_SubPkt, IMP_CMD=2)


class IMP_LOCK_SubPkt(Packet):
    fields_desc = [
    ]


bind_layers(IMP_CmdPkt, IMP_LOCK_SubPkt, IMP_CMD=3)


class IMP_EXEC_SUBCOMMAND_Pkt(Packet):
    fields_desc = [
        BitFieldLenField("subcmd_size", None, 6, length_of="subcmd_blob", adjust=lambda pkt, x: x // 4),
        BitEnumField("subcmd_flags", 0, 2, IMP_EXEC_SUBCMD_FLAGS_ENUM),
        StrLenField("subcmd_blob", b"", length_from=lambda pkt: pkt.subcmd_size * 4)
    ]

    def extract_padding(self, s):
        return b"", s


class IMP_EXEC_SubPkt(Packet):
    fields_desc = [
        PacketListField("subcmds", None, cls=IMP_EXEC_SUBCOMMAND_Pkt),
    ]


bind_layers(IMP_CmdPkt, IMP_EXEC_SubPkt, IMP_CMD=4)


if __name__ == '__main__':
    # from pcap
    rawcmd = b'\x184\xc0\x00\x00U\x00=F;\x98\xfe\x1e\xe4\x94\xbb\x01\x00\x00\x00SCHEDULER_Execute\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xda\x00\x00\x00:'
    cmdpkt = CCSDSPacket(rawcmd)
    cmdpkt.show()
    assert cmdpkt.haslayer(IMP_CmdPkt)
    assert cmdpkt.haslayer(IMP_DUMP_SubPkt)
    assert len(cmdpkt) == 0x5c

    # "check" packet
    chkpkt = CCSDSPacket() / IMP_CmdPkt() / IMP_CHECK_SubPkt()
    assert len(chkpkt) == 0x54

    # "exec" packet
    subcmds = [
        IMP_EXEC_SUBCOMMAND_Pkt(subcmd_flags=0, subcmd_blob="1234"),
        IMP_EXEC_SUBCOMMAND_Pkt(subcmd_flags=0, subcmd_blob="16 BYTES COMMAND"),
    ]
    execpkt = CCSDSPacket() / IMP_CmdPkt() / IMP_EXEC_SubPkt(subcmds=subcmds)
    assert len(execpkt.subcmds) == 2
    execpkt.show2()
