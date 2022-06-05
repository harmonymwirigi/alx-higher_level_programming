#!/usr/bin/python3

def no_c(my_string):
    """
    remove c and C"
    """
    new_str = ""
    for i in my_string:
        if i not in 'cC':
            new_str += i
    return new_str
