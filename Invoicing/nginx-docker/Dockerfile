# Use the official Nginx image from Docker Hub
FROM nginx

# Install netcat-openbsd instead of netcat
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Remove the default Nginx configuration file
RUN rm /etc/nginx/conf.d/default.conf

# Copy the wait-for-it script
COPY wait-for-it.sh /wait-for-it.sh

# Make the script executable
RUN chmod +x /wait-for-it.sh

# Copy the custom Nginx configuration file
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY fullchain.txt /etc/nginx/ssl/fullchain.pem
COPY privkey.txt /etc/nginx/ssl/privkey.pem

# Copy website files to the default Nginx HTML directory
COPY index.html /usr/share/nginx/html/

# Expose ports (optional, as it's defined in docker-compose.yml)
EXPOSE 80
EXPOSE 443

# CMD to start Nginx when the container starts
CMD ["nginx", "-g", "daemon off;"]
