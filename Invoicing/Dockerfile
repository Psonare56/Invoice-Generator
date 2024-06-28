# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y python3-venv

# Create a virtual environment
RUN python -m venv /opt/venv

# Activate the virtual environment and install dependencies
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Migrate the database
RUN python manage.py makemigrations
RUN python manage.py migrate

# Create superuser non-interactively
RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run manage.py to start the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
