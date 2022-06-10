#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    replacing element at index with element
    """
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
