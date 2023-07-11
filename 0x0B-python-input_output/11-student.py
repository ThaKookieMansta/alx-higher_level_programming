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
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for i in attrs:
            try:
                new_dict[i] = self.__dict__[i]
            except FileNotFoundError:
                pass
        return new_dict

    def reload_from_json(self, json):
        """
        This function replaces all attributes of the Student instance
        :param json:
        :return:
        """
        for key in json:
            try:
                setattr(self, key, json[key])
            except FileNotFoundError:
                pass
