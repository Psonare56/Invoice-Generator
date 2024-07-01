#!/bin/bash

docker network rm invoice-network
docker network create invoice-network

# docker build -t kumarsumit74604/postgresql-image:v1 .
docker pull kumarsumit74604/postgresql-image:v1
docker run -d --network invoice-network -p 5432:5432 --name invoice-generator-postgres-container kumarsumit74604/postgresql-image:v1


# docker build -t kumarsumit74604/invoice-generator-image:v2 . 
docker pull kumarsumit74604/invoice-generator-image:v2 
docker run --network invoice-network -d -p 8100:8100 --name invoice-generator-container kumarsumit74604/invoice-generator-image:v2


