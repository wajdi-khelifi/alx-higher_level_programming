#!/usr/bin/python3
def uppercase(str):
    uppercase_result = ""
    for char in str:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - 32)
            uppercase_result += uppercase_char
        else:
            uppercase_result += char
    print("{}".format(uppercase_result))
