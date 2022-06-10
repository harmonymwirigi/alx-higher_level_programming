#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    serches for an element search in list and replaces i
    """
    return ([elem if elem != search else replace for elem in my_list])
