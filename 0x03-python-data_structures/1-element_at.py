#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx not in range(my_list):
        return None
    else:
        for i in my_list:
            print("Element at index {:d} is {}".format(idx, i))
