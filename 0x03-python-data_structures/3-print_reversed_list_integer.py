#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    print list in a reverse way
    """
    if type(my_list) is list:
        my_list.reverse()
        for j in my_list:
            print("",format(j))
