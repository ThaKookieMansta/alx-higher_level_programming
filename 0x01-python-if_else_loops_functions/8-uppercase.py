#!/usr/bin/python3
def uppercase(str):
    uppercase_string = ""
    for i in str:
        if 96 < ord(i) < 123:
            ascii_value = ord(i) - 32
            uppercase_string += chr(ascii_value)
        else:
            uppercase_string += i
    print(uppercase_string)
