#!/usr/bin/python3
"""
This module defines a square
Checks the data for integrity
then calculates the area
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
        self.size = size

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

        if type(value) is int or type(value) is float:
            pass
        else:
            raise TypeError("size must be a number")
        if int(value) < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        This method calculates the area of the square
        :return: The area
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Comparative method for equal to
        :param other:
        :return:
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Comparative method for not equal to
        :param other:
        :return:
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Comparative method for less than
        :param other:
        :return:
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Comparative method for less than or equal to
        :param other:
        :return:
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Comparative method for greater than
        :param other:
        :return:
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Comparative method for greater than or equal to
        :param other:
        :return:
        """
        return self.area() >= other.area()
