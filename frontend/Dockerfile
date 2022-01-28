FROM node:10.19.0-alpine
WORKDIR /app
COPY package.json ./
COPY package-lock.json ./
COPY ./public ./public
COPY ./src ./src
RUN npm i
