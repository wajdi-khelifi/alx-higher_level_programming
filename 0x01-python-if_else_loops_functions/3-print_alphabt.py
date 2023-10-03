#!/usr/bin/python3
for ASCII in range(97, 123):
    if chr(ASCII) not in "qe":
        print("{}".format(chr(ASCII)), end="")
