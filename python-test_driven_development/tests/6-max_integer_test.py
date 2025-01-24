#!/usr/bin/python3

def max_integer(lst=[]):
    """Function to find and return the max integer in a list of integers.
    If the list is empty, the function returns None.
    """
    if len(lst) == 0:
        return None
    result = lst[0]
    for i in lst[1:]:
        if i > result:
            result = i
    return result
