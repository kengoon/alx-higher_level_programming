#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or not a_dictionary:
        return None
    keys = list(a_dictionary)
    values = list(a_dictionary.values())
    return keys[values.index(max(values))]
