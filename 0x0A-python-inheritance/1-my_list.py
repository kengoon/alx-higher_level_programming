#!/usr/bin/python3
"""MyList."""


class MyList(list):
    """MyList class"""
    def print_sorted(self):
        """sort my list"""
        mycopy = self.copy()
        mycopy.sort()
        print(mycopy)
