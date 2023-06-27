#!/usr/bin/python3

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
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        if int(self.__size) < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        This method calculates the area of the square
        :return: The area
        """
        return self.__size ** 2
