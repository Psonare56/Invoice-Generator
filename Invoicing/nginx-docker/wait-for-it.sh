#!/bin/bash
# wait-for-it.sh: Wait for a service to become available.
# Usage: wait-for-it.sh host:port [cmd]

set -e

hostport=$1
shift
cmd="$@"

# Split hostport into HOST and PORT
IFS=':' read -r HOST PORT <<< "$hostport"

until nc -z "$HOST" "$PORT"; do
  echo "Waiting for $HOST:$PORT..."
  sleep 2
done

echo "Service $HOST:$PORT is available"

# Execute the command
exec "$cmd"


# #!/usr/bin/env bash

# # wait-for-it.sh: Wait for a service to become available.
# # Usage: wait-for-it.sh host:port [cmd]

# hostport=$1
# shift
# cmd="$@"

# while ! nc -z $(echo $hostport | cut -d: -f1) $(echo $hostport | cut -d: -f2); do
#   echo "Waiting for $hostport..."
#   sleep 2
# done

# exec $cmd