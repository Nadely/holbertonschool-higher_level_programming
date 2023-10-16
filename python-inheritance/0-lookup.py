#!/usr/bin/python3
""" function that returns the list of available attributes
and methods of an object"""


def lookup(obj):
    list_attributes = dir(obj)
    return list_attributes
