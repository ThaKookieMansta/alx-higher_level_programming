#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    arguments_sum = 0
    for i in argv[1:]:
        arguments_sum += int(i)
    print(arguments_sum)
