#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        """Test when the list is empty"""
        self.assertIsNone(max_integer([]))

    def test_max_at_beginning(self):
        """Test when the max integer is at the beginning of the list"""
        self.assertEqual(max_integer([10, 5, 3, 2]), 10)

    def test_max_at_end(self):
        """Test when the max integer is at the end of the list"""
        self.assertEqual(max_integer([1, 5, 3, 10]), 10)

    def test_max_in_middle(self):
        """Test when the max integer is in the middle of the list"""
        self.assertEqual(max_integer([1, 10, 3, 2]), 10)

    def test_single_element_list(self):
        """Test when the list contains a single element"""
        self.assertEqual(max_integer([42]), 42)

    def test_all_equal_elements(self):
        """Test when all elements in the list are equal"""
        self.assertEqual(max_integer([3, 3, 3, 3, 3]), 3)

    def test_negative_numbers(self):
        """Test when the list contains negative numbers"""
        self.assertEqual(max_integer([-10, -5, -3, -2]), -2)

if __name__ == '__main__':
    unittest.main()
