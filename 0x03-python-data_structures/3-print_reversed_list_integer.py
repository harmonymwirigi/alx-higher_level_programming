#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    print list in a reverse way
    """
    if len(my_list) <= 0:
        return my_list
    else:
        i = my_list.reverse()
        for j in i:
            print("{:d}",format(i[j]))
