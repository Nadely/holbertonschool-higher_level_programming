import unittest
from models.rectangle import Rectangle
import json
import os
import sys
from io import StringIO

class TestRectangle(unittest.TestCase):
    def test_rectangle_initialization(self):
        obj = Rectangle(2, 4)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 4)

    def test_rectangle_initialization_invalid(self):
        with self.assertRaises((TypeError, ValueError)):
            invalid_rect_1 = Rectangle("invalid", 4, 2, 2)
            invalid_rect_2 = Rectangle(2, -3, 1, 1)
            invalid_rect_3 = Rectangle(2, 3, "invalid", 0)
            invalid_rect_4 = Rectangle(2, 3, -1, -2)

    def test_area(self):
        obj = Rectangle(3, 5)
        self.assertEqual(obj.area(), 15)

    def test_display(self):
        obj = Rectangle(2, 2)
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            obj.display()
            display_output = mock_stdout.getvalue()
            self.assertEqual(display_output, "##\n##\n")

    def test_update(self):
        obj = Rectangle(2, 3)
        obj.update(4, 5, 1, 1, 6)
        self.assertEqual(obj.id, 4)
        self.assertEqual(obj.width, 5)
        self.assertEqual(obj.height, 1)
        self.assertEqual(obj.x, 1)
        self.assertEqual(obj.y, 6)

    def test_to_dictionary(self):
        obj = Rectangle(2, 3, 1, 1, 4)
        obj_dict = obj.to_dictionary()
        expected_dict = {'id': 4, 'width': 2, 'height': 3, 'x': 1, 'y': 1}
        self.assertDictEqual(obj_dict, expected_dict)

    def test_exception_handling(self):
        with self.assertRaises(ValueError):
            invalid_rectangle = Rectangle(2, -4)

if __name__ == "__main__":
    unittest.main()
