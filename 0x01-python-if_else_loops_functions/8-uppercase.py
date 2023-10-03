#!/usr/bin/python3
def uppercase(str):
    if 'a' <= str <= 'z':
        str = chr(ord(str) - 32)
        print("{}".format(str))
    else:
        print("{}".format(str))
