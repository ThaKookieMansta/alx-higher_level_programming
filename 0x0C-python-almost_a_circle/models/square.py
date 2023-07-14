#!/usr/bin/python3

"""
This module contains the Square class for all
square instances that may be created
"""

from .rectangle import Rectangle


class Square(Rectangle):
    """
    This is the square class that inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        This method instantiates the Square instances
        :param size:
        :param x:
        :param y:
        :param id:
        """
        super().__init__(size, size, x, y, id )

    def __str__(self):
        """
        This magic method returns the fancy text for this class
        :return:
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        This is the getter method for size
        :return: The private setter attribute
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        This is the setter method for the size attribute
        :param size:
        :return:
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        This method updates attributes of the square
        :param args:
        :param kwargs:
        :return:
        """
        attr_updates = ["id", "size", "x", "y"]
        if args:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                if key in attr_updates:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        This method returns a dictionary representation
        of the square instance
        :return: The dictionary representation
        """
        dict_data = {
            "id" : self.id,
            "size" : self.size,
            "x" : self.x,
            "y" : self.y,
        }

        return dict_data
