#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        for i in my_string:
            if i == "c" or i == "C":
                new_sring = my_string.remove(i)
                return new_string
