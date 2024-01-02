#!/usr/bin/python3
for g in range(0, 100):
    if g == 99:
        print(g)
    else:
        print("{:0>2d}".format(g), end=", ")
