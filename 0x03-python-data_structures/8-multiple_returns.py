#!/usr/bin/python3

def multiple_returns(sentence):
    """
    A function that returns a tuple with the length of a string and its
    first character.
    :param sentence:
    :return:
    """
    fc = ""
    if len(sentence) == 0:
        fc = None
    else:
        length = len(sentence)
        fc = sentence[0]
        sentence_tuple = (length, fc,)
        return sentence_tuple
