# Create TLS secret for PostgreSQL
kubectl create secret tls postgresql-tls --cert=path/to/postgresql.crt --key=path/to/postgresql.key -n invoice-generator-namespace

# Create TLS secret for application
kubectl create secret tls application-tls --cert=path/to/application.crt --key=path/to/application.key -n invoice-generator-namespace

# Create TLS secret for Redis
kubectl create secret tls redis-tls --cert=path/to/redis.crt --key=path/to/redis.key -n invoice-generator-namespace
