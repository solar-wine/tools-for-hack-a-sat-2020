FROM debian:buster

RUN apt-get update && \
    apt-get --yes --no-install-recommends install wget unzip dumb-init git python3 apt-transport-https ca-certificates python3-setuptools python3-pyqt5

WORKDIR /install

RUN git clone https://github.com/fidgetingbits/IDArling /install/idarling && \
    cd /install/idarling && \
    git checkout db5a9ca3b4dd895f8604afe22ac56642e4882d94

# setup.py is broken? "Couldn't find a setup script" when installing PyQt5... hence the hack :)

ADD run.sh /install/run.sh

CMD ["dumb-init", "bash", "/install/run.sh"]
EXPOSE 31013

VOLUME /install/idarling/idarling/files
VOLUME /install/idarling/idarling/logs
