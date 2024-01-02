#!/usr/bin/python3
def remove_char_at(str, n):
    str_lst = list(str)
    if 0 <= n < len(str_lst):
        str_lst.pop(n)
    return "".join(str_lst)
