# Invoice-Generator

## Installation

    To install all package run required_package.sh/install_packages.sh

### 1. Install Python3

Make sure you have Python3 and pip installed on your machine. You can install them using the following commands:

    ```sh
    sudo apt-get install python3 -y
    sudo apt-get install python3-pip -y

### 2. Setup Local Environment

Create and activate a virtual environment to manage your project dependencies.

# Windows:

    ```sh
    python -m venv env
    cd env/Scripts
    activate

# Ubuntu:

    ```sh
    python -m venv env
    source env/bin/activate

Install Dependencies
Install the required packages using pip:

    ```sh
    pip install django
    pip install -r requirements.txt


# Runserver

    python manage.py runserver 0.0.0.0:8000

# Build image 

    docker build -t <username_dockerhub>/<current_image_name>:<tag_name> .

# Run Container

    docker run --name invoice-generator-container -d -p 8000:8000 <username_dockerhub>/<current_image_name>:<tag_name>
