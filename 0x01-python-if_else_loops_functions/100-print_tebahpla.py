#!/usr/bin/python3
for chars in range(ord('z'), ord('a') - 1, -2):
    print("{:c}{:s}".format(chars, chr(chars - 33)), end="")
