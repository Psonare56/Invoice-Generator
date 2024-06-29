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
    && rm -rf /var/lib/apt/list/*

# Create a virtual environment
RUN python -m venv /opt/venv

# Activate the virtual environment and install dependencies
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Install PostgreSQL client library and other dependencies
RUN apt-get install -y libpq-dev
RUN pip install psycopg2-binary
RUN apt-get update -y

# # Set environment variables for PostgreSQL connection
# ENV POSTGRES_DB=invoice_db
# ENV POSTGRES_USER=invoice_user
# ENV POSTGRES_PASSWORD=password12345
# ENV POSTGRES_HOST=postgres-db

# Migrate the database
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py makemigrations invoice1
RUN python manage.py migrate invoice1


# Create superuser non-interactively
RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@admin.com', 'admin')" | python manage.py shell

## Make port 8000 available to the world outside this container
EXPOSE 7000

# Run manage.py to start the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:7000"]
