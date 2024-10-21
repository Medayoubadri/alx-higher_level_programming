#!/usr/bin/python3
"""
Unit tests for the Square class.
"""
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Tests the functionality of the Square class.
    """

    def setUp(self):
        """
        Reset the __nb_objects counter before each test.
        """
        Base._Base__nb_objects = 0

    def test_square_creation(self):
        """
        Test the creation and attributes of a Square instance.
        """
        s1 = Square(5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)

    def test_square_str(self):
        """
        Test the __str__ method of the Square instance.
        """
        s1 = Square(5, 2, 3, 10)
        self.assertEqual(str(s1), "[Square] (10) 2/3 - 5")

    def test_square_area(self):
        """
        Test the area calculation of the Square instance.
        """
        s1 = Square(4)
        self.assertEqual(s1.area(), 16)

    def test_square_display(self):
        """
        Test the display method of the Square instance.
        """
        s1 = Square(2, 2, 1)
        expected_output = "\n  ##\n  ##\n"

        from io import StringIO
        import sys

        captured_output = StringIO()
        sys.stdout = captured_output
        s1.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_square_size(self):
        """
        Test the getter and setter
        for the size attribute of the Square instance.
        """
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

        s1.size = 10
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)

        with self.assertRaises(TypeError):
            s1.size = "9"

        with self.assertRaises(ValueError):
            s1.size = -3

    def test_square_update(self):
        """
        Test the update method of the Square instance with *args and **kwargs.
        """
        s1 = Square(5)

        s1.update(10)
        self.assertEqual(s1.id, 10)

        s1.update(1, 2)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 2)

        s1.update(1, 2, 3)
        self.assertEqual(s1.x, 3)

        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.y, 4)

        s1.update(x=12)
        self.assertEqual(s1.x, 12)

        s1.update(size=7, y=1)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.y, 1)

        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.y, 1)


if __name__ == "__main__":
    unittest.main()
