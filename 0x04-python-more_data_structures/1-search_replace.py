#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for i in my_list:
        if i == search:
            new_list = my_list.remove(i)
            new_list = my_list.insert(replace)
