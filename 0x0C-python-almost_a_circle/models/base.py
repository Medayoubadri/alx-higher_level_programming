#!/usr/bin/python3
"""
This module provides the Base class for other models to inherit from.
"""


class Base:
    """
    The Base class from which other classes will inherit.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base instance.

        Args:
            id (int): The id for the instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
