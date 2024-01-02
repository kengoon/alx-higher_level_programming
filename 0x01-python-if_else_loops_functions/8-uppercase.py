#!/usr/bin/python3
def uppercase(str):
    chars = []
    for ch in str:
        if ord('a') <= ord(ch) <= ord('z'):
            chars.append(chr(ord(ch) - 32))
        else:
            chars.append(ch)
    print("{}".format(chars))
