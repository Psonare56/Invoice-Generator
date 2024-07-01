#!/bin/bash

##  List all files including hidden ones
ls -a

## Make all files executable in the current directory
chmod +x *

# Stop and remove containers, networks, and images managed by docker-compose
docker-compose down --volumes --remove-orphans --rmi all

# Remove the docker network if it exists
docker network rm invoice-network

# Create a new docker network named invoice-network
docker network create invoice-network

# List all docker networks
docker network list

# Rebuild and start the 'web' service defined in docker-compose.yml
docker-compose up --build -d web

# List all docker images
docker images

# List all running docker containers
docker ps
