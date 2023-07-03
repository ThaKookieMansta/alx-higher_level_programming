#!/usr/bin/python3
"""
This class defines a rectangle
"""


class Rectangle:
    """
    This class defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        This is the instantiation method for the class
        :param height: Height of rectangle
        :param width: width of rectangle
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        This is the getter method for the protected
        attribute width
        :return:
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        This is the setter method for the private attribute
        width
        :param value:
        :return:
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        This is the getter attribute for the private
        attribute height
        :return: The private attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        This is the setter method for the private
        attribute height
        :param value:
        :return:
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
