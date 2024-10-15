#!/usr/bin/python3
"""
Defines a class BaseGeometry with an unimplemented area method.
"""


class BaseGeometry:
    """
    A class with a method area that raises an exception.
    """

    def area(self):
        """
        Raises an exception to indicate that area is not implemented.
        """
        raise Exception("area() is not implemented")
