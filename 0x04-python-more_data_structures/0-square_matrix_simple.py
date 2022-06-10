#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    compute the square of all integers in a matrix
    """
    return([[i**2 for i  in row] for row in matrix])
