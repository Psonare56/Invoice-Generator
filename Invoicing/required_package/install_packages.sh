#!/bin/bash

# If you are running without creating Venv 

# Install Python 3 and pip (if not already installed)
sudo apt update -y 
sudo apt upgrade -y
sudo apt install -y python3 python3-pip python3-full python3-pipx python-is-python3
sudo apt install docker.io docker-compose  -y


# Install system dependencies
sudo apt install -y python3-dev libpq-dev libjpeg-dev libopenjp2-7 
sudo apt install -y python3-asgiref
sudo apt install -y python3-django-crispy-forms
sudo apt install -y python3-pdfkit
sudo apt install -y python3-pillow
sudo apt install -y python3-sqlparse
sudo apt install -y tzdata

# Install Django and crispy-bootstrap4 (these packages will be installed using pip)
sudo apt install -y python3-django
sudo apt install -y python3-crispy-bootstrap4
sudo apt install -y python3-psycopg2


# Database
sudo apt-get install -y libpq-dev
dpkg -l | grep postgresql
sudo apt-get update
sudo apt-get install postgresql -y
sudo systemctl restart postgresql
sudo systemctl status postgresql

sudo apt update -y