#!/usr/bin/python3
'''A module containing IO functions.
'''
from json import JSONDecoder


def from_json_string(my_str):
    '''Creates an object from its JSON representation.
    Args:
        my_str (str): A JSON representation of an object.
    Returns:
        any: An object corresponding to the given JSON string,
        otherwise an exception is thrown.
    '''
    return JSONDecoder().decode(my_str)
