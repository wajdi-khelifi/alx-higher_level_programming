#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0]
    if length == 0:
        first = None
    else:
        print("length: {:d} - first character: {}".format(length, first))
