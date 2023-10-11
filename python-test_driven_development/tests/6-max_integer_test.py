#!/usr/bin/python3
import unittest

"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """

    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result

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

if __name__ == '__main__':
    unittest.main()
