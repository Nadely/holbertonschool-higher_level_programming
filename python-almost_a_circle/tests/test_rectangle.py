import unittest
from models.rectangle import Rectangle
import json
import os
import sys
from io import StringIO

class TestRectangle(unittest.TestCase):
    def setUp(self):
        """Initializing instance with width and height
        parameters"""
        self.r = Rectangle(5, 10)

    def tearDown(self):
        """Deleting created instance"""
        del self.r

    def test_init_with_valid_values(self):
        #Teste la création d'une instance de Rectangle avec des valeurs
        # valides pour ses attributs.
        rect = Rectangle(10, 20, 2, 3, 1)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)
        self.assertEqual(rect.id, 1)

    def test_init_with_invalid_width(self):
        #Vérifient que des exceptions sont levées lorsque des valeurs
        # invalides sont utilisées pour initialiser les attributs.
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 20)

    def test_init_with_invalid_height(self):
        #Vérifient que des exceptions sont levées lorsque des valeurs
        # invalides sont utilisées pour initialiser les attributs.
        with self.assertRaises(ValueError):
            rect = Rectangle(10, -5)

    def test_init_with_invalid_x(self):
        #Vérifient que des exceptions sont levées lorsque des valeurs
        # invalides sont utilisées pour initialiser les attributs.
        with self.assertRaises(ValueError):
            rect = Rectangle(10, 20, -1)

    def test_init_with_invalid_y(self):
        #Vérifient que des exceptions sont levées lorsque des valeurs
        # invalides sont utilisées pour initialiser les attributs.
        with self.assertRaises(ValueError):
            rect = Rectangle(10, 20, 2, -1)

    #Testent la modification des attributs de largeur, hauteur, x et y
    # avec des valeurs valides.
    def test_set_width_with_valid_value(self):
        rect = Rectangle(10, 20)
        rect.width = 15
        self.assertEqual(rect.width, 15)

    def test_set_width_with_invalid_value(self):
        rect = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            rect.width = -5

    def test_area(self):
        #Vérifie que la méthode area renvoie la valeur correcte
        # de la zone de l'objet.
        rect = Rectangle(10, 20)
        self.assertEqual(rect.area(), 200)

    def test_str(self):
        #Vérifie que la méthode str renvoie une chaîne de caractères
        # correctement formatée pour représenter l'objet.
        rect = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(str(rect), "[Rectangle] (1) 2/3 - 5/10")

    #Testent les méthodes update pour mettre à jour les attributs de l'objet
    # à l'aide d'arguments positionnels ou de mots-clés.

    def test_update_with_args(self):
        rect = Rectangle(10, 20)
        rect.update(1, 15, 25, 3, 4)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 15)
        self.assertEqual(rect.height, 25)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_update_with_kwargs(self):
        rect = Rectangle(10, 20)
        rect.update(id=1, width=15, height=25, x=3, y=4)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 15)
        self.assertEqual(rect.height, 25)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_to_dictionary(self):
        #Vérifie que la méthode to_dictionary renvoie un dictionnaire
        # contenant les attributs de l'objet.
        rect = Rectangle(10, 20, 1, 2, 3)
        rect_dict = rect.to_dictionary()
        expected_dict = {'id': 3, 'width': 10, 'height': 20, 'x': 1, 'y': 2}
        self.assertEqual(rect_dict, expected_dict)


    def test_rectangle_init_with_valid_values(self):
        rect = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)
        self.assertEqual(rect.id, 1)

    def test_rectangle_init_with_invalid_width(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 10)

    def test_rectangle_set_width_with_valid_value(self):
        rect = Rectangle(5, 10)
        rect.width = 15
        self.assertEqual(rect.width, 15)

    def test_rectangle_set_width_with_invalid_value(self):
        rect = Rectangle(5, 10)
        with self.assertRaises(ValueError):
            rect.width = -5

    # Add similar tests for height, x, and y setters

    def test_rectangle_area(self):
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

    def test_rectangle_str(self):
        rect = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(str(rect), "[Rectangle] (1) 2/3 - 5/10")

    def test_rectangle_update_with_args(self):
        rect = Rectangle(5, 10)
        rect.update(1, 15, 25, 3, 4)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 15)
        self.assertEqual(rect.height, 25)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_rectangle_update_with_kwargs(self):
        rect = Rectangle(5, 10)
        rect.update(id=1, width=15, height=25, x=3, y=4)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 15)
        self.assertEqual(rect.height, 25)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_rectangle_to_dictionary(self):
        rect = Rectangle(5, 10, 2, 3, 1)
        rect_dict = rect.to_dictionary()
        expected_dict = {'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 3}
        self.assertEqual(rect_dict, expected_dict)

if __name__ == "__main__":
    unittest.main()
