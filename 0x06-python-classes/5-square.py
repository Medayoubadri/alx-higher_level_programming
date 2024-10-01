#!/usr/bin/python3
"""
Module that defines a class `Square` and prints the square.
"""


class Square:
    """
    A class that defines a square by its size, calculates area, and prints the square.
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
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size**2

    def my_print(self):
        """
        Prints the square with the character `#`.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
