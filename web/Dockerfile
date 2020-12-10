# pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/web

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install nodejs
RUN apk add --update nodejs nodejs-npm

# copy project
COPY . .

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
WORKDIR /usr/src/web/frontend
RUN npm i webpack webpack-cli --save-dev
RUN npm i babel-loader
RUN npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev
RUN npm i react react-dom --save-dev
RUN npm install @material-ui/core
RUN npm install @babel/plugin-proposal-class-properties
RUN npm install react-router-dom
RUN npm install @material-ui/icons

WORKDIR /usr/src/web

# run entrypoint.sh
ENTRYPOINT ["/usr/src/web/entrypoint.sh"]
