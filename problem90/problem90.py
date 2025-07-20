#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools
import time

SQUARES = set([1, 4, 9, 16, 25, 36, 49, 64, 81])


def is_all_square(s1, s2):

    sq = set()

    for e1 in s1:
        for e2 in s2:
            if 10*e1+e2 in SQUARES:
                sq.add(10*e1+e2)
            if 10*e2+e1 in SQUARES:
                sq.add(10*e2+e1)

    return SQUARES == sq


if __name__ == "__main__":
    t1 = time.time()


    numbers = set([0, 1, 2, 3, 4, 5, 6, 7 ,8, 9])


    count = 0
    for s1 in itertools.combinations(numbers, 6):
        if 6 in s1 and 9 not in s1:
            s1 += (9,)
        if 9 in s1 and 6 not in s1:
            s1 += (6,)
        for s2 in itertools.combinations(numbers, 6):
            if 6 in s2 and 9 not in s2:
                s2 += (9,)
            if 9 in s2 and 6 not in s2:
                s2 += (6,)
            if is_all_square(s1, s2):
                count += 1

    print(count // 2)

    print("done under", time.time() - t1, "seconds")
