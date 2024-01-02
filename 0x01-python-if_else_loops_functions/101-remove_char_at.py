#!/usr/bin/python3
def remove_char_at(str, n):
    str_lst = list(str)
    str_lst.pop(n)
    return "".join(str_lst)
