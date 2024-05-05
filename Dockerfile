FROM ubuntu:latest

RUN mkdir /app
WORKDIR /app

COPY . .

RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install python3-flask -y

CMD python3 app.py