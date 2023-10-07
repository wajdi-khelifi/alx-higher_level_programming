#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        if idx < 0 or idx != len(my_list):
            return my_list.copy()
        for i in range(len(my_list)):
            if i == idx:
                return my_list.append(element)
            else:
                return my_list.append(my_list[i])
