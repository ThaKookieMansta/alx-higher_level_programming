#!/usr/bin/python3
"""
This module defines a square
Checks the data for integrity
then calculates the area
Then draws the square
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

    @property
    def size(self):
        """
        Getter function for size attribute
        :return:
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter Function for size attribute
        :param value:
        :return:
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if int(value) < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        This method calculates the area of the square
        :return: The area
        """
        return self.__size ** 2

    def my_print(self):
        """
        A print function
        :return:
        """
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()