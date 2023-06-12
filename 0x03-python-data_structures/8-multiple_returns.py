#!/usr/bin/python3

def multiple_returns(sentence):
    """
    A function that returns a tuple with the length of a string and its
    first character.
    :param sentence:
    :return:
    """
    fc = ""
    my_length = len(sentence)
    if my_length == 0:
        fc = None
    else:
        fc = sentence[0]

    return my_length, fc,
