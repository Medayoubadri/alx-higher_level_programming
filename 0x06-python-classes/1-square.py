#!/usr/bin/python3
"""
Module that defines a class `Square` with a private attribute.
"""


class Square:
    """
    A class that defines a square by its size.
    """

    def __init__(self, size):
        """
        Initializes a new square.
        Args:
            size (int): The size of the square.
        """
        self.__size = size
