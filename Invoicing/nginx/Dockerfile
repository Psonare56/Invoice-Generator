# Use the official Nginx image
FROM nginx

# Remove default configuration file
RUN rm /etc/nginx/conf.d/default.conf

# Copy custom configuration file from the current directory
COPY nginx.conf /etc/nginx/conf.d
