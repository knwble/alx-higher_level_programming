#!/usr/bin/python3
"""
Takes GitHub credentials (username & password) and uses the GitHub
API to display the user's id
"""


import requests
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]

    r = requests.get('https://api.github.com/user', auth=(username, password))

    try:
        json_response = r.json()

        if 'id' in json_response:
            print(json_response['id'])
        else:
            print("ID not found in the response")
    except ValueError:
        print('Not a valid JSON')
