#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    num = 0

    for i, s in enumerate(roman_string):
        if not roman_dict.get(s) or roman_string.count(s) > 3:
            return 0

        if (i < len(roman_string) - 1 and
                roman_dict[s] < roman_dict[roman_string[i + 1]]):
            num += roman_dict[s] * -1
        else:
            num += roman_dict[s]
    return num
