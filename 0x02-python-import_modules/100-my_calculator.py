#!/usr/bin/python3
import calculator_1
import sys

if __name__ == "__main__":
    a = int(sys.argv[1])
    operators = (sys.argv[2])
    b = int(sys.argv[3])
    argv = (len(sys.argv) - 1)
    if argv != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if operators == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif operators == "-":
        print("{} - {} = {}".format(a, b , sub(a, b)))
    elif operators == "*"
        print("{} * {} = {}".format(a, b, mul(a, b)))
        exit(1)
    elif operators == "/"
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
