#!/usr/bin/python3
for g in range(0, 9):
    for f in range(g + 1, 10):
        if g != 8:
            print("{}{}".format(g, f, end=", "))
        else:
            print("{}{}".format(g, f))
