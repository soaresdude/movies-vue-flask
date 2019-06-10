FROM node:lts-alpine

RUN npm install -g http-server
RUN apk add yarn

WORKDIR /app

COPY yarn.lock package*.json ./

RUN yarn install

COPY . .

RUN yarn build
