#!/bin/bash

# Wait for the specified host and port to be available
host=$1
port=$2

shift 2

while ! nc -z $host $port; do
  echo "Waiting for $host:$port..."
  sleep 1
done

echo "$host:$port is up!"

# Execute the remaining command
exec "$@"
