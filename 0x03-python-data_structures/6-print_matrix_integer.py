#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for idx, j in enumerate(i):
            print("{}".format(j), end="\n" if idx < len(i) - 1 else " ")
