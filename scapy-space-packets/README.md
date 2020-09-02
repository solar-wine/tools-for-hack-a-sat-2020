# Scapy Implementation of CCSDS Space Packet Protocol for Hack-A-Sat final event

This directory contains a full-Python implementation of CCSDS Space Packet Protocol, specified in <https://web.archive.org/web/20180911191526/https://public.ccsds.org/Pubs/133x0b1c2.pdf>.

It requires Python>=3.6 (to use f-strings) with the following packages:

* [`scapy`](https://scapy.net/)
* [`ipython`](https://ipython.org/)

## Usage with a QEMU virtual machine

When using the QEMU virtual machine from [`qemu-vm/`](../qemu-vm), the radio interface receives and transmits packets from the Unix socket file `radio.sock`.
To connect to it, [`client.py`](./client.py) can be used with option `-x`.
The protocol prefixes packets with a synchronization pattern, which is enabled in [`client.py`](./client.py) through option `-s`.

So the following command can be used:
```sh
./client.py -x ../qemu-vm/radio.sock -s
```

Instead of using a Unix socket, it is possible to connect to a TCP socket (for example QEMU options were modified to use a TCP socket instead of a Unix socket to implement the serial connection):
```sh
./client.py -t 127.0.0.1:54321 -s
```

If the client succeeds in connecting to the virtual machine, it will display a packet that enables the telemetry and an IPython prompt, followed by some messages that are received:
```text
Waiting before sending 12 bytes (last recv was 0.00078475201735273 second ago)
Sending 12 bytes: deadbeef19d7c000000107f7

Python 3.8.5 (default, Jul 27 2020, 08:42:51) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.17.0 -- An enhanced Interactive Python. Type '?' for help.

[< CFE_EVS_LONG_EVENT_MSG=0x8 0x5a] [42/3/UART_TO_CI 2.126] Telemetry output enabled for /dev/console_b
[< CFE_EVS_LONG_EVENT_MSG=0x8 0x5b] [42/3/KIT_SCH 3.137] Slots skipped: slot = 2, count = 3
In [1]:
```

Some functions were implemented to send specific packets.
For example:

* `ls("/cf")` sends a `FM SEND_DIR_PKT` command to the File Manager in order to enumerate the content of a directory.
* `file_play_cfdp("/cf/cfe_es_startup.scr")` sends a `CF PLAYBACK_FILE` command to the CFDP application (CCSDS File Delivery Protocol) in order to retrieve the content of a file (such as the startup script here).
* `file_upload_cfdp("/cf/test", b"Hello, world!")` writes bytes to a remote file using the CFDP protocol.

Please read `client.py` to find out more functions that were implemented.

## Usage with COSMOS

When using COSMOS (<https://cosmosrb.com/>) to connect to the virtual machine or a real FlatSat, it is possible to transmit packets through COSMOS thanks to a chaining documented in <https://cosmosrb.com/docs/chaining/>.
The protocol which is used, called "COSMOS PREIDENTIFIED protocol", encapsulates packets both from the CCSDS Space Packet Protocol and from Cosmos's internal components.
By default, COSMOS starts on `127.0.0.1:7779` a *packet router* which implements this protocol.

The following command connects to this router:
```sh
./client.py -c 127.0.0.1:7779
```

The same commands as when interacting with the virtual machine directly can be used.
