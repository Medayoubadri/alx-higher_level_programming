#!/usr/bin/python3
"""
Checks if an object is an instance of a class
that inherited from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited from a_class,
    otherwise returns False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a class that inherited from a_class,
        but not an instance of a_class itself.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
