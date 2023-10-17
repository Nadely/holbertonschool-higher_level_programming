#!/usr/bin/python3
"""A class BaseGeometry"""


class BaseGeometry:
    """def in class"""

    def area(self):
        """that raises an Exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value, assuming name is always a string"""

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
