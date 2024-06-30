#!/bin/bash

sudo apt update -y 

# Install psycopg2 on Ubuntu
sudo apt install python3-pip python3-dev libpq-dev -y
sudo apt install -y python3-psycopg2

# Install PostgreSQL on Ubuntu
sudo apt install postgresql postgresql-contrib -y
sudo systemctl start postgresql
sudo systemctl enable postgresql
sudo systemctl status postgresql

sudo psql --version
sudo apt update -y  

 # configure database in local 
sudo -i -u postgres
psql
CREATE DATABASE invoice_db;
CREATE ROLE invoice_user WITH LOGIN PASSWORD 'password12345';
GRANT ALL PRIVILEGES ON DATABASE invoice_db TO invoice_user;

# ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO invoice_user;
 ALTER SCHEMA public OWNER TO invoice_user;

 ALTER ROLE invoice_user VALID UNTIL 'infinity';~

# -- Grant superuser privileges
 ALTER ROLE invoice_user SUPERUSER;

# -- Grant permission to create roles
ALTER ROLE invoice_user CREATEROLE;

# -- Grant permission to create databases
ALTER ROLE invoice_user CREATEDB;

# -- Grant permission for replication (if needed)
ALTER ROLE invoice_user REPLICATION;

# -- Grant permission to bypass RLS (Row Level Security)
ALTER ROLE invoice_user BYPASSRLS;

\q

exit

psql -U invoice_user -d invoice_db

\l

\du

\dt

\q

exit


sudo nano /etc/postgresql/16/main/pg_hba.conf
# # TYPE  DATABASE        USER            ADDRESS                 METHOD
# local   all             invoice_user    peer                    md5
# local   invoice_db      invoice_user                            md5

sudo systemctl reload postgresql

sudo systemctl restart postgresql