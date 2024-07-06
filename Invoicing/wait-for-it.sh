#!/bin/bash
# wait-for-it.sh: A script to wait for service(s) to be available before executing a command

set -e

# Variables
host="$1"
port="$2"
shift 2
cmd="$@"

# Function to check if a host is reachable on a specific port
wait_for() {
    echo -n "Waiting for $host:$port..."
    while ! nc -z "$host" "$port"; do
        echo -n "."
        sleep 1
    done
    echo " Service is up!"
}

# Check for required arguments
if [ -z "$host" ] || [ -z "$port" ]; then
    echo "Usage: $0 host port [cmd]"
    exit 1
fi

# Call the wait_for function
wait_for

# Execute the provided command (if any)
exec "$cmd"