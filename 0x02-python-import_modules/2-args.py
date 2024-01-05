#!/usr/bin/env python3
"""
This module prints the number of and the list of its arguments
"""
if __name__ == "__main__":
    from sys import argv
    
    arg_len = len(argv) - 1
    if not arg_len:
        print("0 arguments.")
    else:
        print(f"{arg_len} arguments:")
        for i, arg in enumerate(argv):
            if not i: continue
            print(f"{i}: {arg}")
