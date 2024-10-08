#!/usr/bin/python3
"""
Module that defines a `MagicClass` matching the behavior of given bytecode.
"""

import math


class MagicClass:
    """
    A class that represents a circle with methods to calculate its area
    and circumference.
    """

    def __init__(self, radius=0):
        """
        Initializes a MagicClass instance with a given radius.
        Args:
            radius (int or float): The radius of the circle, default is 0.
        Raises:
            TypeError: If radius is not a number (int or float).
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculates the area of the circle.
        Returns:
            float: The area of the circle.
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """
        Calculates the circumference of the circle.
        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
