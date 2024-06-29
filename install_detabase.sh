#!/bin/bash

sudo apt update -y 
sudo apt upgrade -y 

# Install psycopg2 on Ubuntu
sudo apt install python3-pip python3-dev libpq-dev -y

# Install PostgreSQL on Ubuntu
sudo apt install postgresql postgresql-contrib -y
sudo systemctl start postgresql
sudo systemctl enable postgresql
sudo systemctl status postgresql

