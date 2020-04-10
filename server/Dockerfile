FROM alpine:latest

RUN apk update\
 && apk add python3-dev gcc\
 musl-dev libffi-dev openssl-dev\
 && pip3 install --upgrade pip

RUN mkdir /opt/app
COPY ./ /opt/app
WORKDIR /opt/app

RUN pip3 install -r requrements.txt
EXPOSE 8040

CMD gunicorn -w 4 -b :8040 wsgi:app
