#!/usr/bin/python3
"""
This file contains a script that takes in a URL and displays the
value of the variable X-Request_Id
"""


import sys
import requests


if __name__ == "__main__":
    passed_url = sys.argv[1]
    my_response = requests.get(passed_url)
    print(my_response.headers.get("X-Request-Id"))
