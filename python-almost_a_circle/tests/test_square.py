#!/usr/bin/python3
import unittest, os, sys, json
from models.square import Square
from models.base import Base
from io import StringIO

class TestSquare(unittest.TestCase):
    def setUp(self):
        """Initialisation d'une instance de Square avec une taille de 5."""
        self.s = Square(5)

    def tearDown(self):
        """Suppression de l'instance créée et du fichier Square.json
        s'il existe."""
        try:
            os.remove("Square.json")
        except Exception:
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

# ---------------------------------------------------------------------- #

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

    def test_square_inherits_from_base(self):
        """ Testing inheritance """
        self.assertTrue(issubclass(Square, Base))

    def test_width(self):
        """Testing the square width getter"""
        self.assertEqual(5, self.s.width)

    def test_height(self):
        """Testing the square height getter"""
        self.assertEqual(5, self.s.height)

    def test_x(self):
        """Testing square x getter and setter"""
        self.s.x = 54
        self.assertEqual(54, self.s.x)
        self.assertEqual(0, self.s.y)

    def test_y(self):
        """Testing square y getter and setter"""
        self.s.y = 45
        self.assertEqual(45, self.s.y)
        self.assertEqual(0, self.s.x)

    def test_asquare_id(self):
        """Test the id for square"""
        sq = Square(2, 0, 0, 199)
        self.assertEqual(199, sq.id)

    def test_width_string(self):
        """Testing for other than int"""
        with self.assertRaises(TypeError):
            sq = Square("1")

    def test_width_bool(self):
        """Testing for other than int"""
        with self.assertRaises(TypeError):
            sq = Square(True)

    def test_width_list(self):
        """Testing for other than int"""
        with self.assertRaises(TypeError):
            sq = Square([10, 6])

    def test_x_string(self):
        """Testing for other than int"""
        with self.assertRaises(TypeError):
            sq = Square(1, "46")

    def test_x_bool(self):
        """Testing for other than int"""
        with self.assertRaises(TypeError):
            sq = Square(1, True)

    def test_x_list(self):
        """Testing for other than int"""
        with self.assertRaises(TypeError):
            sq = Square(1, [10, 6])

    def test_y_string(self):
        """Testing for other than int"""
        with self.assertRaises(TypeError):
            sq = Square(1, 7, "46")

    def test_y_bool(self):
        """Testing for other than int"""
        with self.assertRaises(TypeError):
            sq = Square(1, 7, True)

    def test_y_list(self):
        """Testing for other than int"""
        with self.assertRaises(TypeError):
            sq = Square(1, 7, [10, 6])

    def test_width_negative(self):
        """Testing with negative int"""
        with self.assertRaises(ValueError):
            sq = Square(-4)

    def test_x_negative(self):
        """Testing with negative int"""
        with self.assertRaises(ValueError):
            sq = Square(4, -3)

    def test_y_negative(self):
        """Testing with negative int"""
        with self.assertRaises(ValueError):
            sq = Square(4, 2, -3)

    def test_width_zero(self):
        """Testing with negative int"""
        with self.assertRaises(ValueError):
            sq = Square(0, 5)

    def test_width_float(self):
        """Testing for other than int"""
        with self.assertRaises(TypeError):
            sq = Square(1.07, 5)

    def test_x_float(self):
        """Testing for other than int"""
        with self.assertRaises(TypeError):
            sq = Square(5, 1.07)

    def test_y_float(self):
        """Testing for other than int"""
        with self.assertRaises(TypeError):
            sq = Square(5, 8, 1.07)

    def test_area(self):
        """Testing the area of the square"""
        self.assertEqual(self.s.area(), 5 * 5)
        sq = Square(3, 8, 8, 2)
        self.assertEqual(sq.area(), 3 * 3)

    def test_str_overload(self):
        s = Square(5, 8, 7, 88)
        self.assertEqual(s.__str__(), "[Square] (88) 8/7 - 5")

    def test_update_id(self):
        """Testing the update method"""
        self.s.update(54)
        self.assertEqual(54, self.s.id)

    def test_update_width(self):
        """Testing the update method"""
        self.s.update(54, 30)
        self.assertEqual(30, self.s.width)

    def test_update_height(self):
        """Testing the update method"""
        self.s.update(54, 10)
        self.assertEqual(10, self.s.height)

    def test_update_x(self):
        """Testing the update method"""
        self.s.update(54, 30, 10)
        self.assertEqual(10, self.s.x)

    def test_update_y(self):
        """Testing the update method"""
        self.s.update(54, 30, 6, 2)
        self.assertEqual(2, self.s.y)

    def test_update_dict(self):
        """Testing the update method with **kwargs"""
        self.s.update(y=1, size=2, x=3, id=89)
        self.assertEqual(1, self.s.y)
        self.assertEqual(2, self.s.size)
        self.assertEqual(3, self.s.x)
        self.assertEqual(89, self.s.id)

    def test_update_dict_list(self):
        """Testing the update method with **kwargs and *args"""
        self.s.update(1000, y=1, width=2, x=3, id=89)
        self.assertEqual(1000, self.s.id)

    def test_update_dict_no_key(self):
        """Testing the update method with **kwargs"""
        self.s.update(y=1, size=2, x=3, id=89)

    def test_update_string(self):
        """Testing the update method with **kwargs"""
        self.s.update("str")
        self.assertEqual(self.s.id, "str")

    def test_to_dict(self):
        """Testing the type that is returned from the to_dictionary method"""
        r1 = Square(5)
        self.assertEqual(type(r1.to_dictionary()), dict)

    def test_to_dict_print(self):
        """Testing the dict that will be printed"""
        r1 = Square(5, 0, 0, 410)
        r1_dict = r1.to_dictionary()
        self.assertEqual(r1_dict, {"size": 5, "id": 410, "x": 0, "y": 0})

    def test_missing_height(self):
        """Expecting a type error because size are missing"""
        with self.assertRaises(TypeError):
            Square()

    def test_saving_to_file(self):
        """Testing saving a file into json format"""
        try:
            os.remove("Square.json")
        except:
            pass
        r1 = Square(5, 0, 0, 346)
        Square.save_to_file([r1])
        with open("Square.json", "r") as file:
            content = file.read()
        t = [{"id": 346, "x": 0, "size": 5, "y": 0}]
        self.assertEqual(t, json.loads(content))

    def test_saving_to_file_no_iter(self):
        """Sending a non iterable to the function"""
        with self.assertRaises(TypeError):
            Square.save_to_file(self.s)

    def test_saving_to_file_None(self):
        """Testing saving a file into json format sending None"""
        try:
            os.remove("Square.json")
        except:
            pass
        r1 = Square(5, 0, 0, 346)
        Square.save_to_file(None)

        with open("Square.json", "r") as file:
            content = file.read()

        self.assertEqual("[]", content)

    def test_saving_to_file_type(self):
        """Testing saving a file into json format and testing the type"""
        try:
            os.remove("Square.json")
        except:
            pass
        r1 = Square(5, 0, 0, 346)
        Square.save_to_file([r1])
        with open("Square.json", "r") as file:
            content = file.read()
        self.assertEqual(str, type(content))
        try:
            os.remove("Square.json")
        except:
            pass

    def test_json_string_type(self):
        """Testing the returned type"""
        list_input = [{"id": 2089, "size": 10}, {"id": 2712, "size": 1}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(type(list_input), list)

    def test_json_string(self):
        """Testing that the json string gets converted into a list"""
        list_input = [{"id": 2089, "size": 10}, {"id": 2712, "size": 7}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        s1 = {"id": 2089, "size": 10}
        s2 = {"size": 7, "id": 2712}
        self.assertEqual(list_input[0], s1)
        self.assertEqual(list_input[1], s2)

    def test_dict_to_instance(self):
        """test that an instance is created from a dict"""
        r1 = Square(5)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_isnot_dict_to_instance(self):
        """test that an instance is created from a dict"""
        r1 = Square(109)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_load_from_file_not_the_same(self):
        """Checking that an object was created from the
        list but has a different adress."""
        r1 = Square(10)
        list_squares_input = [r1]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertNotEqual(id(r1), id(list_squares_output[0]))

    def test_load_from_file_same_width(self):
        """Checking that an object was created from the
        list and has the same witdh"""
        r1 = Square(10)
        list_squares_input = [r1]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual(r1.width, list_squares_output[0].size)

    def test_load_from_file_same_height(self):
        """Checking that an object was created from the
        list and has the same height"""
        r1 = Square(10)
        list_squares_input = [r1]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual(r1.size, list_squares_output[0].size)

    def test_load_from_file_same_x(self):
        """Checking that an object was created from the
        list and has the same x"""
        r1 = Square(10, 2, 8)
        list_squares_input = [r1]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual(r1.x, list_squares_output[0].x)

    def test_load_from_file_same_y(self):
        """Checking that an object was created from the
        list and has the same y"""
        r1 = Square(10, 2, 8)
        list_squares_input = [r1]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual(r1.y, list_squares_output[0].y)

    def test_display_square(self):
        """Checking the stdout output by capturing it"""
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1 = Square(10)
        r1.display()
        sys.stdout = sys.__stdout__
        output = (
            "##########\n"
            + "##########\n"
            + "##########\n"
            + "##########\n"
            + "##########\n"
            + "##########\n"
            + "##########\n"
            + "##########\n"
            + "##########\n"
            + "##########\n"
        )
        self.assertEqual(capturedOutput.getvalue(), output)

    def test_display_square_size_one(self):
        """Checking the stdout output by capturing it"""
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1 = Square(1)
        r1.display()
        sys.stdout = sys.__stdout__
        output = "#\n"
        self.assertEqual(capturedOutput.getvalue(), output)

    def test_display_square_size_zero(self):
        """Checking the stdout output by capturing it"""
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1 = Square(3)
        r1.display()
        sys.stdout = sys.__stdout__
        output = "###\n###\n###\n"
        self.assertEqual(capturedOutput.getvalue(), output)

    def test_display_square(self):
        """Checking the stdout output by capturing it"""
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1 = Square(10)
        r1.display()
        sys.stdout = sys.__stdout__
        output = (
            "##########\n"
            + "##########\n"
            + "##########\n"
            + "##########\n"
            + "##########\n"
            + "##########\n"
            + "##########\n"
            + "##########\n"
            + "##########\n"
            + "##########\n"
        )
        self.assertEqual(capturedOutput.getvalue(), output)

    def test_display_square_size_one(self):
        """Checking the stdout output by capturing it"""
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1 = Square(1)
        r1.display()
        sys.stdout = sys.__stdout__
        output = "#\n"
        self.assertEqual(capturedOutput.getvalue(), output)

    def test_display_square_size_zero(self):
        """Checking the stdout output by capturing it"""
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1 = Square(3)
        r1.display()
        sys.stdout = sys.__stdout__
        output = "###\n###\n###\n"
        self.assertEqual(capturedOutput.getvalue(), output)

# ---------------------------------------------------------------------- #

if __name__ == "__main__":
    unittest.main()
