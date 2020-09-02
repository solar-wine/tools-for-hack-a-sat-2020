#!/bin/bash
# Dependencies for Ubuntu 20.04:
#   apt install -y bison build-essential flex libglib2.0-dev libpixman-1-dev pkg-config python3

set -e

CUR_DIR="$(readlink -f "$0")"
BASE_DIR="$(dirname "$CUR_DIR")"

QEMU_DIR="${BASE_DIR}/qemu-4.1.0"
QEMU_BIN="${QEMU_DIR}/sparc-softmmu/qemu-system-sparc"

if [ $# -lt 1 ]
then
    echo "USAGE: \"$0\" <kernel file> [extra qemu options]"
    echo "  Note that extra options can be something like -gdb tcp::1234"
    exit 1
fi

if [ ! -f "${QEMU_BIN}" ]
then
    echo "QEMU need to be compiled !"
    echo "Configuring QEMU for SPARC..."
    (cd "${QEMU_DIR}" && ./configure --target-list=sparc-softmmu --enable-debug)
    echo "Compiling QEMU..."
    if ! make -C "${QEMU_DIR}"
    then
        echo "Something went wrong while compiling QEMU"
        exit 1
    fi
fi

echo "Launching QEMU..."
echo "Exit with C-a X or launch the monitoring console with C-a C"
echo ""

"${QEMU_BIN}" -no-reboot -nographic -M leon3_generic -m 512M \
    -monitor "unix:${BASE_DIR}/monitor.sock,server,nowait" \
    -serial stdio \
    -serial "unix:${BASE_DIR}/radio.sock,server,nowait" \
    -serial "unix:${BASE_DIR}/atmega.sock,server,nowait" \
    -kernel "$@" \
    || exit $?

# To interact with the radio interface, use the radio.sock Unix socket:
#   ../scapy-space-packets/ccsds_scapy_protocol.py -sx radio.sock
#
# To interact with the C&DH interface, use the atmega.sock Unix socket
# To interact with QEMU monitor, use: socat STDIO,cfmakeraw,isig=1 UNIX:monitor.sock
