# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y python3-venv \
    && apt-get install -y postgresql-client \
    && apt-get install -y libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Create a virtual environment
RUN python -m venv /opt/venv

# Activate the virtual environment and install dependencies
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip install psycopg2-binary

# Make port 7000 available to the world outside this container
EXPOSE 9000

# Command to run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:9000"]
