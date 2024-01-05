#!/usr/bin/env python3
if __name__ == "__main__":
    from sys import argv

    arg_len = len(argv) - 1
    if not arg_len:
        print("0 arguments.")
    else:
        print(f"{arg_len} arguments:")
        for i, arg in enumerate(argv):
            if i:
                print(f"{i}: {arg}")
