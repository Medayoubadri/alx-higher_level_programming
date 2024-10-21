#!/usr/bin/python3
"""
This module defines the Rectangle class, inheriting from Base.
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class for representing rectangles.
    Inherits from the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x position of the rectangle. Defaults to 0.
            y (int): The y position of the rectangle. Defaults to 0.
            id (int): The id of the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for the x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x attribute."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for the y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y attribute."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area value of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Prints the Rectangle instance with the character '#',
        considering the x and y offsets.
        """
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Return a string representation of the Rectangle instance.
        """
        return (
            f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
            f"{self.width}/{self.height}"
            )

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute based on the order of arguments.

        Args:
            *args (int): No-keyword arguments in the following order:
                        1st argument -> id attribute
                        2nd argument -> width attribute
                        3rd argument -> height attribute
                        4th argument -> x attribute
                        5th argument -> y attribute
            **kwargs (dict): Key-value pairs of attributes to be updated.
        """
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i, value in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle instance.

        Returns:
            dict: A dictionary with keys 'id', 'width', 'height', 'x', 'y'.
        """
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }
