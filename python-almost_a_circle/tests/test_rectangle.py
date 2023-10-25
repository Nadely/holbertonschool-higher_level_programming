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

if __name__ == "__main__":
    unittest.main()
