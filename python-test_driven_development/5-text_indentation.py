#!/usr/bin/python3
""" function that prints a text with 2 new lines after each of
these characters: ".", "?" and ":"
>>> text_indentation("Hello, who's that ? It's me !")
Hello, who's that ?

It's me !
"""


def text_indentation(text):
    """ text must be a string, otherwise raise a TypeError exception
    with the message: "text must be a string"
    There should be no space at the beginning or at the end of
    each printed line """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    symboles = {".", "?", ":"}
    indentation = "\n"
    result = ""
    new_line = True
    for s in text:
        if s in symboles:
            result += s + "\n" + indentation
            new_line = True
        elif s == " " and new_line:
            pass
        else:
            result += s
            new_line = False
    print(result, end='')
