from scapy.all import *
from ccsds_base import CCSDSPacket


class MM_NOOP_CmdPkt(Packet):
    """Generate an info event message with app version

    app = MM
    command = NOOP
    msg_id = MM_CMD_MID = 0x1888 = 0x1800 + 0x088
    cmd_func_code = 0
    data_len = 0 bytes
    """
    name = "MM_NOOP_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, MM_NOOP_CmdPkt, pkttype=1, apid=136, cmd_func_code=0)


class MM_RESET_CTRS_CmdPkt(Packet):
    """Reset command counters

    app = MM
    command = RESET_CTRS
    msg_id = MM_CMD_MID = 0x1888 = 0x1800 + 0x088
    cmd_func_code = 1
    data_len = 0 bytes
    """
    name = "MM_RESET_CTRS_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, MM_RESET_CTRS_CmdPkt, pkttype=1, apid=136, cmd_func_code=1)


class MM_PEEK_MEM_CmdPkt(Packet):
    """Reads 8,16, or 32 bits of data from any given input address

    app = MM
    command = PEEK_MEM
    msg_id = MM_CMD_MID = 0x1888 = 0x1800 + 0x088
    cmd_func_code = 2
    data_len = 72 bytes
    """
    name = "MM_PEEK_MEM_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER DATA_SIZE          8 UINT MIN_UINT8 MAX_UINT8   8   "Bit size of the data to be read: 8, 16, or 32"
        ByteField("DATA_SIZE", 8),
        # APPEND_PARAMETER MEM_TYPE           8 UINT MIN_UINT8 MAX_UINT8   1   "0=No Type, 1=RAM, 2=EEPROM"
        ByteField("MEM_TYPE", 1),
        # APPEND_PARAMETER PAD_16            16 UINT MIN_UINT8 MAX_UINT8   0   "Structure padding"
        ShortField("PAD_16", 0),
        # APPEND_PARAMETER ADDR_OFFSET       32 UINT MIN_UINT32 MAX_UINT32 0   "Offset from symbol or absolute address if no symbol specified"
        IntField("ADDR_OFFSET", 0),
        # APPEND_PARAMETER ADDR_SYMBOL_NAME 512 STRING default "Symbol to be used as base address or empty string if no symbol"
        StrFixedLenField("ADDR_SYMBOL_NAME", b"default", 64),
    ]


bind_layers(CCSDSPacket, MM_PEEK_MEM_CmdPkt, pkttype=1, apid=136, cmd_func_code=2)


class MM_POKE_MEM_CmdPkt(Packet):
    """Writes 8, 16, or 32 bits of data to any memory address

    app = MM
    command = POKE_MEM
    msg_id = MM_CMD_MID = 0x1888 = 0x1800 + 0x088
    cmd_func_code = 3
    data_len = 76 bytes
    """
    name = "MM_POKE_MEM_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER DATA_SIZE          8 UINT MIN_UINT8 MAX_UINT8 8     "Bit size of the data to be written: 8, 16, or 32"
        ByteField("DATA_SIZE", 8),
        # APPEND_PARAMETER MEM_TYPE           8 UINT MIN_UINT8 MAX_UINT8 1     "0=No Type, 1=RAM, 2=EEPROM"
        ByteField("MEM_TYPE", 1),
        # APPEND_PARAMETER PAD_16            16 UINT MIN_UINT8 MIN_UINT8 0     "Structure padding"
        ShortField("PAD_16", 0),
        # APPEND_PARAMETER DATA              32 UINT MIN_UINT32 MAX_UINT32 0   "Data to be written"
        IntField("DATA", 0),
        # APPEND_PARAMETER ADDR_OFFSET       32 UINT MIN_UINT32 MAX_UINT32 0   "Offset from symbol or absolute address if no symbol specified"
        IntField("ADDR_OFFSET", 0),
        # APPEND_PARAMETER ADDR_SYMBOL_NAME 512 STRING default "Symbol to be used as base address or empty string if no symbol"
        StrFixedLenField("ADDR_SYMBOL_NAME", b"default", 64),
    ]


bind_layers(CCSDSPacket, MM_POKE_MEM_CmdPkt, pkttype=1, apid=136, cmd_func_code=3)


class MM_LOAD_MEM_WID_CmdPkt(Packet):
    """Load processor memory with interrupts disabled. Loads up to MM_MAX_UNINTERRUPTABLE_DATA data bytes into RAM with interrupts disabled

    app = MM
    command = LOAD_MEM_WID
    msg_id = MM_CMD_MID = 0x1888 = 0x1800 + 0x088
    cmd_func_code = 4
    data_len = 276 bytes
    """
    name = "MM_LOAD_MEM_WID_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER NUM_BYTES          8 UINT MIN_UINT8  MAX_UINT8  0   "Number of bytes to be loaded"
        ByteField("NUM_BYTES", 0),
        # APPEND_PARAMETER PAD_8              8 UINT MIN_UINT8 MAX_UINT8   0   "Structure padding"
        ByteField("PAD_8", 0),
        # APPEND_PARAMETER PAD_16            16 UINT MIN_UINT16 MAX_UINT16 0   "Structure padding"
        ShortField("PAD_16", 0),
        # APPEND_PARAMETER CRC               32 UINT MIN_UINT32 MAX_UINT32 0   "Data check value"
        IntField("CRC", 0),
        # APPEND_PARAMETER ADDR_OFFSET       32 UINT MIN_UINT32 MAX_UINT32 0   "Offset from symbol or absolute address if no symbol specified"
        IntField("ADDR_OFFSET", 0),
        # APPEND_PARAMETER ADDR_SYMBOL_NAME 512 STRING default "Symbol to be used as base address or empty string if no symbol"
        StrFixedLenField("ADDR_SYMBOL_NAME", b"default", 64),
        # APPEND_ARRAY_PARAMETER DATA_ARRAY   8 UINT 1600                      "Data to be loaded"
        StrFixedLenField("DATA_ARRAY", b"", 200),
    ]


bind_layers(CCSDSPacket, MM_LOAD_MEM_WID_CmdPkt, pkttype=1, apid=136, cmd_func_code=4)


class MM_LOAD_MEM_FROM_FILE_CmdPkt(Packet):
    """Loads a contiguous block of memory using the data in teh specified file

    app = MM
    command = LOAD_MEM_FROM_FILE
    msg_id = MM_CMD_MID = 0x1888 = 0x1800 + 0x088
    cmd_func_code = 5
    data_len = 64 bytes
    """
    name = "MM_LOAD_MEM_FROM_FILE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER FILENAME 512 STRING "default" "FSW /path/filename of memory load file"
        StrFixedLenField("FILENAME", b"default", 64),
    ]


bind_layers(CCSDSPacket, MM_LOAD_MEM_FROM_FILE_CmdPkt, pkttype=1, apid=136, cmd_func_code=5)


class MM_DUMP_MEM_TO_FILE_CmdPkt(Packet):
    """Dumps the input number of bytes from processor memory to a file

    app = MM
    command = DUMP_MEM_TO_FILE
    msg_id = MM_CMD_MID = 0x1888 = 0x1800 + 0x088
    cmd_func_code = 6
    data_len = 140 bytes
    """
    name = "MM_DUMP_MEM_TO_FILE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER MEM_TYPE           8 UINT MIN_UINT8 MAX_UINT8   1 "0=No Type, 1=RAM, 2=EEPROM"
        ByteField("MEM_TYPE", 1),
        # APPEND_PARAMETER PAD_8              8 UINT MIN_UINT8 MAX_UINT8   0 "Structure padding"
        ByteField("PAD_8", 0),
        # APPEND_PARAMETER PAD_16            16 UINT MIN_UINT16 MAX_UINT16 0 "Structure padding"
        ShortField("PAD_16", 0),
        # APPEND_PARAMETER NUM_BYTES         32 UINT MIN_UINT32 MAX_UINT32 0 "Number of bytes to fill"
        IntField("NUM_BYTES", 0),
        # APPEND_PARAMETER ADDR_OFFSET       32 UINT MIN_UINT32 MAX_UINT32 0 "Offset from symbol or absolute address if no symbol specified"
        IntField("ADDR_OFFSET", 0),
        # APPEND_PARAMETER ADDR_SYMBOL_NAME 512 STRING "default" "Symbol to be used as base address or empty string if no symbol"
        StrFixedLenField("ADDR_SYMBOL_NAME", b"default", 64),
        # APPEND_PARAMETER FILENAME         512 STRING "default" "FSW /path/filename of memory dump file."
        StrFixedLenField("FILENAME", b"default", 64),
    ]


bind_layers(CCSDSPacket, MM_DUMP_MEM_TO_FILE_CmdPkt, pkttype=1, apid=136, cmd_func_code=6)


class MM_DUMP_IN_EVENT_CmdPkt(Packet):
    """Dumps up to MM_MAX_DUMP_INEVENT_BYTES of memory in an event message

    app = MM
    command = DUMP_IN_EVENT
    msg_id = MM_CMD_MID = 0x1888 = 0x1800 + 0x088
    cmd_func_code = 7
    data_len = 72 bytes
    """
    name = "MM_DUMP_IN_EVENT_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER MEM_TYPE           8 UINT MIN_UINT8 MAX_UINT8   1 "0=No Type, 1=RAM, 2=EEPROM"
        ByteField("MEM_TYPE", 1),
        # APPEND_PARAMETER NUM_BYTES          8 UINT MIN_UINT8 16          0 "Number of bytes to be dumped (max 16)"
        ByteField("NUM_BYTES", 0),
        # APPEND_PARAMETER PAD_16            16 UINT MIN_UINT16 MAX_UINT16 0 "Structure padding"
        ShortField("PAD_16", 0),
        # APPEND_PARAMETER ADDR_OFFSET       32 UINT MIN_UINT32 MAX_UINT32 0 "Offset from symbol or absolute address if no symbol specified"
        IntField("ADDR_OFFSET", 0),
        # APPEND_PARAMETER ADDR_SYMBOL_NAME 512 STRING "default"             "Symbol to be used as base address or empty string if no symbol"
        StrFixedLenField("ADDR_SYMBOL_NAME", b"default", 64),
    ]


bind_layers(CCSDSPacket, MM_DUMP_IN_EVENT_CmdPkt, pkttype=1, apid=136, cmd_func_code=7)


class MM_FILL_MEM_CmdPkt(Packet):
    """Load a contiguous block of memory with a fill pattern

    app = MM
    command = FILL_MEM
    msg_id = MM_CMD_MID = 0x1888 = 0x1800 + 0x088
    cmd_func_code = 8
    data_len = 80 bytes
    """
    name = "MM_FILL_MEM_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER MEM_TYPE           8 UINT MIN_UINT8 MAX_UINT8 1 "0=No Type, 1=RAM, 2=EEPROM"
        ByteField("MEM_TYPE", 1),
        # APPEND_PARAMETER PAD_8              8 UINT MIN_UINT8 MAX_UINT8 0 "Structure padding"
        ByteField("PAD_8", 0),
        # APPEND_PARAMETER PAD_16            16 UINT MIN_UINT16 MAX_UINT16 0 "Structure padding"
        ShortField("PAD_16", 0),
        # APPEND_PARAMETER NUM_BYTES         32 UINT MIN_UINT32 MAX_UINT32 0 "Number of bytes to fill"
        IntField("NUM_BYTES", 0),
        # APPEND_PARAMETER FILL_PATTERN      32 UINT MIN_UINT32 MAX_UINT32 0 "Fill pattern to use"
        IntField("FILL_PATTERN", 0),
        # APPEND_PARAMETER ADDR_OFFSET       32 UINT MIN_UINT32 MAX_UINT32 0 "Offset from symbol or absolute address if no symbol specified"
        IntField("ADDR_OFFSET", 0),
        # APPEND_PARAMETER ADDR_SYMBOL_NAME 512 STRING "default" "Symbol to be used as base address or empty string if no symbol"
        StrFixedLenField("ADDR_SYMBOL_NAME", b"default", 64),
    ]


bind_layers(CCSDSPacket, MM_FILL_MEM_CmdPkt, pkttype=1, apid=136, cmd_func_code=8)


class MM_LOOKUP_SYMBOL_CmdPkt(Packet):
    """Queries the system symbol table and reports the resolved address in telemetry and an informational event message

    app = MM
    command = LOOKUP_SYMBOL
    msg_id = MM_CMD_MID = 0x1888 = 0x1800 + 0x088
    cmd_func_code = 9
    data_len = 64 bytes
    """
    name = "MM_LOOKUP_SYMBOL_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER SYMBOL_NAME 512 STRING "default" "Symbol name string"
        StrFixedLenField("SYMBOL_NAME", b"default", 64),
    ]


bind_layers(CCSDSPacket, MM_LOOKUP_SYMBOL_CmdPkt, pkttype=1, apid=136, cmd_func_code=9)


class MM_SYMBOLTBL_TO_FILE_CmdPkt(Packet):
    """Saves the system symbol table to a file that can be transfered to the ground

    app = MM
    command = SYMBOLTBL_TO_FILE
    msg_id = MM_CMD_MID = 0x1888 = 0x1800 + 0x088
    cmd_func_code = 10
    data_len = 64 bytes
    """
    name = "MM_SYMBOLTBL_TO_FILE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER FILENAME 512 STRING "default" "FSW /path/filename of symbol dump file"
        StrFixedLenField("FILENAME", b"default", 64),
    ]


bind_layers(CCSDSPacket, MM_SYMBOLTBL_TO_FILE_CmdPkt, pkttype=1, apid=136, cmd_func_code=10)


class MM_ENA_EEPROM_WRITE_CmdPkt(Packet):
    """Enables writing to a specified EEPROM bank

    app = MM
    command = ENA_EEPROM_WRITE
    msg_id = MM_CMD_MID = 0x1888 = 0x1800 + 0x088
    cmd_func_code = 11
    data_len = 4 bytes
    """
    name = "MM_ENA_EEPROM_WRITE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER BANK 32 UINT MIN_UINT32 MAX_UINT32 0 "EEPROM bank number to write-enable"
        IntField("BANK", 0),
    ]


bind_layers(CCSDSPacket, MM_ENA_EEPROM_WRITE_CmdPkt, pkttype=1, apid=136, cmd_func_code=11)


class MM_DIS_EEPROM_WRITE_CmdPkt(Packet):
    """Disables writing to a specified EEPROM bank

    app = MM
    command = DIS_EEPROM_WRITE
    msg_id = MM_CMD_MID = 0x1888 = 0x1800 + 0x088
    cmd_func_code = 12
    data_len = 4 bytes
    """
    name = "MM_DIS_EEPROM_WRITE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER BANK 32 UINT MIN_UINT32 MAX_UINT32 0 "EEPROM bank number to write-disable"
        IntField("BANK", 0),
    ]


bind_layers(CCSDSPacket, MM_DIS_EEPROM_WRITE_CmdPkt, pkttype=1, apid=136, cmd_func_code=12)
