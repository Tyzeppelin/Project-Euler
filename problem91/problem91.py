#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools
import time


def test_right_triangle(x1, y1, x2, y2):
    if x1+y1 == 0 or x2+y2 == 0:
        return False
    if x1 == x2 and y1 == y2:
        return False
    if (x1 == 0 and y2 == 0) or (x2 == 0 and y1 == 0):
        return True
    if x1 * (x1 - x2) + y1 * (y1 - y2) == 0:
        return True
    if x2 * (x2 - x1) + y2 * (y2 - y1) == 0:
        return True
    return False

if __name__ == "__main__":

    t1 = time.time()

    max_n = 50
    count = 0

    pq = itertools.product(range(max_n+1), repeat=2)
    for (x1, y1), (x2, y2) in itertools.combinations_with_replacement(list(pq), 2):
        if test_right_triangle(x1, y1, x2, y2):
            count += 1

    print(count)

    print("done under", time.time() - t1, "seconds")
