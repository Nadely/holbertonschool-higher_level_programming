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
        #Vérifie que la classe Base attribue automatiquement des IDs
        # incrémentiels aux objets créés.
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_private_nb_objects_no_direct_access(self):
        #S'assure qu'il n'y a pas d'accès direct à l'attribut privé
        # __nb_objects.
        obj1 = Base()
        with self.assertRaises(AttributeError):
            obj1.__nb_objects

    #Vérifient que la méthode to_json_string convertit correctement
    # des données en format JSON.
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

    #Testent la sauvegarde de données JSON dans un fichier et leur lecture
    # pour vérifier l'intégrité des données.
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

    #Vérifient que la méthode from_json_string peut convertir une chaîne
    # JSON en une structure de données Python.
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




    def test_init_with_non_integer_id(self):
        with self.assertRaises(TypeError):
            base = Base("invalid_id")

    def test_init_with_negative_id(self):
        with self.assertRaises(ValueError):
            base = Base(-5)

    def test_init_with_zero_id(self):
        base = Base(0)
        self.assertEqual(base.id, 0)

    def test_init_with_maximum_id(self):
        base = Base(2**31 - 1)
        self.assertEqual(base.id, 2**31 - 1)

    def test_set_id_to_maximum_value(self):
        base = Base()
        base.id = 2**31 - 1
        self.assertEqual(base.id, 2**31 - 1)

if __name__ == "__main__":
    unittest.main()
