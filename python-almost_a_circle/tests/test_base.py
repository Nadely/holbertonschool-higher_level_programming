import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import os
import sys
from io import StringIO

class TestBase(unittest.TestCase):
    def test_base_initialization(self):
        obj = Base(1)
        self.assertEqual(obj.id, 1)

    def test_base_not_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_to_json_string(self):
        obj = Base(1)
        json_string = Base.to_json_string([obj.to_dictionary()])
        self.assertIsInstance(json_string, str)

    def test_save_to_file(self):
        obj1 = Base(1)
        obj2 = Base(2)
        filename = "test_objects.json"
        Base.save_to_file([obj1, obj2], filename)
        with open(filename, 'r', encoding='utf-8') as file:
            loaded_json = file.read()
        self.assertEqual(loaded_json, '[{"id": 1}, {"id": 2}]')

    def test_from_json_string(self):
        json_string = '[{"id": 1}, {"id": 2}]'
        objects = Base.from_json_string(json_string)
        self.assertIsInstance(objects, list)
        self.assertEqual(len(objects), 2)
        self.assertEqual(objects[0]['id'], 1)
        self.assertEqual(objects[1]['id'], 2)

    def test_create(self):
        obj_dict = {"id": 3, "x": 0, "y": 0}
        obj = Base.create(**obj_dict)
        self.assertIsInstance(obj, Base)
        self.assertEqual(obj.id, 3)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)

    def test_load_from_file(self):
        filename = "test_objects.json"
        objects = Base.load_from_file(filename)
        self.assertIsInstance(objects, list)
        self.assertEqual(len(objects), 2)
        self.assertEqual(objects[0].id, 1)
        self.assertEqual(objects[1].id, 2)

    def test_exception_handling(self):
        with self.assertRaises(FileNotFoundError):
            Base.load_from_file("nonexistent.json")
        with self.assertRaises(ValueError):
            invalid_obj = Base("invalid")

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

if __name__ == "__main__":
    unittest.main()
