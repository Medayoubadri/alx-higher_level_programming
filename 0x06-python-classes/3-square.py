#!/usr/bin/python3
"""
Module that defines a class `Square` which includes an area method.
"""


class Square:
    """
    A class that defines a square by its size and calculates its area.
    """

    def __init__(self, size=0):
        """
        Initializes a new square with size validation.
        Args:
            size (int): The size of the square, default is 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the current square area.
        """
        return self.__size**2