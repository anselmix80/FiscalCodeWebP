#!/bin/bash

docker build -t web ../.
docker run -p 8080:80 --name web -d web