#!/usr/bin/python3
"""
Module that defines a class `Square` with a getter and setter for size.
"""


class Square:
    """
    A class that defines a square by its size, and calculates area.
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
        self.size = size

    @property
    def size(self):
        """
        Gets the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.
        Args:
            value (int): The size of the square.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the current square area.
        """
        return self.__size**2
