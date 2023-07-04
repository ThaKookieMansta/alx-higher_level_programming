#!/usr/bin/python3
"""
Defines a locked class
"""


class LockedClass:
    """
    This prevents the user from instantiating
    a new LockedClass attribute
    """
    __slots__ = ["first_name"]
