# 3.0
FROM ubuntu:22.04
ENV TZ=Europe/Warsaw

RUN apt update && apt upgrade -y && apt install -y openjdk-8-jdk kotlin

RUN useradd -ms /bin/bash student
RUN adduser student sudo

USER student
WORKDIR /home/student/


CMD ["/bin/bash"]