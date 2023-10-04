#!/usr/bin/python3
def safe_print_division(a, b) :
    try:
        result = a / b
    except ZeroDivisionError:
        print("Inside result : None")
        result = None
    else:
        print("Inside result : {}".format(result))
    finally:
        return result

