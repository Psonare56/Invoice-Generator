#!/bin/bash

sudo apt remove python3-psycopg2

sudo apt-get --purge remove postgresql postgresql-client postgresql-client-common postgresql-common -y
sudo apt-get autoremove
sudo apt-get autoclean

sudo rm -rf /var/lib/postgresql/
sudo rm -rf /etc/postgresql/
