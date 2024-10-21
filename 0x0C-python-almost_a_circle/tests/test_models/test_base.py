#!/usr/bin/python3
"""
Unit tests for the Base class.
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test the functionality of the Base class.
    """

    def setUp(self):
        """
        Reset the __nb_objects counter before each test.
        """
        Base._Base__nb_objects = 0

    def test_auto_id_assignment(self):
        """
        Test if IDs are automatically assigned when not provided.
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_manual_id_assignment(self):
        """
        Test if manual IDs are correctly assigned.
        """
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_mixed_auto_and_manual_id_assignment(self):
        """
        Test the combination of manual and automatic ID assignment.
        """
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 12)
        self.assertEqual(b3.id, 2)


if __name__ == "__main__":
    unittest.main()
