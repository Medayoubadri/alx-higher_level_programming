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

    def update(self, *args, **kwargs):
        """
        Assigns attributes based on *args or **kwargs.

        Args:
            *args (int): No-keyword arguments in the following order:
                        1st argument -> id attribute
                        2nd argument -> size attribute
                        3rd argument -> x attribute
                        4th argument -> y attribute
            **kwargs (dict): Key-value pairs of attributes to be updated.
        """
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for i, value in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Square instance.

        Returns:
            dict: A dictionary with keys 'id', 'size', 'x', 'y'.
        """
        return {
            'id': self.id,
            'x': self.x,
            'size': self.width,
            'y': self.y
        }
