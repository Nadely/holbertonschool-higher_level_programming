#!/usr/bin/python3
import sys
def add(number):
    return sum(number)
if __name__ == "__main__":
    number = [int(arg) for arg in sys.argv[1:]]
    result = add(number)
    print("{}".format(result))
