# Use the official Nginx image from Docker Hub
FROM nginx

# Remove the default Nginx configuration file
RUN rm /etc/nginx/conf.d/default.conf

# Copy the custom Nginx configuration file
COPY nginx.conf /etc/nginx/conf.d/

# Expose port 80 from the container
EXPOSE 81

# Start Nginx and keep it running in the foreground
CMD ["nginx", "-g", "daemon off;"]
