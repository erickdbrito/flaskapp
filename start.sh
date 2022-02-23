#!/bin/bash
app="flask.test"
docker build -t ${app} .
docker run -d -p 56733:80 \
  --name=flask.test \
  -v ./:/app flask.test