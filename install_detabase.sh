#!/bin/bash

sudo apt update -y 

# Install psycopg2 on Ubuntu
sudo apt install python3-pip python3-dev libpq-dev -y
sudo apt install python3-psycopg2 -y

# Install PostgreSQL on Ubuntu
sudo apt install postgresql postgresql-contrib -y
sudo systemctl start postgresql
sudo systemctl enable postgresql
sudo systemctl status postgresql
sudo psql --version


sudo apt update -y  



# # configure database
# sudo -i -u postgres
# psql
# CREATE DATABASE invoiceDB;
# CREATE USER myuser WITH ENCRYPTED PASSWORD 'password1612';
# GRANT ALL PRIVILEGES ON DATABASE invoiceDB TO myuser;
# \q
# exit