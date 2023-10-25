import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import os
import sys
from io import StringIO

class TestBase(unittest.TestCase):
    def test_creation_with_id(self):
        #Checks if an object is created with the specified ID.
        obj = Base(1)
        self.assertEqual(obj.id, 1)

    def test_creation_without_id(self):
        #Checks if objects are created with auto-incrementing IDs when no ID
        # is provided.
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_private_nb_objects_no_direct_access(self):
        #Ensures that there is no direct access to the private __nb_objects
        # attribute
        obj1 = Base()
        with self.assertRaises(AttributeError):
            obj1.__nb_objects

    def test_to_json_string_with_data(self):
        data = [{'key1': 'value1', 'key2': 'value2'}]
        json_str = Base.to_json_string(data)
        self.assertEqual(json_str, json.dumps(data))

    def test_to_json_string_with_empty_data(self):
        data = []
        json_str = Base.to_json_string(data)
        self.assertEqual(json_str, "[]")

    def test_to_json_string_with_none_data(self):
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")

    def test_save_to_file_with_empty_data(self):
        data = []
        filename = "Base.json"

        Base.save_to_file(data)

        with open(filename, 'r', encoding='utf-8') as file:
            saved_data = json.load(file)
            self.assertEqual(saved_data, [])

        os.remove(filename)

    def test_save_to_file_with_none_data(self):
        filename = "Base.json"

        Base.save_to_file(None)

        with open(filename, 'r', encoding='utf-8') as file:
            saved_data = json.load(file)
            self.assertEqual(saved_data, [])

        os.remove(filename)

    def test_from_json_string_with_data(self):
        data = [{'key1': 'value1', 'key2': 'value2'}]
        json_str = json.dumps(data)
        loaded_data = Base.from_json_string(json_str)
        self.assertEqual(loaded_data, data)

    def test_from_json_string_with_empty_data(self):
        json_str = "[]"
        loaded_data = Base.from_json_string(json_str)
        self.assertEqual(loaded_data, [])

    def test_from_json_string_with_none_data(self):
        loaded_data = Base.from_json_string(None)
        self.assertEqual(loaded_data, [])

    def test_create_with_attributes(self):
        data = {'attr1': 10, 'attr2': 'example'}
        instance = Base.create(**data)
        self.assertEqual(instance.attr1, 10)
        self.assertEqual(instance.attr2, 'example')

    def test_create_without_attributes(self):
        instance = Base.create()
        self.assertEqual(instance.attr1, 1)
        self.assertEqual(instance.attr2, 1)

    def test_load_from_file_with_data(self):
        data = [{'attr1': 10, 'attr2': 'example'}, {'attr1': 20, 'attr2': 'test'}]
        filename = "Base.json"

        # Create a JSON file with the test data
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(json.dumps(data))

        instances = Base.load_from_file()

        self.assertEqual(len(instances), 2)
        self.assertEqual(instances[0].attr1, 10)
        self.assertEqual(instances[0].attr2, 'example')
        self.assertEqual(instances[1].attr1, 20)
        self.assertEqual(instances[1].attr2, 'test')

    def test_load_from_file_with_no_file(self):
        instances = Base.load_from_file()
        self.assertEqual(instances, [])

if __name__ == "__main__":
    unittest.main()
