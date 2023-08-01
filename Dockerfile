FROM python:3.10-slim-buster

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y

RUN apt-get update \
    && apt-get -y install netcat gcc python3-opencv \
    && apt-get clean

WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python", "webapp.py", "--port=5001" ]