#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    serches for an element search in list and replaces it
    """
    for i in my_list:
        if i == search:
            i = replace
    return (my_list)
