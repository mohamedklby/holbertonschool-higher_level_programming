#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    my_list = [1, 2, 3, 4, 5]
    idx = element(my_list, 3, 55)

    print("My_list:", my_list)
    print("New_list:", idx)


