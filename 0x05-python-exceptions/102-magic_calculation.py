#!/usr/bin/python3

def magic_calculation(a, b):
    """
    This python code imitates a python bytecode
    :param a:
    :param b:
    :return:
    """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise ValueError("Too far")
            else:
                result += (a ** b) / 1
        except ValueError:
            result = b + a
            break
    return result
