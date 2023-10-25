import unittest
from models.square import Square
import json
import os
import sys
from io import StringIO

class TestSquare(unittest.TestCase):
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

if __name__ == "__main__":
    unittest.main()
