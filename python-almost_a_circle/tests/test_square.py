import unittest
from models.square import Square
import os

class TestSquare(unittest.TestCase):
    def setUp(self):
        """Initialisation d'une instance de Square avec une taille de 5."""
        self.s = Square(5)

    def tearDown(self):
        """Suppression de l'instance créée et du fichier Square.json
        s'il existe."""
        try:
            os.remove("Square.json")
        except:
            pass
        del self.s

    def test_init_with_valid_values(self):
        """Vérifie que Square peut être initialisé avec des valeurs valides
        pour ses attributs."""
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    def test_init_with_invalid_size(self):
        """Vérifie que Square génère une exception lorsqu'une taille
        invalide est utilisée pour l'initialisation."""
        with self.assertRaises(ValueError):
            square = Square(0)

    def test_set_size_with_valid_value(self):
        """Vérifie que la taille de Square peut être modifiée avec une
        valeur valide."""
        square = Square(5)
        square.size = 10
        self.assertEqual(square.size, 10)

    def test_set_size_with_invalid_value(self):
        """Vérifie que Square génère une exception lorsque la taille est
        définie avec une valeur invalide."""
        square = Square(5)
        with self.assertRaises(ValueError):
            square.size = -5

    def test_str(self):
        """Vérifie que la méthode str renvoie une représentation sous forme
        de chaîne correcte de l'objet Square."""
        square = Square(5, 2, 3, 1)
        self.assertEqual(str(square), "[Square] (1) 2/3 - 5")

    def test_update_with_args(self):
        """Vérifie que la méthode update met à jour les attributs de Square
        en utilisant des arguments positionnels."""
        square = Square(5)
        square.update(1, 10, 2, 3)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_update_with_kwargs(self):
        """Vérifie que la méthode update met à jour les attributs de Square
        en utilisant des arguments par mot-clé."""
        square = Square(5)
        square.update(id=1, size=10, x=2, y=3)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_to_dictionary(self):
        """Vérifie que la méthode to_dictionary renvoie un dictionnaire
        contenant les attributs de Square."""
        square = Square(5, 2, 3, 1)
        square_dict = square.to_dictionary()
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(square_dict, expected_dict)

    def test_init_with_non_integer_size(self):
        """Vérifie que Square génère une exception lorsqu'une taille non
        entière est utilisée pour l'initialisation."""
        with self.assertRaises(TypeError):
            square = Square("invalid_size")

    def test_set_size_with_non_integer_value(self):
        """Vérifie que Square génère une exception lorsque la taille est
        définie avec une valeur non entière."""
        square = Square(5)
        with self.assertRaises(TypeError):
            square.size = "invalid_size"

    def test_set_x_with_negative_value(self):
        """Vérifie que Square génère une exception lorsque la position x est
        définie avec une valeur négative."""
        square = Square(5, 2, 3)
        with self.assertRaises(ValueError):
            square.x = -1

    def test_set_y_with_negative_value(self):
        """Vérifie que Square génère une exception lorsque la position y est
        définie avec une valeur négative."""
        square = Square(5, 2, 3)
        with self.assertRaises(ValueError):
            square.y = -1

    def test_init_with_minimum_size(self):
        """Vérifie que Square peut être initialisé avec une taille minimale
        (1)."""
        square = Square(1)
        self.assertEqual(square.size, 1)

    def test_init_with_maximum_size(self):
        """Vérifie que Square peut être initialisé avec la taille maximale
        autorisée."""
        square = Square(2**31 - 1)
        self.assertEqual(square.size, 2**31 - 1)

    def test_set_size_to_maximum_value(self):
        """Vérifie que la taille de Square peut être définie à la valeur
        maximale autorisée."""
        square = Square(5)
        square.size = 2**31 - 1
        self.assertEqual(square.size, 2**31 - 1)

    def test_init_with_minimum_x_and_y(self):
        """Vérifie que Square peut être initialisé avec des positions x et y
        minimales (0)."""
        square = Square(5, 0, 0)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

    def test_init_with_maximum_x_and_y(self):
        """Vérifie que Square peut être initialisé avec les positions x et y
        maximales autorisées."""
        square = Square(5, 2**31 - 1, 2**31 - 1)
        self.assertEqual(square.x, 2**31 - 1)
        self.assertEqual(square.y, 2**31 - 1)

    def test_set_x_to_maximum_value(self):
        """Vérifie que la position x de Square peut être définie à la valeur
        maximale autorisée."""
        square = Square(5, 2, 3)
        square.x = 2**31 - 1
        self.assertEqual(square.x, 2**31 - 1)

    def test_set_y_to_maximum_value(self):
        """Vérifie que la position y de Square peut être définie à la valeur
        maximale autorisée."""
        square = Square(5, 2, 3)
        square.y = 2**31 - 1
        self.assertEqual(square.y, 2**31 - 1)

if __name__ == "__main__":
    unittest.main()
