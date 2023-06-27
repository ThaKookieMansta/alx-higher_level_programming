#!/usr/bin/python3
"""
This module has the classes Node and Singlylinkedlist
"""


class Node:
    """
    This defines the node object
    """

    def __init__(self, data, next_node=None):
        """
        Instantiation of the attributes
        :param data:
        :param next_node:
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
        Getter method for data
        :return:
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        setter method for data
        :param value:
        :return:
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter method for next node
        :return:
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        setter method for next node
        :param value:
        :return:
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    This class defines a singly linked list object
    """

    def __init__(self):
        """
        Simple instantiation
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new node to the list
        :param value:
        :return:
        """

        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current_node = self.__head
            while (current_node.next_node is not None and
                   current_node.next_node.data < value):
                current_node = current_node.next_node
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node

    def __str__(self):
        """
        Creating a printable format
        :return:
        """
        values = []
        current_node = self.__head
        while current_node is not None:
            values.append(str(current_node.data))
            current_node = current_node.next_node
        return '\n'.join(values)
