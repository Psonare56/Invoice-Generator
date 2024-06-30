#!/bin/bash

# Delate all containers, Images
docker rm -f $(docker ps -aq)
docker rmi -f $(docker images -aq)
docker network rm invoice-network
docker network create invoice-network
#docker network create --driver overlay invoice-network  # docker swam

