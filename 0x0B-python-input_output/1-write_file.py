#!/usr/bin/python3
'''A module containing IO functions.
'''


def write_file(filename="", text=""):
    '''Writes a UTF-8 encoded text to a file.
    Args:
        filename (str): The name of the file to write to.
        text (str): The content to store in the file.
    Returns:
        int: The number of characters written.
    '''
    n = 0
    with open(filename, mode='w', encoding='utf-8') as file:
        n = file.write(text)
    return n
