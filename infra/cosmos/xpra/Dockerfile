FROM debian:buster
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get --yes --no-install-recommends install xpra dumb-init dbus-x11 xauth python-pil python-pyinotify lz4 python-lz4

RUN mkdir -p /run/user/0/

CMD ["dumb-init", "/usr/bin/xpra", "start", "--bind-tcp=0.0.0.0:6010", ":10", "--daemon=no"]
EXPOSE 6000
