#!/usr/bin/python3
'''A module containing IO functions.'''


def write_file(filename="", text=""):
    '''Writes a UTF-8 encoded text to a file'''
    n = 0
    with open(filename, mode='w', encoding='utf-8') as f:
        n = f.write(text)
    return n
