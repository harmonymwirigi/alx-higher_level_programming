#!/usr/bin/python3
def best_score(a_dictionary):
    """
     returns a key with the biggest integer value.
    """
    maxi = 0
    winner = None
    if type(a_dictionary) is dict:
        for (key, value) in a_dictionary.items():
            if value > maxi:
                maxi = value
                winner = key
    return winner
