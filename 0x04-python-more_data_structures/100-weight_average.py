#!/usr/bin/python3
def weight_average(my_list=[]):
    s, w = 0, 0
    if my_list == []:
        return 0
    for i, j in my_list:
        s += i * j
        w += j
    s /= w
    return s
