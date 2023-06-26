#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
    This function executes a function safely
    :param fct: The pointer to the function
    :param args: The arguments
    :return: Result of the function
    """
    try:
        result = fct(*args)
        return result
    except (ZeroDivisionError, TypeError, ValueError, IndexError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
