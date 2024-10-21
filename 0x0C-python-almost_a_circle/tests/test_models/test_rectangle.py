#!/usr/bin/python3
"""
Unit tests for the Rectangle class.
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base

from io import StringIO
import sys


class TestRectangle(unittest.TestCase):
    """
    Tests the functionality of the Rectangle class.
    """

    def setUp(self):
        """
        Reset the __nb_objects counter before each test.
        """
        Base._Base__nb_objects = 0

    def test_id_assignment(self):
        """
        Test if IDs are correctly assigned to Rectangle instances.
        """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    def test_attribute_validation(self):
        """
        Test the validation of attribute values.
        """
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)

    def test_area(self):
        """
        Test the area calculation of the Rectangle instance.
        """
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        """
        Test the display method of the Rectangle instance.
        """
        r1 = Rectangle(4, 3)
        expected_output = "####\n####\n####\n"

        captured_output = StringIO()
        sys.stdout = captured_output
        r1.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_str_method(self):
        """
        Test the __str__ method of the Rectangle instance.
        """
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1)

        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")

    def test_display_with_offset(self):
        """
        Test the display method of the Rectangle instance
        with x and y offsets.
        """
        r1 = Rectangle(2, 3, 2, 2)
        expected_output_1 = "\n\n  ##\n  ##\n  ##\n"

        r2 = Rectangle(3, 2, 1, 0)
        expected_output_2 = " ###\n ###\n"

        captured_output = StringIO()
        sys.stdout = captured_output
        r1.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), expected_output_1)

        captured_output = StringIO()
        sys.stdout = captured_output
        r2.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), expected_output_2)

    def test_update_method(self):
        """
        Test the update method of the Rectangle instance with *args.
        """
        r1 = Rectangle(10, 10, 10, 10, 1)
        r1.update(89)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)

        r1.update(89, 2)
        self.assertEqual(r1.width, 2)

        r1.update(89, 2, 3)
        self.assertEqual(r1.height, 3)

        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.x, 4)

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.y, 5)


if __name__ == "__main__":
    unittest.main()
