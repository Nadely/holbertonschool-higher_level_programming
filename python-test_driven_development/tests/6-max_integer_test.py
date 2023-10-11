#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_list_is_empty(self):
        result = max_integer([])
        self.assertEqual(result, None)

    def test_integer_is_identical(self):
        result = max_integer([4, 4, 4, 4])
        self.assertEqual(result, 4)

    def test_max_integer_bis(self):
        result = max_integer([1, 2, 4, 3])
        self.assertEqual(result, 4)

    def test_max_integer_reverse(self):
        result = max_integer([4, 3, 2, 1])
        self.assertEqual(result, 4)

    def test_max_integer_opose(self):
        result = max_integer([1, 4])
        self.assertEqual(result, 4)

    def test_max_integer_min(self):
        result = max_integer([-1])
        self.assertEqual(result, -1)

