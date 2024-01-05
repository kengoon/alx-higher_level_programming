#!/usr/bin/python3
def max_integer(my_list=[]):
    biggest_int = None
    for i in my_list:
        if i > biggest_int or 0:
            biggest_int = i
    return biggest_int
