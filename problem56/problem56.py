#!/usr/bin/python3

from math import log

if __name__ == "__main__":

    m = 1
    for a in range(99, 50, -1):
        for b in range(99, 50, -1):
            m = max(m, sum([int(e) for e in str(a**b)]))
    print(m)
