#!/usr/bin/python3

"""
This module prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    This function prints text with a double new line
    after each of these characters: ., ? and :
    :param text: The text to print
    :return:
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    txt_output = text.replace('.', '.\n\n').replace(':', ':\n\n') \
        .replace('?', '?\n\n')
    for i in range(len(text)):
        txt_output = txt_output.replace('\n ', '\n')

    print(txt_output, end='')


