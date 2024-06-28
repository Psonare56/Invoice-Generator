#!/bin/bash

docker rm -f $(docker ps -a -q)
docker rm -f $(docker ps -aq)
docker rmi -f $(docker images -aq)