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
        self.size = size
        self.position = position

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
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
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
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """
        Make the output printable
        :return:
        """
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ""
