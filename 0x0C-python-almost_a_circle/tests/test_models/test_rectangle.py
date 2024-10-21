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


if __name__ == "__main__":
    unittest.main()
