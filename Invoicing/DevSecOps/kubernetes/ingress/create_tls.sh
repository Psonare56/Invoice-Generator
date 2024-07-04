#!/bin/bash

# Create directories for TLS certificates
mkdir -p application-tls postgresql-tls redis-tls

# Function to generate TLS certificates and keys
generate_tls() {
    local name="$1"
    local directory="$2"

    # Generate private key
    openssl genrsa -out "${directory}/${name}.key" 2048

    # Generate CSR (Certificate Signing Request)
    openssl req -new -key "${directory}/${name}.key" -out "${directory}/${name}.csr" -subj "/CN=${name}.yourdomain.com"

    # Self-sign the certificate (valid for 365 days)
    openssl x509 -req -days 365 -in "${directory}/${name}.csr" -signkey "${directory}/${name}.key" -out "${directory}/${name}.crt"

    # Clean up the CSR file
    rm "${directory}/${name}.csr"

    echo "Generated ${directory}/${name}.key and ${directory}/${name}.crt"
}

# Generate TLS certificates and keys for application
generate_tls "application" "application-tls"

# Generate TLS certificates and keys for PostgreSQL
generate_tls "postgresql" "postgresql-tls"

# Generate TLS certificates and keys for Redis
generate_tls "redis" "redis-tls"

echo "TLS certificates and keys generated successfully."

