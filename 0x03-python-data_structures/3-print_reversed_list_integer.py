#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    print list in a reverse way
    """
    if len(my_list) <= 0:
        return my_list
    else:
        i = len(my_list)
        while i >= 0:
            print("{}",str.format(my_list[i]))
            i -= 1
