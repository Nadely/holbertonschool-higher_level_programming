#!/usr/bin/python3
"""A class BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """def in class"""

    def __init__(self, width, height):
        """width and height must be positive integers,
        validated by integer_validator"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
