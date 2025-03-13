# 3.0
FROM ubuntu:22.04
ENV TZ=Europe/Warsaw

RUN apt update && apt upgrade -y && apt install -y openjdk-21-jdk kotlin curl
RUN curl --location --show-error -O --url "https://services.gradle.org/distributions/gradle-8.13-bin.zip"
RUN mkdir /opt/gradle
RUN unzip -d /opt/gradle gradle-8.13-bin.zip
RUN rm gradle-8.13-bin.zip
ENV PATH="$PATH:/opt/gradle/gradle-8.13/bin"

RUN useradd -ms /bin/bash student
RUN adduser student sudo
USER student
ENV PATH="$PATH:/opt/gradle/gradle-8.13/bin"


RUN mkdir /home/student/project
WORKDIR /home/student/project

RUN gradle init --type java-application --debug --dsl groovy --package org.example --project-name app
RUN sed -i '/dependencies {/a \    implementation "org.xerial:sqlite-jdbc:3.49.1.0"' ./app/build.gradle
RUN gradle build
RUN ./gradlew :app:dependencies


ENTRYPOINT ["/bin/bash","-c"]
CMD ["gradle run"]