#!/usr/bin/python3
"""A class BaseGeometry"""


class BaseGeometry:
    """def in class"""

    def area(self):
        """that raises an Exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value, assuming name is always a string"""

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """def in class"""

    def __init__(self, width, height):
        """width and height must be positive integers,
        validated by integer_validator0"""

        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)
