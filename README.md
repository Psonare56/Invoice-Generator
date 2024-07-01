# Invoice-Generator
## Installation
# To install all package follow ./required_package/install_packages.sh
### 1. Install Python3

Make sure you have Python3 and pip installed on your machine. You can install them using the following commands:


    sudo apt-get install python3 -y
    sudo apt-get install python3-pip -y
    sudo apt-get install -y libpq-dev -y
    pip install psycopg2-binary

## 2. Setup Local Environment

Create and activate a virtual environment to manage your project dependencies.

# Windows:

    python -m venv env
    cd env/Scripts
    activate

# Ubuntu:
    
    python -m venv env
    source env/bin/activate

## Install Dependencies, Install the required packages using pip:

    pip install django
    pip install -r requirements.txt

# Apply database migrations:

    python manage.py makemigrations
    python manage.py migrate

# Create a superuser:

    python manage.py createsuperuser  

# Runserver

    python manage.py runserver 0.0.0.0:8000

### Docker Setup for Separate Containers

# 1. Clone the Repository

    git clone https://github.com/yourusername/invoice-generator.git

    cd invoice-generator

# 2. Create Network

    docker create network <network-name>

# Build and Run Database Container

### 3. Create a Dockerfile for your database container, build the image, and run the container:
        
    docker build -t <username_dockerhub>/<db_image_name>:<tag_name> .

    docker run --network invoice-network -d -p 5432:5432 --name invoice-generator-db-container <username_dockerhub>/<db_image_name>:<tag_name>
                                    
#### Or with environment variables:

    docker run --network <network-name> -d -p 5432:5432 -e POSTGRES_DB=invoice_db -e POSTGRES_USER=invoice_user -e POSTGRES_PASSWORD=password12345 -e POSTGRES_PORT=5432 --name invoice-generator-db-container <username_dockerhub>/<db_image_name>:<tag_name>


# Build and Run Application Container

### 4. Create a Dockerfile for your application container, build the image, and run the container:
        
    docker build -t <username_dockerhub>/<app_image_name>:<tag_name> .

    docker run --network <network-name> -d -p 8100:8100 --name invoice-generator-container <username_dockerhub>/<app_image_name>:<tag_name>
                                        
#### Or with environment variables:

        docker run --network <network-name> -d -p 8100:8100 -e DATABASE_NAME=invoice_db -e DATABASE_USER=invoice_user -e DATABASE_PASSWORD=password12345 -e DATABASE_HOST=invoice-generator-db-container -e DATABASE_PORT=5432 --name invoice-generator-container <username_dockerhub>/<app_image_name>:<tag_name>

# From docker-compose

    docker-compose down --volumes --remove-orphans --rmi all  
    docker-compose up --build -d web

# Additional Steps
### Apply database migrations:
        
    docker-compose exec web python manage.py migrate

### Create a superuser:
        
    docker-compose exec web python manage.py createsuperuser
         
For Create Jenkins Pipeline follow ./DevSecops folder 