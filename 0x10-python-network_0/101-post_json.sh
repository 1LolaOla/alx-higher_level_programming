#!/bin/bash

# Get the URL and JSON file from command line arguments
URL="$1"
JSON_FILE="$2"

# Check if the JSON file is valid
if ! jq '.' "$JSON_FILE" >/dev/null 2>&1; then
    echo "Not a valid JSON"
    exit 1
fi

# Send the POST request with the contents of the JSON file in the body
RESPONSE=$(curl -s -X POST -H "Content-Type: application/json" -d "@$JSON_FILE" "$URL")

# Display the body of the response
echo "$RESPONSE"
