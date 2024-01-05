#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    print(sum(int(num) for i, num in enumerate(argv) if i))
