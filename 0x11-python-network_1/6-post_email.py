#!/usr/bin/python3
"""
This file contains a script that takes a URL and email address, sends
a post request to the URL and displays the body of the response
"""
import sys
import requests


if __name__ == "__main__":
    passed_url = sys.argv[1]
    email = {"email": sys.argv[2]}

    my_response = requests.post(passed_url, data=email)
    print(my_response.text)
