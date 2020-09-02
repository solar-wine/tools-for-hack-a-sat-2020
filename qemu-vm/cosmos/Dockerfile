# Usage:
#   podman build -t cosmos .
#   podman run -ti -v $(pwd):/host --net=host -p 54321:54321 -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix:rw -v ~/.Xauthority:/root/.Xauthority:Z cosmos
#   (in container) rm Gemfile.lock && bundle install && ruby Launcher

FROM ubuntu:18.04

RUN \
    export DEBIAN_FRONTEND=noninteractive && \
    apt-get update -yy && \
    apt-get install -y build-essential curl wget dnsutils net-tools netcat socat tcpdump
COPY cosmos /cosmos/
WORKDIR /cosmos

# Automatically answer:
#    Install dependencies using Root/Sudo/No (Rsn):  => R
#    Do you want to continue? [Y/n]  => Y (because of a missing -y in "apt-get install bundler")
#    Install ruby using rbenv (Yn):  => Y
#    Install and run COSMOS demo (Yn): => N
RUN cd /cosmos && export DEBIAN_FRONTEND=noninteractive && printf 'r\ny\ny\nn\n' | ./setup.sh

# For Gtk with Qt4
ENV QT_STYLE_OVERRIDE=gtk2 QT_X11_NO_MITSHM=1
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y gedit qt4-qtconfig gtk2-engines-qtcurve libxext-dev libxrender-dev libxtst-dev
RUN rm Gemfile.lock && bundle install

CMD ["/bin/bash"]
