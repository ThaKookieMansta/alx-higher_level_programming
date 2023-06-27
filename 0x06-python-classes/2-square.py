#!/usr/bin/python3
"""
This module defines the square and
checks the attributes for errors
"""


class Square:
    """
    This class defines a square
    """

    def __init__(self, size=0):
        """
        Initiation for the class Square
        :param size:
        :return:
        """
        self.__size = size
        if int(self.__size) < 0:
            raise ValueError("size must be >= 0")
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
