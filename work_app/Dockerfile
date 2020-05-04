FROM openjdk:alpine

ADD . /work_app

WORKDIR /work_app

RUN javac -cp ".:./jedis-3.2.0.jar:./postgresql-42.2.12.jar" work_app.java

CMD ["java", "-cp", ".:./jedis-3.2.0.jar:./postgresql-42.2.12.jar", "work_app"]
