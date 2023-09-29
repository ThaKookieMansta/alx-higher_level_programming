#!/usr/bin/python3
"""
This file contains a script that takes a URL and email address, sends
a post request to the URL and displays the body of the response
"""

import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    passed_url = sys.argv[1]
    email = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(email).encode("ascii")

    request = urllib.request.Request(passed_url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
