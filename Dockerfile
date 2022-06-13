FROM python:3.8-slim-buster

WORKDIR /ai
RUN apt-get update -y
RUN apt-get install -y curl
RUN pip install --upgrade pip

COPY . /ai

RUN pip3 install -r requirements.txt

CMD [ "python3", "./main.py"]


