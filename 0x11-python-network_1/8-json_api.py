#!/usr/bin/python3
"""
This script takes a letter and searches for a user  with the  letter
passed
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]
    payload = {"q": letter}

    my_response = requests.post("http://0.0.0.0:5000/search_user",
                                data=payload)
    try:
        response = my_response.json()
        if response == {}:
            print("No result")
        else:
            print(f'[{response.get("id")}] {response.get("name")}')
    except ValueError:
        print("Not a valid JSON")
