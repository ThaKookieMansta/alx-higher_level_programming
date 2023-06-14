#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """
    A unction that returns a list with all values
    multiplied by a number
    :param my_list:
    :param number:
    :return:
    """
    return list(map(lambda x: x * number, my_list))
