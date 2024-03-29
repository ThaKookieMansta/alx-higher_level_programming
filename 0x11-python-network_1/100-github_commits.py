#!/usr/bin/python3
"""
This script checks the last 10 commits of a github repository
"""
import sys
import requests


if __name__ == "__main__":
    github_api = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    my_response = requests.get(github_api)
    commits = my_response.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
