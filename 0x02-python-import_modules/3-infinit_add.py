#!/usr/bin/python3
from sys import argv

print(sum(int(num) for num in argv if num.isnumeric()))
