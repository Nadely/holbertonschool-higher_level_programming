#!/usr/bin/python3
"""function that reads a text file"""


def read_file(filename=""):
    """use the with statement"""

    with open(filename, "r") as file:
        print(file.read())
