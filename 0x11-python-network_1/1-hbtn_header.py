#!/usr/bin/python3
"""
This file contains a script that takes a URL, sends a
request to the URL and displays the value of
X-Request_Id
"""

import urllib.request
import sys


if __name__ == "__main__":
    passed_url = sys.argv[1]
    request = urllib.request.Request(passed_url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
