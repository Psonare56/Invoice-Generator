# Use the official PostgreSQL image from the Docker Hub
FROM postgres:13

# Set environment variables for the database
ENV POSTGRES_DB=invoice_db
ENV POSTGRES_USER=invoice_user
ENV POSTGRES_PASSWORD=password12345

# Expose the default PostgreSQL port
EXPOSE 5432

# Copy custom initialization scripts to the container's initialization directory
COPY init.sql /docker-entrypoint-initdb.d/

# Set the default command to run when starting the container
CMD ["postgres"]
