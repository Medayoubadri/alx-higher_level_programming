#!/usr/bin/python3
"""
Returns the list of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Arg:
        obj (any): The object to inspect.

    Returns:
        List of attributes and methods.
    """
    return dir(obj)
