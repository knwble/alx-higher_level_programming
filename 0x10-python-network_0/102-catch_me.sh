#!/bin/bash

# Send a request to the specified URL causing the server to respond
curl -s -X PUT -H "Origin: test" -d "user_id=98" "0.0.0.0:5000/catch_me" >/dev/null 2>&1 &
