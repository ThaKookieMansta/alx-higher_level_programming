#!/usr/bin/python3

"""
This module has a class Square
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    This class inherits from the class Rectangle
    """

    def __init__(self, size):
        """
        This magic method instantiates the class variables
        :param size:
        """
        self.integer_validator(name="size", value=size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        This magic method returns fancy text when called
        :return: Fancy text
        """
        return f"[Square] {self.__size}/{self.__size}"
