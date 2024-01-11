#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints the content of a list of lists (matrix)"""
    for line in matrix:
        for elem in line:
            print("{:d}".format(elem), end=" " if elem != line[-1] else "")
        print()
