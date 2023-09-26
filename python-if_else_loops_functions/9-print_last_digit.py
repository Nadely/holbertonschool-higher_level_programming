#!/usr/bin/python3
def print_last_digit(number):
    if number <= 0:
        last_number = str(-number)[-1]
    else:
        last_number = str(number)[-1]

    print("{}".format(int(last_number)), end="")
    return last_number
