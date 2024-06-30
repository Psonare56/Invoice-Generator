#!/bin/bash

docker-compose down --volumes --remove-orphans --rmi all



docker-compose logs web
docker-compose exec web /entrypoint.sh
docker-compose up --build -d web