#!/usr/bin/python3
"""
Module that defines a class `Square` with size and position attributes
and provides functionality to calculate area and print the square.
"""


class Square:
    """
    A class that defines a square by its size and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new square with size and position.
        Args:
            size(int): The size of the square, default is 0.
            position(tuple): A tuple of 2 positive integers, default is (0, 0).
        Raises:
            TypeError: If size is not an integer or position is not a tuple of
                       2 positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Gets the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square with validation.
        Args:
            value (tuple): A tuple of 2 positive integers representing the
                           position.
        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns the current square area.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character `#`.
        """
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):
            print("")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Defines the string representation of the square.
        Returns:
            A string representing the square with the character `#`.
        """
        if self.__size == 0:
            return ""

        result = []
        for _ in range(self.__position[1]):
            result.append("")
        for _ in range(self.__size):
            result.append(" " * self.__position[0] + "#" * self.__size)
        return "\n".join(result)
