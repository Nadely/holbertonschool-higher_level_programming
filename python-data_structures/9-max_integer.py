#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    number_max = my_list[0]
    for number in my_list:
        if number > number_max:
            number_max = number
    return number_max
