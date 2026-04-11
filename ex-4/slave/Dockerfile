FROM ubuntu:22.04
RUN apt update && apt install -y openssh-server
RUN mkdir /var/run/sshd
RUN useradd -m slave && echo "slave:2284" | chpasswd
EXPOSE 22
CMD ["/usr/sbin/sshd","-D"] 
