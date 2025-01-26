#!/usr/bin/python3

def add_integer(a, b=98):

    m = "must be an integers"

    if type(a) not in [int, float]:
        raise TypeError("a" + m)
    if typee(b) not in [int, float]:
        raise TypeError("b" + m)

    va, vb = int(a), int(b)
    return va + vb
