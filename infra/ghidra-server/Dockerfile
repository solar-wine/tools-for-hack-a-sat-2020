FROM debian:buster


ARG GHIDRA_VERSION=9.1.2_PUBLIC
ARG GHIDRA_DATE=20200212
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get --yes --no-install-recommends install wget unzip openjdk-11-jre-headless dumb-init

RUN wget "https://ghidra-sre.org/ghidra_${GHIDRA_VERSION}_${GHIDRA_DATE}.zip" -O /tmp/ghidra.zip && \
    unzip "/tmp/ghidra.zip" -d "/tmp" && \
	mv "/tmp/ghidra_${GHIDRA_VERSION}/" "/ghidra/" && \
	rm -rf /tmp/

WORKDIR /ghidra

ADD server.conf /ghidra/server/
ADD jaas.conf /ghidra/server/

CMD ["dumb-init", "/ghidra/server/ghidraSvr", "console"]
EXPOSE 13100 13101 13102

VOLUME /data
