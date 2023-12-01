#!/usr/bin/python3
"""Sends a POST request http://0.0.0.0:5000/search_user with a given letter."""


import sys
import requests

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {"q": letter}

    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        json_response = response.json()

        if json_response:
            print("[{}] {}".format(json_response['id'], json_response['name']))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
