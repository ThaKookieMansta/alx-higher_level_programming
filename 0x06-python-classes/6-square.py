#!/usr/bin/python3
"""
This module defines a square
Checks the data for integrity
then calculates the area
Then draws the square
adds the position of the square
"""


class Square:
    """
    This class defines a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initiation for the class Square
        :param size:
        :return:
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        Getter for the position attribute
        :return:
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter function for position attribute
        :param value:
        :return:
        """
        if type(value) != tuple and int(value[0]) > 0 and int(value[1]) > 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

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
        h = self.__size
        while h > 0:
            print(" " * self.__position[1] + "#" * self.__size)
            h -= 1
