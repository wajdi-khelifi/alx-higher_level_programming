#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        new_list = my_list.remove(idx) + my_list.index[idx + 1:]
        return new_list
