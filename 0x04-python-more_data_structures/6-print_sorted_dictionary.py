#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key in a_dictionary.keys():
        print("{:s} : {}".format(key, a_dictionary[key]))
