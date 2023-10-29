#!/usr/bin/python3
"""
This is the "4-print_square" module
The 4-print_square  module supplies one function, print_square(size)
"""


def print_square(size):
    """print a square with "#" that has a len of size"""
    if type(size) is not int:
        raise TypeError("size must be integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
