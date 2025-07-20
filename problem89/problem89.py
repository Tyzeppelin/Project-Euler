#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

OPTIMAL_SIZE = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 2, "5": 1, "6": 2, "7": 3, "8": 4, "9": 2}

def decode_roman(rs):
    """
    PRECEDENCE:

    CM
    M*
    CD
    D

    XC
    C*
    XL
    L

    IX
    X*
    IV
    V
    I*

    """

    n = 0

    count = lambda c: sum([1 for e in rs if e == c])

    nc = 0

    if "MCM" in rs:
        n += 1000 * (count("M") - 1) + 900
        nc += 1
    elif "CM" in rs:
        n += 900
        nc += 1
    else:
        n += 1000 * count("M")

    if "CD" in rs:
        n += 400
        nc += 1
    elif "D" in rs:
        n += 500

    nx = 0

    if "CXC" in rs:
        nx += 1
        nc += 1
        n += 100 * (count("C") - nc) + 90
    elif "XC" in rs:
        n += 90
        nx += 1
    else:
        n += 100 * (count("C") - nc)


    if "XL" in rs:
        n += 40
        nx += 1
    elif "L" in rs:
        n += 50

    ni = 0
    if "XIX" in rs:
        nx += 1
        ni += 1
        n += 10 * (count("X") - nx) + 9
    elif "IX" in rs:
        ni += 1
        n += 9
    elif "IV" in rs:
        ni += 1
        n += 4
        n += 10 * (count("X") - nx)
    else:
        n += 10 * (count("X") - nx)
        n += 5 * count("V")
        n += count("I") - ni

    return n


if __name__ == "__main__":

    t1 = time.time()

    with open("0089_roman.txt", 'r') as f:
        numbers = [trim.strip() for trim in f.readlines()]

    n = 0
    for ro in numbers:
        arabic = decode_roman(ro)
        # 4000 is a pain
        n += len(ro) - sum([OPTIMAL_SIZE[e] for e in str(arabic)]) - (2 if arabic//1000 == 4 else 0)

    print(n)

    print("done under", time.time() - t1, "seconds")
