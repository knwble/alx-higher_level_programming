#!/bin/bash
# Script that sends a GET request to a given URL and display status code.
curl -so /dev/null -w "%{http_code}" $1
