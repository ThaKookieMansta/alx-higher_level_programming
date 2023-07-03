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
        attribute length
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

    def area(self):
        """
        A public instance method for the area of the
        rectangle
        :return: The area of the rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        A public instance method for the perimeter
        of the rectangle
        :return: The perimeter of the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        The printable format of the rectangle class
        :return: The rectangle
        """
        printout = ""
        if self.__width != 0 and self.__height != 0:
            printout += "\n".join("#" * self.__width
                                  for j in range(self.__height))
        return printout

    def __repr__(self):
        """
        The official printable version
        :return:
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints a string when a rectangle is deleted
        :return:
        """
        print("Bye rectangle...")
