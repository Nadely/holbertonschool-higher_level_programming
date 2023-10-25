import unittest
from models.square import Square
import json
import os
import sys
from io import StringIO

class TestSquare(unittest.TestCase):
    def test_square_initialization(self):
        obj = Square(3)
        self.assertEqual(obj.size, 3)

    def test_square_initialization_invalid(self):
        with self.assertRaises((TypeError, ValueError)):
            invalid_square_1 = Square("invalid", 0, 0)
            invalid_square_2 = Square(2, -1, 1)
            invalid_square_3 = Square(2, 3, "invalid")

    def test_update(self):
        obj = Square(3)
        obj.update(4, 5, 2, 2)
        self.assertEqual(obj.id, 4)
        self.assertEqual(obj.size, 5)
        self.assertEqual(obj.x, 2)
        self.assertEqual(obj.y, 2)
        with self.assertRaises((TypeError, ValueError)):
            obj.update("invalid", 5, 2, 2)
            obj.update(4, -5, 1, 1)


    def test_to_dictionary(self):
        obj = Square(3, 1, 1, 4)
        obj_dict = obj
