#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL."""


import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    # Send a GET request to the URL
    response = requests.get(url)

    # Print the value of the X-Request-Id header from the response
    print(response.headers.get("X-Request-Id"))
