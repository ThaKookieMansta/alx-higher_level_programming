#!/usr/bin/python3

def safe_print_integer_err(value):
    """
    This function Prints an integer
    :param value: The value, can be any type
    :return: True if value is integer
             False if it isn't
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as e:
        print("Exception: " + str(e))
        return False
