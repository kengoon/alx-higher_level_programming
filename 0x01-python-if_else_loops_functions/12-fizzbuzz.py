#!/usr/bin/python3
def fizzbuzz():
    for m in range(1, 100):
        if m % 15 == 0:
            print("FizzBuzz", end=" ")
        elif m % 5 == 0:
            print("Buzz", end=" ")
        elif m % 3 == 0:
            print("Fizz", end=" ")
        else:
            print(m, end=" ")
