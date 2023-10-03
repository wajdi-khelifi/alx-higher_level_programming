#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            uppercase = chr(ord(char) - 32)
            print("{}".format(uppercase), end="")
        else:
            print("{}".format(char), end="")
