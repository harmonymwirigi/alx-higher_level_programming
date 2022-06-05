#!/usr/bin/python3

def element_at(my_list, idx):
    """
    prints the item at index idx in the list my_list
    """
    if idx >= len(my_list) or idx < 0:
        return
    return my_list[idx]
