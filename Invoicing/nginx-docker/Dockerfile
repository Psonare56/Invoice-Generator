# Use the official Nginx image from Docker Hub
FROM nginx

# Remove the default Nginx configuration file
RUN rm /etc/nginx/conf.d/default.conf

# Copy the custom Nginx configuration file
COPY nginx.conf /etc/nginx/conf.d/

# Copy website files to the default Nginx HTML directory
COPY index.html /usr/share/nginx/html/

# Expose ports (optional, as it's defined in docker-compose.yml)
EXPOSE 80

# CMD to start Nginx when the container starts
CMD ["nginx", "-g", "daemon off;"]
