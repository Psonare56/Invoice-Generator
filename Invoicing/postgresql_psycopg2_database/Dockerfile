#------------------------ Dockerfile ---------------------------------------#
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

# Copy custom configuration files to the container
COPY pg_hba.conf /etc/postgresql/
COPY environment /etc/postgresql/
COPY pg_ctl.conf /etc/postgresql/
COPY pg_ident.conf /etc/postgresql/
COPY postgresql.conf /etc/postgresql/
COPY start.conf /etc/postgresql/

# Set the default command to run when starting the container
CMD ["postgres"]
