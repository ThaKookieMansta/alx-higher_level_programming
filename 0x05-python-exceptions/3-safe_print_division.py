#!/usr/bin/python3
def safe_print_division(a, b):
    """
    This function divides 2 integers and prints teh result
    :param a: The first integer
    :param b: The second integer
    :return: The value of the division
    """
    result = 0
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        result = None
        return result
    finally:
        print("Inside result: {}".format(result))
