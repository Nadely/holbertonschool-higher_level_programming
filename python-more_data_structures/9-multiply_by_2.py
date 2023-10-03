#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for idx, value in a_dictionary.items():
        new_dictionary[idx] = value * 2
    return new_dictionary
