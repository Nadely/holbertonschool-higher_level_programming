#!/usr/bin/python3
"""class Square that defines a square
this class is empty
"""


class Square():
    """line defining that it is a class is empty"""
    {}

    """Private instance attribute: size"""

    def __init__(self, _Square__size=0):
        """Instantiation with optional size"""
        if not isinstance(_Square__size, int):
            raise TypeError("size must be an integer")
        if _Square__size < 0:
            raise ValueError("size must be >= 0")
        """Instantiation with size"""
        self._Square__size = _Square__size

    """Public instance method"""

    def area(self):
        """Compute the area of the square"""
        return self._Square__size ** 2
