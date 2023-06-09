#!/usr/bin/python3


"""
This module contains a class Student
"""


class Student:
    """
    The Class Student
    """

    def __init__(self, first_name, last_name, age):
        """
        This function instantiates the class variables
        :param first_name:
        :param last_name:
        :param age:
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        This function retrieves a dictionary representation
        of a Student instance
        :param attrs:
        :return:
        """
        if type(attrs) == list and all(type(x) == str for x in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
