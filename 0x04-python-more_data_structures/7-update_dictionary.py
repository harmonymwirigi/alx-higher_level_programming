#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    that replaces or adds key/value in a dictionary
    """
    a_dictionary.update({key: value})
    return (a_dictionary.copy())
