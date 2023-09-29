#!/usr/bin/python3
"""
This script takes GitHub credentials and uses the GitHub API
to display the account ID
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    api_authentication = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    api_response = requests.get("https://api.github.com/user", auth=api_authentication)
    print(api_response.json().get("id"))
