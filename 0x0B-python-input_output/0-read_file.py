#!/usr/bin/python3

"""
This module contains a function that reads a text in UTF8 and
prints it to stdout
"""


def read_file(filename=""):
    """
    This function reads a file and prints it
    to stdout
    :param filename:
    :return:
    """
    with open(filename, encoding="utf-8") as text_file:
        print(text_file.read(), end="")
