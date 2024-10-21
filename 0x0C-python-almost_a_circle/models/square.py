#!/usr/bin/python3
"""
This module defines the Square class, inheriting from Rectangle.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a Square, which is a special case of a Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square.
            x (int): The x position of the square. Defaults to 0.
            y (int): The y position of the square. Defaults to 0.
            id (int): The id of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return a string representation of the Square instance.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        Getter for the size attribute
        (which represents both width and height).
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.
        Assigns the same value to both width and height.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        self.width = value
        self.height = value
