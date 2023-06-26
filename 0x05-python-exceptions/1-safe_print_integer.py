#!/usr/bin/python3

def safe_print_integer(value):
    """
    This function prints integers with the "{:d}".format() format
    :param value: A variable of any type
    :return: Returns True if value has been correctly printed
    (If value is an integer)
    """
    try:
        print("{:d}".format(value))
        return True
    except TypeError:
        return False
