#!/usr/bin/python3
"""function that reads a text file"""


def read_file(filename=""):
    """use the with statement"""

    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
