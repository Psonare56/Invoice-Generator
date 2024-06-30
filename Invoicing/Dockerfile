# Use an official Python runtime as a parent image
FROM python:3-slim

# Set the working directory in the container
WORKDIR /app

# Install PostgreSQL client dependencies
RUN apt-get update && apt-get install -y postgresql-client

# Copy the current directory contents into the container at /app
COPY . /app

# Install virtualenv
RUN python -m venv /opt/venv

# Activate the virtual environment and install dependencies
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --upgrade pip && pip install -r requirements.txt

# Ensure the database configuration is set for Docker
ENV DATABASE_NAME=invoice_db
ENV DATABASE_USER=invoice_user
ENV DATABASE_PASSWORD=password12345
ENV DATABASE_HOST=invoice-generator-postgres-container
ENV DATABASE_PORT=5432

# Migrate the database
RUN python manage.py makemigrations
RUN python manage.py migrate

# Create Django superuser (make sure the command doesn't fail the build if the superuser already exists)
RUN python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin') if not User.objects.filter(username='admin').exists() else None"

# Expose port 8100 (not necessary unless you're using it directly with docker run)
EXPOSE 8100

# Run manage.py to start the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8100"]

#-----------------------------------------------------------------------------------
# # Use an official Python runtime as a parent image
# FROM python:3-slim

# # Set the working directory in the container
# WORKDIR /app

# # Copy the current directory contents into the container at /app
# COPY . /app

# # Install virtualenv and PostgreSQL client dependencies
# RUN apt-get update && apt-get install -y python3-venv postgresql-client

# # Create a virtual environment
# RUN python -m venv /opt/venv

# # Activate the virtual environment and install dependencies
# ENV PATH="/opt/venv/bin:$PATH"
# RUN pip install --upgrade pip && pip install -r requirements.txt


# # Migrate the database
# RUN python manage.py makemigrations && python manage.py migrate

# # Create Django superuser
# RUN echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell

# # Make port 8000 available to the world outside this container
# EXPOSE 8000

# # Run manage.py to start the Django server
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
