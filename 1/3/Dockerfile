# 3.0
FROM ubuntu:22.04
ENV TZ=Europe/Warsaw

RUN apt update && apt upgrade -y && apt install -y python3.10
RUN ln -s /usr/bin/python3.10 /usr/bin/python

RUN useradd -ms /bin/bash student
RUN adduser student sudo

USER student
WORKDIR /home/student/

EXPOSE 8080
VOLUME /home/student/

CMD ["/bin/bash"]