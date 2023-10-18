#!/usr/bin/python3
"""Write a function that returns the dictionary description with simple
ata structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object"""


import json


def class_to_json(obj):
    """obj is an instance of a Class"""

    dictionnary = {}
    if hasattr(obj, "__dict__"):
        dictionnary = obj.__dict__.copy()
    return dictionnary
