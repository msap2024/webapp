# Dockerfile
FROM ubuntu:16.04

RUN apt-get update && apt-get install -y python python-pip flask

RUN pip install --upgrade pip

COPY app.py /opt/

ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0
