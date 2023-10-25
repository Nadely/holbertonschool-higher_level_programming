import unittest
from models.base import Base
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

if __name__ == "__main__":
    unittest.main()
