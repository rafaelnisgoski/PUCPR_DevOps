FROM ubuntu:latest

RUN mkdir /app

WORKDIR /app

COPY . .

RUN apt-get update

RUN apt-get install python -y

RUN echo "print('hello world')" > hellopuc.py

CMD python hellopuc.py