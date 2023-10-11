#!/usr/bin/python3
def roman_to_int(roman_string):
    x = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i,j in enumerate(roman_string):
        if (i+1) == len(roman_string) or x[j] >= x[roman_string[i+1]]:
            result += x[j]
        else:
            result -= x[j]
    return result
