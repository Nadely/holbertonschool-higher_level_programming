#!/usr/bin/python3
import json

def class_to_json(obj):
    dictionnary = {}
    if hasattr(obj, "__dict__"):
        dictionnary = obj.__dict__.copy()
    return dictionnary
