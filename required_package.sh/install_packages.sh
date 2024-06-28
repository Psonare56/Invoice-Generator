#!/bin/bash

# If you are running without creating Venv 

# Install Python 3 and pip (if not already installed)
apt install -y python3 python3-pip python3-full pipx python-is-python3
apt install docker.io -y


# Install system dependencies
apt install -y python3-dev libpq-dev libjpeg-dev libopenjp2-7 

# Install packages using pip
apt install -y python3-asgiref
apt install -y python3-django-crispy-forms
apt install -y python3-pdfkit
apt install -y python3-pillow
apt install -y python3-sqlparse
apt install -y tzdata

# Install Django and crispy-bootstrap4 (these packages will be installed using pip)
apt install -y python3-django
apt install -y python3-crispy-bootstrap4


apt update -y
apt upgrade -y