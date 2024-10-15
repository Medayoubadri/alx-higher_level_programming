#!/usr/bin/python3
"""
Defines a class BaseGeometry with area and integer_validator methods.
"""


class BaseGeometry:
    """
    A class with an unimplemented area method and an integer validator.
    """

    def area(self):
        """
        Raises an exception to indicate that area is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the value is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
