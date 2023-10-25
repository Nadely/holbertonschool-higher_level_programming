import unittest
from models.square import Square
import json
import os
import sys
from io import StringIO

class TestSquare(unittest.TestCase):
    def setUp(self):
        """Initializing instance with width and height
        parameters"""
        self.s = Square(5)

    def tearDown(self):
        """Deleting created instance"""
        try:
            os.remove("Square.json")
        except:
            pass
        del self.s

    def test_init_with_valid_values(self):
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    def test_init_with_invalid_size(self):
        with self.assertRaises(ValueError):
            square = Square(0)

    def test_set_size_with_valid_value(self):
        square = Square(5)
        square.size = 10
        self.assertEqual(square.size, 10)

    def test_set_size_with_invalid_value(self):
        square = Square(5)
        with self.assertRaises(ValueError):
            square.size = -5

    def test_str(self):
        square = Square(5, 2, 3, 1)
        self.assertEqual(str(square), "[Square] (1) 2/3 - 5")

    def test_update_with_args(self):
        square = Square(5)
        square.update(1, 10, 2, 3)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_update_with_kwargs(self):
        square = Square(5)
        square.update(id=1, size=10, x=2, y=3)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_to_dictionary(self):
        square = Square(5, 2, 3, 1)
        square_dict = square.to_dictionary()
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(square_dict, expected_dict)


    def test_square_init_with_valid_values(self):
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    def test_square_init_with_invalid_size(self):
        with self.assertRaises(ValueError):
            square = Square(0)

    def test_square_set_size_with_valid_value(self):
        square = Square(5)
        square.size = 10
        self.assertEqual(square.size, 10)

    def test_square_set_size_with_invalid_value(self):
        square = Square(5)
        with self.assertRaises(ValueError):
            square.size = -5

    def test_square_str(self):
        square = Square(5, 2, 3, 1)
        self.assertEqual(str(square), "[Square] (1) 2/3 - 5")

    def test_square_update_with_args(self):
        square = Square(5)
        square.update(1, 10, 2, 3)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_square_update_with_kwargs(self):
        square = Square(5)
        square.update(id=1, size=10, x=2, y=3)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_square_to_dictionary(self):
        square = Square(5, 2, 3, 1)
        square_dict = square.to_dictionary()
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(square_dict, expected_dict)


    def test_square_init_with_valid_values(self):
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    def test_square_init_with_invalid_size(self):
        with self.assertRaises(ValueError):
            square = Square(0)

    def test_square_set_size_with_valid_value(self):
        square = Square(5)
        square.size = 10
        self.assertEqual(square.size, 10)

    def test_square_set_size_with_invalid_value(self):
        square = Square(5)
        with self.assertRaises(ValueError):
            square.size = -5

    def test_square_str(self):
        square = Square(5, 2, 3, 1)
        self.assertEqual(str(square), "[Square] (1) 2/3 - 5")

    def test_square_update_with_args(self):
        square = Square(5)
        square.update(1, 10, 2, 3)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_square_update_with_kwargs(self):
        square = Square(5)
        square.update(id=1, size=10, x=2, y=3)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_square_to_dictionary(self):
        square = Square(5, 2, 3, 1)
        square_dict = square.to_dictionary()
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(square_dict, expected_dict)

if __name__ == "__main__":
    unittest.main()
