FROM alpine:latest

RUN apk update\
 && apk add npm

RUN mkdir /opt/app
COPY ./ /opt/app
WORKDIR /opt/app

RUN npm i
EXPOSE 8040

CMD node app.js
