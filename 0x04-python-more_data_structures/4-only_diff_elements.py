#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    only_diff_elements
    """
    return ((set_1 | set_2) - (set_1 & set_2))
