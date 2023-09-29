#!/usr/bin/python3
"""
This file contains a script that fetches
https://alx-intranet.hbtn.io/status
"""

import requests

if __name__ == "__main__":
    my_response = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(my_response.text)))
    print("\t- content: {}".format(my_response.text))
