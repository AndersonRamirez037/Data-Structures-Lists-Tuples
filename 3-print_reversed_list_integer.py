#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lenght = len(my_list)
    while (lenght > 0):
        print(my_list[lenght - 1])
        lenght -= 1