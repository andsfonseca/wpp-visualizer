FROM node:16-alpine

ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true

WORKDIR /home/node/

RUN apk update && \
    apk add chromium && \
    apk add git

RUN git clone --branch v1.1.23 https://github.com/wppconnect-team/wppconnect-server.git && \
    mv ./wppconnect-server  ./app

WORKDIR /home/node/app

COPY ./src/config.json ./src/config.json

RUN yarn install &&\
    yarn build

EXPOSE 21465

CMD [ "yarn", "dev"]