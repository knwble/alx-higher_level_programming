#!/usr/bin/python3
"""Python script that Lists recent commits on a given GitHub repository."""


import sys
import requests

if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    response = requests.get(url)
    commits = response.json()

    try:
        for i in range(10):
            print(f"{commits[i]['sha']}:
                  {commits[i]['commit']['author']['name']}")
    except IndexError:
        pass
