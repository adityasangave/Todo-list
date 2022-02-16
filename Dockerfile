# explain about docker, docker images and where to get those
FROM python:3.8-alpine

ENV PYTHONBUFFERED=1 
# avoids buffer while running

COPY ./requirements.txt /requirements.txt
#store dependencies
RUN pip3 install -r requirements.txt
#run and install dependencies

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
# creates a user named user to avoid running app from root user