#!/usr/bin/python3
"""
Unit tests for the Base class.
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle


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

    def test_to_json_string(self):
        """
        Test the to_json_string method of the Base class.
        """
        dictionaries = [{'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}]
        json_str = Base.to_json_string(dictionaries)
        expected_str = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        self.assertEqual(json_str, expected_str)
        self.assertEqual(type(json_str), str)

        self.assertEqual(Base.to_json_string(None), "[]")

        self.assertEqual(Base.to_json_string([]), "[]")

    def test_save_to_file(self):
        """
        Test the save_to_file method of the Base class.
        """
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            file_content = file.read()
            expected_output = (
                '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}, '
                '{"x": 0, "y": 0, "id": 2, "height": 4, "width": 2}]'
            )
            self.assertEqual(file_content, expected_output)

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_from_json_string(self):
        """
        Test the from_json_string method of the Base class.
        """
        json_str = (
            '[{"height": 4, "width": 10, "id": 89}, '
            '{"height": 7, "width": 1, "id": 7}]'
            )
        expected_list = [
            {"height": 4, "width": 10, "id": 89},
            {"height": 7, "width": 1, "id": 7}
        ]
        self.assertEqual(Base.from_json_string(json_str), expected_list)
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string(None), [])

    def test_create(self):
        """
        Test the create method of the Base class.
        """
        from models.square import Square
        rect_dict = {'id': 1, 'width': 3, 'height': 5, 'x': 1, 'y': 0}
        r1 = Rectangle.create(**rect_dict)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 0)

        square_dict = {'id': 2, 'size': 4, 'x': 2, 'y': 1}
        s1 = Square.create(**square_dict)
        self.assertEqual(s1.id, 2)
        self.assertEqual(s1.size, 4)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 1)

    def test_load_from_file(self):
        """
        Test the load_from_file method of the Base class.
        """
        from models.square import Square
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])

        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(len(list_rectangles_output), 2)

        self.assertEqual(
            list_rectangles_output[0].to_dictionary(),
            r1.to_dictionary()
            )
        self.assertEqual(
            list_rectangles_output[1].to_dictionary(),
            r2.to_dictionary()
            )

        s1 = Square(5, 0, 0, 5)
        s2 = Square(7, 9, 1, 6)
        Square.save_to_file([s1, s2])

        list_squares_output = Square.load_from_file()
        self.assertEqual(len(list_squares_output), 2)

        self.assertEqual(
            list_squares_output[0].to_dictionary(),
            s1.to_dictionary()
            )
        self.assertEqual(
            list_squares_output[1].to_dictionary(),
            s2.to_dictionary()
            )

        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        empty_list = Rectangle.load_from_file()
        self.assertEqual(empty_list, [])


if __name__ == "__main__":
    unittest.main()
