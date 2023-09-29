#!/usr/bin/python3
"""
This file contains a script that takes in a URL, sends a request to
the URL and displays the body of the response
"""

import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as error_msg:
        print("Error code: {}".format(error_msg.code))
