#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col_idx, col in enumerate(row):
            if col_idx != 0:
                print(" ", end="")
            print("{:d}".format(col), end="")
    if not matrix:
        print("$")
