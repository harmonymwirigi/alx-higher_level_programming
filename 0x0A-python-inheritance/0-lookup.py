#!/usr/bin/python3
#0-lookup.py

"""
print the instances and function in an object
"""

def lookup(obj):
    """
    function to return the list of objects ad functions
    Args:
        obj: the object of the class
    """
    k = dir(obj)
    return k
