#!/usr/bin/python3
def uppercase(str):
    if 97 <= ord(str) <= 122:
        str = chr(ord(str) - 32)
        print("{}".format(str))
    else:
        print("{}".format(str))
