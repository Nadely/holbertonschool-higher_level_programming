#!/usr/bin/python3
"""
Function for adds two integers, a and b must be integers or floats,
otherwise raise a TypeError exception with the message :
'a must be an integer or b must be an integer'
a and b must be first casted to integers if they are float """


def add_integer(a, b=98):
    """ if a or b is not int or float return message error
    then check if a or b is a flaot convert in int
    finish adds a and b """
    if not isinstance(a, (int, float)) or a is None:
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
