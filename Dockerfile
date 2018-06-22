FROM python:3

COPY requirements.txt /

RUN apt-get update

RUN apt-get install -y libgdal-dev

RUN pip install numpy

RUN pip install -r requirements.txt