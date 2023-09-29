#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    arg = len(argv)
    if arg != 4:
        print("Usage: ./100-my_calculator.py <a> <argv[2]> <b>")
        exit(1)
    if argv[2] != "+" and argv[2] != "-" and argv[2] != '*' and argv[2] != "/":
        print("Unknown argv[2]. Available argv[2]s: +, -, * and /")
        exit(1)
    if argv[2] == "+":
        print("{}".format(add(int(sys.argv[1]), int(sys.argv[3]))))
    elif argv[2] == "-":
        print("{}".format(sub(int(sys.argv[1]), int(sys.argv[3]))))
    elif argv[2] == '*':
        print("{}".format(mul(int(sys.argv[1]), int(sys.argv[3]))))
    elif argv[2] == "/":
        print("{}".format(div(int(sys.argv[1]), int(sys.argv[3]))))
