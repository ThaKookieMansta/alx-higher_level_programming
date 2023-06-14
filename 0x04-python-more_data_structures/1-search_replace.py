#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    A function that replaces all occurrences of an element
    :param my_list:
    :param search:
    :param replace:
    :return:
    """
    return [item if item != search else replace for item in my_list]
