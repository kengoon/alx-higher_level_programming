#!/usr/bin/env python3
if __name__ == "__main__":
    from sys import argv

    arg_len = len(argv) - 1
    if not arg_len:
        print("0 arguments.")
    elif arg_len == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg_len))
    for i, arg in enumerate(argv):
        if i:
            print("{}: {}".format(i, arg))
