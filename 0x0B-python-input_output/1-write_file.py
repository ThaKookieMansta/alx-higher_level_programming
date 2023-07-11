#!/usr/bin/python3

"""
This function writes a string to a text file
"""


def write_file(filename="", text=""):
    """
    This function writes a string to a text file
    :param filename:
    :param text:
    :return: the number of characters written
    """
    with open(filename, mode="w", encoding="utf") as text_file:
        return text_file.write(text)
