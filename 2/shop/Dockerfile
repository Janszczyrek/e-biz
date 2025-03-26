FROM ubuntu:24.04

RUN apt-get update && apt-get install -y \
    openjdk-21-jdk \
    maven \
    git \
    scala \
    curl
RUN echo "deb https://repo.scala-sbt.org/scalasbt/debian all main" | tee /etc/apt/sources.list.d/sbt.list
RUN echo "deb https://repo.scala-sbt.org/scalasbt/debian /" | tee /etc/apt/sources.list.d/sbt_old.list
RUN curl -sL "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x2EE0EA64E40A89B84B2DF73499E82A75642AC823" | tee /etc/apt/trusted.gpg.d/sbt.asc
RUN apt-get update && apt-get install -y sbt

WORKDIR /app
COPY . /app

EXPOSE 9000

CMD ["sbt", "run"]

