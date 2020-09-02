# COSMOS over TCP

## Introduction

In the default configuration, Comos cannot be used to communicate with the [QEMU environment we provide](https://github.com/solar-wine/tools-for-hack-a-sat-2020/tree/master/qemu-vm).

A new interface had to be added to Cosmos, `tcpip_cs_client_interface.rb`, to allow TCP communication with a checksum so that it can be directly forwarded to a serial port (which uses a checksum).

A `Dockerfile` is provided for the Cosmos installation.


## Configuration for Cosmos

  - Decompress [`infra/cosmos/cosmos/cosmos.tar.gz`](../../infra/cosmos/cosmos/cosmos.tar.gz) in this folder: `tar xzf cosmos.tar.gz`
  - Make `setup.sh` executable: `chmod +x cosmos/setup.sh`
  - Replace the telemetry server configuration with the one that establishes a connection to a TCP/IP endpoint: `cp cmd_tlm_server.txt cosmos/config/tools/cmd_tlm_server/`
  - Add support for TCP/IP interface with checksum: `cp tcpip_cs_client_interface.rb cosmos/lib/`

## Create/Launch a Docker container with Cosmos

  - The first time, create the container: `docker build -t cosmos .`
  - Launch the Docker container: `docker run -ti -v "$(pwd):/host" --net=host -p 54321:54321 -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix:rw -v "${XAUTHORITY:-~/.Xauthority}:/root/.Xauthority:Z" cosmos`
  - Inside the container, fix the Ruby setup and start Cosmos: `gem install bundler:1.16.1 && bundle install && ruby Launcher`

## Connecting to QEMU Unix socket

  - To forward Cosmos packets to `radio.sock`, use `socat`: `socat TCP-L:54321,reuseaddr UNIX:radio.sock`

## Remote connection to a FlatSat

**This part is only useful in case you have a FlatSat to connect to.**

  - On the remote computer: `socat /dev/ttyUSB0,b19200,raw,echo=0 tcp-l:54321,reuseaddr`
  - On the local computer: `ssh -NfL 54321:localhost:54321 <user>@<IP>`
  - This replaces emulation with the real hardware!
