#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    arg = len(sys.argv)
    if arg != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operator = sys.argv[2]
    if operator != "+" and operator != "-" and operator != "*" and
    operator != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if operator == "+":
        print("{}".format(add(int(sys.argv[1]), int(sys.argv[3]))))
    elif operator == "-":
        print("{}".format(sub(int(sys.argv[1]), int(sys.argv[3]))))
    elif operator == "*":
        print("{}".format(mul(int(sys.argv[1]), int(sys.argv[3]))))
    elif operator == "/":
        print("{}".format(div(int(sys.argv[1]), int(sys.argv[3]))))
