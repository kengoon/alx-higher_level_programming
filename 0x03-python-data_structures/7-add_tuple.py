#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    pad = (0, 0)
    a = tuple_a + pad
    b = tuple_b + pad
    return a[0] + b[0], a[1] + b[1]
