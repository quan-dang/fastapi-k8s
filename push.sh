#!/usr/bin/bash
docker build -t dangvanquan25/iris-fastapi:0.0.1 . --platform=linux/amd64
docker push dangvanquan25/iris-fastapi:0.0.1