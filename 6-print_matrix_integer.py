#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for fila in matrix:
        for i in fila:
            print(i,end="")
            if i != fila[-1]:
                print(" ",end="")
        print()