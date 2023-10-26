import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import os


class TestBase(unittest.TestCase):
    def test_creation_with_id(self):
        """Vérifie si un objet est créé avec l'ID spécifié."""
        obj = Base(1)
        self.assertEqual(obj.id, 1)

    def test_creation_without_id(self):
        """Vérifie que la classe Base attribue automatiquement des IDs
        incrémentiels aux objets créés."""
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_private_nb_objects_no_direct_access(self):
        """S'assure qu'il n'y a pas d'accès direct à l'attribut privé
        __nb_objects."""
        obj1 = Base()
        with self.assertRaises(AttributeError):
            obj1.__nb_objects

    def test_to_json_string_with_data(self):
        """Vérifie que la méthode to_json_string convertit correctement des
        données en format JSON."""
        data = [{'key1': 'value1', 'key2': 'value2'}]
        json_str = Base.to_json_string(data)
        self.assertEqual(json_str, json.dumps(data))

    def test_to_json_string_with_empty_data(self):
        """Vérifie que to_json_string gère correctement une liste vide."""
        data = []
        json_str = Base.to_json_string(data)
        self.assertEqual(json_str, "[]")

    def test_to_json_string_with_none_data(self):
        """Vérifie que to_json_string gère correctement une valeur None."""
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")

    def test_save_to_file_with_empty_data(self):
        """Vérifie la sauvegarde de données JSON dans un fichier et leur
        lecture pour vérifier l'intégrité des données."""
        data = []
        filename = "Base.json"
        Base.save_to_file(data)
        with open(filename, 'r', encoding='utf-8') as file:
            saved_data = json.load(file)
            self.assertEqual(saved_data, [])

        os.remove(filename)

    def test_save_to_file_with_none_data(self):
        """Vérifie la gestion de la valeur None lors de la sauvegarde dans
        un fichier."""
        filename = "Base.json"

        Base.save_to_file(None)

        with open(filename, 'r', encoding='utf-8') as file:
            saved_data = json.load(file)
            self.assertEqual(saved_data, [])

        os.remove(filename)

    def test_from_json_string_with_data(self):
        """Vérifie que la méthode from_json_string peut convertir une chaîne
        JSON en une structure de données Python."""
        data = [{'key1': 'value1', 'key2': 'value2'}]
        json_str = json.dumps(data)
        loaded_data = Base.from_json_string(json_str)
        self.assertEqual(loaded_data, data)

    def test_from_json_string_with_empty_data(self):
        """Vérifie que from_json_string gère correctement une chaîne
        JSON vide."""
        json_str = "[]"
        loaded_data = Base.from_json_string(json_str)
        self.assertEqual(loaded_data, [])

    def test_from_json_string_with_none_data(self):
        """Vérifie que from_json_string gère correctement la valeur None."""
        loaded_data = Base.from_json_string(None)
        self.assertEqual(loaded_data, [])

    def test_init_with_non_integer_id(self):
        """Vérifie que la classe Base génère une exception lorsque l'ID n'est
        pas un entier."""
        with self.assertRaises(TypeError):
            base = Base("invalid_id")

    def test_init_with_negative_id(self):
        """Vérifie que la classe Base génère une exception lorsque l'ID est
        négatif."""
        with self.assertRaises(ValueError):
            base = Base(-5)

    def test_init_with_zero_id(self):
        """Vérifie que la classe Base accepte un ID de zéro."""
        base = Base(0)
        self.assertEqual(base.id, 0)

    def test_init_with_maximum_id(self):
        """Vérifie que la classe Base accepte un ID maximum autorisé."""
        base = Base(2**31 - 1)
        self.assertEqual(base.id, 2**31 - 1)

    def test_set_id_to_maximum_value(self):
        """Vérifie que la classe Base accepte de définir l'ID à la valeur
        maximale autorisée."""
        base = Base()
        base.id = 2**31 - 1
        self.assertEqual(base.id, 2**31 - 1)

# ---------------------------------------------------------------------- #

    def test_id_none(self):
        """Sending no id"""
        Base._Base__nb_objects = 0
        b = Base()
        self.assertEqual(1, b.id)

    def test_id(self):
        """Sending a valid id"""
        b = Base(50)
        self.assertEqual(50, b.id)

    def test_id_zero(self):
        """Sending an id 0"""
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_id_negative(self):
        """Sending a negative id"""
        with self.assertRaises(ValueError):
            b = Base(-20)

    def test_id_string(self):
        """Sending an id that is not an int"""
        with self.assertRaises(TypeError):
            b = Base("Betty")

    def test_id_dict(self):
        """Sending an id that is not an int"""
        b = Base(109)
        self.assertEqual(109, b.id)

    def test_id_tuple(self):
        """Sending an id that is not an int"""
        with self.assertRaises(TypeError):
            b = Base((8,))

    def test_to_json_type(self):
        """Testing the json string"""
        sq = Square(1)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(type(json_string), str)

    def test_to_json_value(self):
        """Testing the json string"""
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(
            json.loads(json_string), [{"id": 609, "y": 0, "size": 1, "x": 0}]
        )

    def test_to_json_None(self):
        """Testing the json string"""
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_Empty(self):
        """Testing the json string"""
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

# ---------------------------------------------------------------------- #

if __name__ == "__main__":
    unittest.main()
