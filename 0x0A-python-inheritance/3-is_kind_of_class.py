#!/usr/bin/python3
"""
Checks if an object is an instance of, or inherited from, a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of or
    inherited from a_class, else False.

    Args:
        obj: The object to check.
        a_class: The class or superclass to compare against.

    Returns:
        True if obj is an instance or inherited from a_class, False otherwise.
    """
    return isinstance(obj, a_class)
