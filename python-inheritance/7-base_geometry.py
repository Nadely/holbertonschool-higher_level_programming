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
