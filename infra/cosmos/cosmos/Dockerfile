FROM debian:buster


ENV DEBIAN_FRONTEND noninteractive
ENV DISPLAY :10
# For Gtk with Qt4
ENV QT_STYLE_OVERRIDE=gtk2 QT_X11_NO_MITSHM=1

RUN apt-get update && \
    apt-get --yes --no-install-recommends install build-essential curl wget dnsutils net-tools netcat socat tcpdump gedit qt4-qtconfig gtk2-engines-qtcurve libxext-dev libxrender-dev libxtst-dev xauth python-pil

ADD cosmos.tar.gz /
WORKDIR /cosmos

# Automatically answer:
#    Install dependencies using Root/Sudo/No (Rsn):  => R
#    Do you want to continue? [Y/n]  => Y (because of a missing -y in "apt-get install bundler")
#    Install ruby using rbenv (Yn):  => Y
#    Install and run COSMOS demo (Yn): => N
RUN chmod +x setup.sh
RUN printf 'r\ny\ny\nn\n' | ./setup.sh

RUN gem install bundler:1.16.1
RUN rm Gemfile.lock && bundle install
ADD cmd_tlm_server.txt /cosmos/config/tools/cmd_tlm_server/cmd_tlm_server.txt
ADD start.sh /cosmos/start.sh

CMD ["bash", "/cosmos/start.sh"]

