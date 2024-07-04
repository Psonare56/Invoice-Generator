#/bin/bash
#!/usr/bin/env bash
# wait-for-it.sh: Wait for services defined in docker-compose.yml to become available.

set -e

host=$1
port=$2
shift 2
cmd="$@"

while ! nc -z $host $port; do
  echo "Waiting for $host:$port..."
  sleep 2
done

echo "Service $host:$port is available!"

# Execute the command if provided
if [ -n "$cmd" ]; then
  exec $cmd
fi



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