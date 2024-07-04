#!/usr/bin/env bash
# wait-for-it.sh

set -e

host="$1"
shift
port="$1"
shift
cmd="$@"

while ! nc -z "$host" "$port"; do
  echo "Waiting for $host:$port..."
  sleep 1
done

echo "$host:$port is up!"
exec $cmd

# # wait-for-it.sh: Wait for a service to become available.
# # Usage: wait-for-it.sh host:port [cmd] #

# hostport=$1
# shift
# cmd="$@"

# while ! nc -z $(echo $hostport | cut -d: -f1) $(echo $hostport | cut -d: -f2); do
#   echo "Waiting for $hostport..."
#   sleep 2
# done

# exec $cmd