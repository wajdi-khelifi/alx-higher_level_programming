#!/usr/bin/python3
"""
This is the "5-test_indentation" module.
The 5-text_indentation module supplies one function, text_indentation(text).
"""


def text_indentation(text):
    """Prints a text with 2 new lines after these characters: ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    var = 0
    for count in text:
        if var == 0:
            if count == ' ':
                continue
            else:
                var = 1
        if var == 1:
            if count == '?' or count == '.' or count == ':':
                print(count)
                print()
                var = 0
            else:
                print(count, end="")
