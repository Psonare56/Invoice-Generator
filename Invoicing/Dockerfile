# ------------------- postgressql
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

# Expose port 8100 (not necessary unless you're using it directly with docker run)
EXPOSE 8200

# Copy the entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod 777 /entrypoint.sh

# # Run the entrypoint script to start the Django server
# ENTRYPOINT ["/entrypoint.sh"]

# # Run manage.py to start the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8200"]
