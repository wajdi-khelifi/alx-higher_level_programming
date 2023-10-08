#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = sentence.index(0)
    if length == 0:
        first = None
        print("length: {:d} - first character: {}".format(length, first))
    else:
        print("length: {:d} - first character: {}".format(length, first))
