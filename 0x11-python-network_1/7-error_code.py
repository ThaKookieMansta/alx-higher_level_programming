#!/usr/bin/python3
"""
This file contains a script that takes a URL, sends a request  to the
URL and displays the body
"""
import sys
import requests


if __name__ == "__main__":
    passed_url = sys.argv[1]

    my_response = requests.get(passed_url)
    if my_response.status_code >= 400:
        print("Error code: {}".format(my_response.status_code))
    else:
        print(my_response.text)
