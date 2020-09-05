# SPACE SECURITY CHALLENGE 2020 HACK-A-SAT: Tools & Infra

## 2020 Hack-a-Sat Final challenges

You can find the open source release of challenges and other code used in the 2020 Hack-a-Sat Final in this repository: [hackasat-final-2020](https://github.com/cromulencellc/hackasat-final-2020).

## QEMU + GDB to emulate and debug a satellite

The subfolder [`qemu-vm`](https://github.com/solar-wine/tools-for-hack-a-sat-2020/tree/master/qemu-vm) contains instructions and patches to compile and launch QEMU for the satellite architecture.

The binaries given for the Finals are also present so that it is possible to replay some of the Finals challenges.

In addition, a `python-gdb` plugin for `RTEMS 5` is provided to help debugging. Specifically, it helps developping the exploit to solve Chall3 from the Finals.

## CCSDS using scapy

The subfolder [`scapy-space-packets`](https://github.com/solar-wine/tools-for-hack-a-sat-2020/tree/master/scapy-space-packets) provides an implementation of the CCSDS Space Packet Protocol using Python and [`scapy`](https://scapy.net/).

Using a command line interface, it enables communicating with a satellite without the hassle of having to find where to click on a GUI interface.

It can directly connect to the satellite via a Unix socket or TCP port, or using the [COSMOS](https://cosmosrb.com/) router port.

## Infrastructure

Parts of the infrastructure we used during the final event and for the preparation phase are available in the [`infra`](infra/) subfolder.

## Misc

A list of acronyms can be found in [`acronyms.md`](https://github.com/solar-wine/tools-for-hack-a-sat-2020/blob/master/acronyms.md).


--

*Solar Wine Team*
