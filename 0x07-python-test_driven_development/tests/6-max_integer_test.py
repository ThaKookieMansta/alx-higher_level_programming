#!/usr/bin/python3
"""unitest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Class for testing the max integer module
    """

    def test_max_integer(self):
        """
        This tests for normal operation of the module
        :return:
        """
        input_list = [25, 78,14,37,62,81,99]
        self.assertEqual(max_integer(input_list), 99)

    def test_negative_max_integer(self):
        """
        This tests for when the max integer is negative
        :return:
        """
        input_list = [50, -55, -16, 26, 79, -40]
        self.assertEqual(max_integer(input_list), 79)

    def test_floats_max_integer(self):
        """
        This tests for when the numbers are floats
        :return:
        """
        input_list = [12.5, 15, 59.3, 22, -10]
        self.assertEqual(max_integer(input_list), 59.3)

    def test_empty_list_max_integer(self):
        """
        This tests for when the list is empty
        :return:
        """
        input_list = []
        self.assertEqual(max_integer(input_list), None)

    def test_first_max_integer(self):
        """
        This tests if the function will work if the first
        integer is the max in the list
        :return:
        """
        input_list = [15, 5, 6, 1, 8]
        self.assertEqual(max_integer(input_list), 15)

    def test_last_max_integer(self):
        """
        This tests if the function will work if the last
        integer is the highest in the list
        :return:
        """
        input_list = [2,6,1,76,99]
        self.assertEqual(max_integer(input_list), 99)

    def test_only_max_integer(self):
        """
        This tests if the function will work
        with only 1 integer in the list
        :return:
        """
        self.assertEqual(max_integer([12]), 12)



