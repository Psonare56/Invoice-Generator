# Use an official Python runtime as a parent image
FROM python:3-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install virtualenv
RUN apt-get update && apt-get install -y python-venv

# Create a virtual environment
RUN python -m venv env

# Activate the virtual environment and install dependencies
RUN /bin/bash -c "source env/bin/activate \
                 && pip install --upgrade pip \
                 && pip install -r requirements.txt"

# Migrate the database
RUN python manage.py makemigrations && python manage.py migrate

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run manage.py to start the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
