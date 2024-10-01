#!/usr/bin/python3
"""
Module that defines a class `Square` with size attribute
and provides comparison functionality.
"""


class Square:
    """
    A class that defines a square by its size.
    Supports area calculation and comparison based on area.
    """

    def __init__(self, size=0):
        """
        Initializes a new square with size validation.
        Args:
            size (int or float): The size of the square, default is 0.
        Raises:
            TypeError: If size is not a number.
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
            value (int or float): The size of the square.
        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the current square area.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Defines the behavior of the == operator.
        Compares the area of two squares.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return NotImplemented

    def __ne__(self, other):
        """
        Defines the behavior of the != operator.
        Compares the area of two squares.
        """
        if isinstance(other, Square):
            return self.area() != other.area()
        return NotImplemented

    def __lt__(self, other):
        """
        Defines the behavior of the < operator.
        Compares the area of two squares.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """
        Defines the behavior of the <= operator.
        Compares the area of two squares.
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented

    def __gt__(self, other):
        """
        Defines the behavior of the > operator.
        Compares the area of two squares.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """
        Defines the behavior of the >= operator.
        Compares the area of two squares.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented
