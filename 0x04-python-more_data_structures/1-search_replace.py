#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for i in range my_list:
        new_list = my_list.insert(replace, search)
    return new_list
