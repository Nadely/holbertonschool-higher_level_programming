#!/usr/bin/python3
"""class Square that defines a square
this class is empty
"""


class Square():
    """line defining that it is a class is empty"""
    {}

    """Private instance attribute: size"""

    def __init__(self, _Square__size=0):
        """Instantiation with size"""
        self._Square__size = _Square__size

    """Public instance method"""

    def area(self):
        """Compute the area of the square"""
        return self._Square__size ** 2

    """property getter"""

    @property
    def size(self):
        """return getter"""
        return self._Square__size

    """property setter"""

    @size.setter
    def size(self, value):
        """Instantiation with optional size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        """Change name"""
        self._Square__size = value

        """Printing a square"""

    def my_print(self):
        """print function"""
        if self._Square__size > 0:
            for _ in range(self._Square__size):
                print("#" * self._Square__size)
        else:
            print()
