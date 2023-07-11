#!/usr/bin/python3

"""
This module contains a function that appends a string at the end of a
text file
"""


def append_write(filename="", text=""):
    """
    This function appends a string at eh end of a text file
    :param filename:
    :param text:
    :return: The number of characters added
    """

    with open(filename, mode="a", encoding="utf") as text_file:
        return text_file.write(text)
