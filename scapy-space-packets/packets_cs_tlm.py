from scapy.all import *
from ccsds_base import CCSDSPacket


class CS_HK_TLM_PKT_TlmPkt(Packet):
    """Housekeeping Packet Structure

    app = CS
    command = HK_TLM_PKT
    msg_id = CS_HK_TLM_MID = 0x08a4 = 0x0800 + 0x0a4
    """
    name = "CS_HK_TLM_PKT_TlmPkt"
    fields_desc = [
        # APPEND_ITEM CMD_VALID_COUNT 8 UINT "CS Application Command Counter."
        ByteField("CMD_VALID_COUNT", 0),
        # APPEND_ITEM CMD_ERROR_COUNT 8 UINT "CS Application Command Error Counter."
        ByteField("CMD_ERROR_COUNT", 0),
        # APPEND_ITEM CHECKSUMSTATE 8 UINT "CS Application global checksum state."
        ByteField("CHECKSUMSTATE", 0),
        # APPEND_ITEM EEPROMCSSTATE 8 UINT "CS Eeprom table checksum stat e."
        ByteField("EEPROMCSSTATE", 0),
        # APPEND_ITEM MEMORYCSSTATE 8 UINT "CS Memory table checksum state."
        ByteField("MEMORYCSSTATE", 0),
        # APPEND_ITEM APPCSSTATE 8 UINT "CS App table checksum state."
        ByteField("APPCSSTATE", 0),
        # APPEND_ITEM TABLESCSSTATE 8 UINT "CS Tables table checksum stat e."
        ByteField("TABLESCSSTATE", 0),
        # APPEND_ITEM OSCSSTATE 8 UINT "OS code segment checksum state."
        ByteField("OSCSSTATE", 0),
        # APPEND_ITEM CFECORECSSTATE 8 UINT "cFE Core code segment checksum stat e"
        ByteField("CFECORECSSTATE", 0),
        # APPEND_ITEM CHILDTASKINUSE 8 UINT "CS 'Child Task In Use' flag."
        ByteField("CHILDTASKINUSE", 0),
        # APPEND_ITEM ONESHOTTASKINUSE 8 UINT "CS 'OneShot Task In Use' flag."
        ByteField("ONESHOTTASKINUSE", 0),
        # APPEND_ITEM FILLER8 8 UINT "8 bit padding"
        ByteField("FILLER8", 0),
        # APPEND_ITEM EEPROMCSERRCOUNTER 16 UINT "Eeprom miscompare counte r."
        ShortField("EEPROMCSERRCOUNTER", 0),
        # APPEND_ITEM MEMORYCSERRCOUNTER 16 UINT "Memory miscompare counter."
        ShortField("MEMORYCSERRCOUNTER", 0),
        # APPEND_ITEM APPCSERRCOUNTER 16 UINT "App miscompare counter."
        ShortField("APPCSERRCOUNTER", 0),
        # APPEND_ITEM TABLESCSERRCOUNTER 16 UINT "Tables miscompare counter."
        ShortField("TABLESCSERRCOUNTER", 0),
        # APPEND_ITEM CFECORECSERRCOUNTER 16 UINT "cFE core miscompare counter"
        ShortField("CFECORECSERRCOUNTER", 0),
        # APPEND_ITEM OSCSERRCOUNTER 16 UINT "OS code segment miscopmare counter."
        ShortField("OSCSERRCOUNTER", 0),
        # APPEND_ITEM CURRENTCSTABLE 16 UINT "Current table being checksummed."
        ShortField("CURRENTCSTABLE", 0),
        # APPEND_ITEM CURRENTENTRYINTABLE 16 UINT "Current entry ID in the table being checksummed."
        ShortField("CURRENTENTRYINTABLE", 0),
        # APPEND_ITEM EEPROMBASELINE 32 UINT "Baseline checksum for all of Eeprom."
        IntField("EEPROMBASELINE", 0),
        # APPEND_ITEM OSBASELINE 32 UINT "Baseline checksum for the OS code segment."
        IntField("OSBASELINE", 0),
        # APPEND_ITEM CFECOREBASELINE 32 UINT "Basline checksum for the cFE core."
        IntField("CFECOREBASELINE", 0),
        # APPEND_ITEM LASTONESHOTADDRESS 32 UINT "Address used in last one shot checksum command."
        IntField("LASTONESHOTADDRESS", 0),
        # APPEND_ITEM LASTONESHOTSIZE 32 UINT "Size used in the last one shot checksum command."
        IntField("LASTONESHOTSIZE", 0),
        # APPEND_ITEM LASTONESHOTCHECKSUM 32 UINT "Checksum of the last one shot checksum command."
        IntField("LASTONESHOTCHECKSUM", 0),
        # APPEND_ITEM PASSCOUNTER 32 UINT "Number of times CS has passed through all of its tables."
        IntField("PASSCOUNTER", 0),
    ]


bind_layers(CCSDSPacket, CS_HK_TLM_PKT_TlmPkt, pkttype=0, apid=164)
