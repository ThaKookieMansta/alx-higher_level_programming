#!/usr/bin/python3
def no_c(my_string):
    """
    This function removes all characters c and C from a string.
    :param my_string:
    :return:
    """
    my_new_string = ""
    for i in my_string:
        if i not in "cC":
            my_new_string += i
    return my_new_string
