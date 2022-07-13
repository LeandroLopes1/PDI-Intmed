FROM python:3.10
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /app
WORKDIR /app
# install dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
libsqlite3-dev


COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

ADD . /app