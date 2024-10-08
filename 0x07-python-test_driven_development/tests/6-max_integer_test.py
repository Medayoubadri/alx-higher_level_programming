#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([10, 20, 30]), 30)
    
    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -20, -30]), -10)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)
    
    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)
    
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
    
    def test_none_input(self):
        with self.assertRaises(TypeError):
            max_integer(None)
    
    def test_string_input(self):
        # If input is a string, max should return the max character
        self.assertEqual(max_integer("string"), 't')

if __name__ == "__main__":
    unittest.main()
