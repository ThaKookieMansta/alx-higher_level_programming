#!/usr/bin/python3

"""
This module contains the rectangle class
"""
from .base import Base


class Rectangle(Base):
    """
    This is the Rectangle class that inherits from
    the bse class. This class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        This method instantiates the class instances.
        :param width:
        :param height:
        :param x:
        :param y:
        :param id:
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # This section of the class contains all the getters

    @property
    def width(self):
        """
        This is a getter method for the width attribute
        :return: The value of the private width attribute
        """
        return self.__width

    @property
    def height(self):
        """
        This method is the getter for the height attribute
        :return: The value of the Private height attribute
        """
        return self.__height

    @property
    def x(self):
        """
        This method is the getter for the X attribute
        :return: The value of the private x attribute
        """
        return self.__x

    @property
    def y(self):
        """
        This method is the getter for the y attribute
        :return: The value of the private y attribute
        """
        return self.__y

    # This section of the class contains the setters of the attributes

    @width.setter
    def width(self, width):
        """
        This is the setter method for Width
        :param width: Of the Rectangle
        :return:
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 1:
            raise ValueError("width must be > 0")

        self.__width = width

    @height.setter
    def height(self, height):
        """
        This is the setter method for height
        :param height: Of the Rectangle
        :return:
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 1:
            raise ValueError("height must be > 0")

        self.__height = height

    @x.setter
    def x(self, x):
        """
        This is the setter method for x
        :param x: coordinate of the Rectangle
        :return:
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

    @y.setter
    def y(self, y):
        """
        This is the setter method for y
        :param y: coordinate of the Rectangle
        :return:
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__y = y

    # This section of the class contains the functional methods

    def area(self):
        """
        This method calculates the area of the Rectangle
        :return: The area of the Rectangle instance
        """
        return self.__width * self.__height

    def display(self):
        """
        This method prints the Rectangle instance on the stdout
        :return:
        """
        print("\n" * self.__y)
        for i in range(self.__height):
            print((" " * self.__x) + ("#" * self.__width))

    def __str__(self):
        """
        This magic method defines how fancy text will be displayed
        :return: The fancy text
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - " \
               f"{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """
        This method updates the instance attributes
        :param args:
        :return:
        """
        attr_updates = ["id", "width", "height", "x", "y"]
        if args:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                if key in attr_updates:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        This method returns a dictionary representation
        of a rectangle instance
        :return: A dictionary representation
        """
        dict_data = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }

        return dict_data
