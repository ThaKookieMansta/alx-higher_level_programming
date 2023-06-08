#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    arguments_length = len(argv) - 1
    print("{:d} arguments".format(arguments_length), end="")
    if arguments_length == 0:
        print(".")
    else:
        print(":")
        counter = 1
        for i in argv[1:]:
            print("{:d}: {}".format(counter, i))
            counter += 1
