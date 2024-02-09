#!/usr/bin/python3
'''A module containing IO functions.
'''
from json import JSONEncoder


def to_json_string(my_obj):
    '''Creates the JSON representation of an object.
    Args:
        my_obj (any): An object to convert to JSON.
    Returns:
        str: A JSON representation of the object if possible,
        otherwise an exception is thrown.
    '''
    return JSONEncoder().encode(my_obj)
