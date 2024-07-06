#!/bin/bash 


# to generate ssl key for localhost  privkey.pem, fullchain.pem
openssl genrsa -out privkey.pem 2048
openssl req -x509 -new -nodes -key privkey.pem -sha256 -days 365 -out fullchain.pem

openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout localhost.key -out localhost.crt

openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/nginx/ssl/localhost.key -out /etc/nginx/ssl/localhost.crt -subj "/CN=localhost"


# ------------------------------------- # -----------------------------------------------

# previous configuration 

root@3b8842b6be56:/etc/nginx# cat nginx.conf 

user  nginx;
worker_processes  auto;

error_log  /var/log/nginx/error.log notice;
pid        /var/run/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    include /etc/nginx/conf.d/*.conf;
}
root@3b8842b6be56:/etc/nginx#


#--------------------------------------------------
nginx -s reload
