#!/bin/bash

# Check if the number of arguments is less than 2
if [ $# -lt 2 ]; then
    echo "Usage: $0 <URL> <file>"
    exit 1
fi

# Sends a JSON POST request to the given URL with the content of the file as the request body
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
