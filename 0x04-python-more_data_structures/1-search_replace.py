#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for i in range my_list:
        if my_list[i] == search:
            my_list.remove(my_list[i])
            my_list.insert(replace)
