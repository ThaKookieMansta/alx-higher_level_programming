#!/usr/bin/python3
"""
This module contains a function that inserts a line of text to a file
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    This function inserts a line of text to a file, after
    each line containing a specific string
    :param filename:
    :param search_string:
    :param new_string:
    :return:
    """
    with open(filename, encoding='utf-8') as text_file:
        line_list = []
        while True:
            line = text_file.readline()
            if line == "":
                break
            line_list.append(line)
            if search_string in line:
                line_list.append(new_string)
    with open(filename, mode="w", encoding='utf-8') as text_file:
        text_file.writelines(line_list)
