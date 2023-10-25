import unittest
from models.rectangle import Rectangle
import os


class TestRectangle(unittest.TestCase):
    def setUp(self):
        """Initialisation d'une instance avec des paramètres de largeur et de
        hauteur."""
        self.r = Rectangle(5, 10)

    def tearDown(self):
        """Suppression de l'instance créée."""
        del self.r

    def test_init_with_valid_values(self):
        """Vérifie la création d'une instance de Rectangle avec des valeurs
        valides pour ses attributs."""
        rect = Rectangle(10, 20, 2, 3, 1)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)
        self.assertEqual(rect.id, 1)

    def test_init_with_invalid_width(self):
        """Vérifie que des exceptions sont levées lorsque des valeurs invalides
        sont utilisées pour initialiser la largeur."""
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 20)

    def test_init_with_invalid_height(self):
        """Vérifie que des exceptions sont levées lorsque des valeurs invalides
        sont utilisées pour initialiser la hauteur."""
        with self.assertRaises(ValueError):
            rect = Rectangle(10, -5)

    def test_init_with_invalid_x(self):
        """Vérifie que des exceptions sont levées lorsque des valeurs invalides
        sont utilisées pour initialiser la position x."""
        with self.assertRaises(ValueError):
            rect = Rectangle(10, 20, -1)

    def test_init_with_invalid_y(self):
        """Vérifie que des exceptions sont levées lorsque des valeurs invalides
        sont utilisées pour initialiser la position y."""
        with self.assertRaises(ValueError):
            rect = Rectangle(10, 20, 2, -1)

    def test_set_width_with_valid_value(self):
        """Vérifie que la largeur de Rectangle peut être modifiée avec une
        valeur valide."""
        rect = Rectangle(10, 20)
        rect.width = 15
        self.assertEqual(rect.width, 15)

    def test_set_width_with_invalid_value(self):
        """Vérifie que Rectangle génère une exception lorsque la largeur est
        définie avec une valeur invalide."""
        rect = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            rect.width = -5

    def test_area(self):
        """Vérifie que la méthode area renvoie la valeur correcte de la zone
        de l'objet."""
        rect = Rectangle(10, 20)
        self.assertEqual(rect.area(), 200)

    def test_str(self):
        """Vérifie que la méthode str renvoie une représentation sous forme de
        chaîne correcte de l'objet Rectangle."""
        rect = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(str(rect), "[Rectangle] (1) 2/3 - 5/10")

    def test_update_with_args(self):
        """Vérifie que la méthode update met à jour les attributs de Rectangle
        en utilisant des arguments positionnels."""
        rect = Rectangle(10, 20)
        rect.update(1, 15, 25, 3, 4)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 15)
        self.assertEqual(rect.height, 25)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_update_with_kwargs(self):
        """Vérifie que la méthode update met à jour les attributs de Rectangle
        en utilisant des arguments par mot-clé."""
        rect = Rectangle(10, 20)
        rect.update(id=1, width=15, height=25, x=3, y=4)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 15)
        self.assertEqual(rect.height, 25)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_to_dictionary(self):
        """Vérifie que la méthode to_dictionary renvoie un dictionnaire
        contenant les attributs de l'objet Rectangle."""
        rect = Rectangle(10, 20, 1, 2, 3)
        rect_dict = rect.to_dictionary()
        expected_dict = {'id': 3, 'width': 10, 'height': 20, 'x': 1, 'y': 2}
        self.assertEqual(rect_dict, expected_dict)

    def test_init_with_non_integer_width(self):
        """Vérifie que Rectangle génère une exception lorsqu'une largeur non
        entière est utilisée pour l'initialisation."""
        with self.assertRaises(TypeError):
            rect = Rectangle("invalid_width", 10)

    def test_init_with_non_integer_height(self):
        """Vérifie que Rectangle génère une exception lorsqu'une hauteur non
        entière est utilisée pour l'initialisation."""
        with self.assertRaises(TypeError):
            rect = Rectangle(10, "invalid_height")

    def test_init_with_non_integer_x(self):
        """Vérifie que Rectangle génère une exception lorsqu'une position x
        non entière est utilisée pour l'initialisation."""
        with self.assertRaises(TypeError):
            rect = Rectangle(10, 20, "invalid_x")

    def test_init_with_non_integer_y(self):
        """Vérifie que Rectangle génère une exception lorsqu'une position y
        non entière est utilisée pour l'initialisation."""
        with self.assertRaises(TypeError):
            rect = Rectangle(10, 20, 2, "invalid_y")

    def test_init_with_negative_width(self):
        """Vérifie que Rectangle génère une exception lorsqu'une largeur
        négative est utilisée pour l'initialisation."""
        with self.assertRaises(ValueError):
            rect = Rectangle(-5, 10)

    def test_init_with_zero_width(self):
        """Vérifie que Rectangle génère une exception lorsqu'une largeur de
        zéro est utilisée pour l'initialisation."""
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 10)

    def test_init_with_negative_height(self):
        """Vérifie que Rectangle génère une exception lorsqu'une hauteur
        négative est utilisée pour l'initialisation."""
        with self.assertRaises(ValueError):
            rect = Rectangle(10, -5)

    def test_init_with_zero_height(self):
        """Vérifie que Rectangle génère une exception lorsqu'une hauteur de
        zéro est utilisée pour l'initialisation."""
        with self.assertRaises(ValueError):
            rect = Rectangle(10, 0)

    def test_set_width_with_negative_value(self):
        """Vérifie que Rectangle génère une exception lorsque la largeur est
        définie avec une valeur négative."""
        rect = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            rect.width = -5

    def test_set_height_with_negative_value(self):
        """Vérifie que Rectangle génère une exception lorsque la hauteur est
        définie avec une valeur négative."""
        rect = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            rect.height = -5

    def test_set_x_with_negative_value(self):
        """Vérifie que Rectangle génère une exception lorsque la position x
        est définie avec une valeur négative."""
        rect = Rectangle(10, 20, 2, 3)
        with self.assertRaises(ValueError):
            rect.x = -1

    def test_set_y_with_negative_value(self):
        """Vérifie que Rectangle génère une exception lorsque la position y
        est définie avec une valeur négative."""
        rect = Rectangle(10, 20, 2, 3)
        with self.assertRaises(ValueError):
            rect.y = -1

    def test_init_with_minimum_width_and_height(self):
        """Vérifie que Rectangle peut être initialisé avec une largeur et une
        hauteur minimales (1)."""
        rect = Rectangle(1, 1)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 1)

    def test_init_with_maximum_width_and_height(self):
        """Vérifie que Rectangle peut être initialisé avec la largeur et la
        hauteur maximales autorisées."""
        rect = Rectangle(2**31 - 1, 2**31 - 1)
        self.assertEqual(rect.width, 2**31 - 1)
        self.assertEqual(rect.height, 2**31 - 1)

    def test_set_width_to_maximum_value(self):
        """Vérifie que la largeur de Rectangle peut être définie à la valeur
        maximale autorisée."""
        rect = Rectangle(10, 20)
        rect.width = 2**31 - 1
        self.assertEqual(rect.width, 2**31 - 1)


if __name__ == "__main__":
    unittest.main()
