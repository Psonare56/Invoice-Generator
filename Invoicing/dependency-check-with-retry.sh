#!/bin/bash

MAX_RETRIES=5
RETRY_DELAY=60  # in seconds
RETRIES=0
SUCCESS=0

while [ $RETRIES -lt $MAX_RETRIES ]; do
    dependency-check.sh --project "Invoice-Generator" --scan "./" --out "./dependency-check-report" --format "XML" --cveUrlBase "https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-" --cveUrlModified "https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-modified.json.gz"
    
    if [ $? -eq 0 ]; then
        SUCCESS=1
        break
    else
        echo "Dependency Check failed. Retrying in ${RETRY_DELAY} seconds..."
        sleep $RETRY_DELAY
        RETRIES=$((RETRIES + 1))
    fi
done

if [ $SUCCESS -eq 0 ]; then
    echo "Dependency Check failed after ${MAX_RETRIES} retries."
    exit 1
fi

echo "Dependency Check completed successfully."
exit 0
