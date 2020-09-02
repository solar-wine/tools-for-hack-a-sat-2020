# QEMU for emulating satellite firmware for Hack-A-Sat final event

## Setup

You need to download [QEMU 4.1.0](https://download.qemu.org/qemu-4.1.0.tar.xz) first, then decompress it in this folder:

```sh
tar xaf qemu-4.1.0.tar.xz
```
Apply the provided patches to recreate the satellite architecture and fix some bugs:

```sh
for patch in ./qemu-patches/*
do
    patch -p1 < "${patch}"
done
```

Finally, run the launch script, it will take care of the QEMU compilation:

```sh
./launch-qemu.sh <PROM file> [extra qemu options]
```

The debug UART will be directly available on `stdio` while the Radio and C&DH UART are available through Unix sockets: `radio.sock` and `atmega.sock`.

## Debugging

You need to install `gdb-multiarch` or you can compile the full toolchain with GDB using the [RTEMS tools](https://github.com/RTEMS/rtems-tools).

Follow the dedicated [README in the `gdbpython` folder](gdbpython/README.md).

## Additional resources

Some GDB scripts are provided to help debugging:
  - [`fix_gdb_uart_to_ci_dos.gdbscript`](./fix_gdb_uart_to_ci_dos.gdbscript)
  - [`load_implant.gdbscript`](./load_implant.gdbscript)

The fix for the `UART_TO_CI` module (UART Telemetry Output and Command Ingest) dynamically fixes an underflow in the message parsing that ends up rewritting all the satellite memory with garbage. This script was created early on during the preparation, and uses breakpoints to work.

The second script first patches the previously described underflow, then loads the implant from Chall3 in memory, and finally patches a kernel function call to initialize it as was the case during the "attack". This script is useful to help debug the exploit needed to validate Chall3.
