#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections
import itertools
import math
import time

from functools import reduce


def dynamic(f):
    cache = collections.defaultdict(lambda: [])
    def is_known(*args):
        key = "".join(map(str, args))
        if cache[key] == []:
            cache[key] = f(*args)
        return cache[key]
    return is_known


def sum_digits(vec):
    squared = sum(map(lambda s: s**2, vec))
    return [int(e) for e in str(squared)]


@dynamic
def square_digit_chain(vec):
    if vec == [1] or vec == [0]:
        return 1
    elif vec == [8, 9]:
        return 89
    else:
        return square_digit_chain(sum_digits(vec))

# https://en.m.wikipedia.org/wiki/Multinomial_theorem#Ways_to_put_objects_into_bins
def number_of_unique_permutations(k, vec):
    c = collections.Counter(vec)
    facts = [math.factorial(e) for e in c.values()]
    deno = reduce(lambda x, y: x*y, facts)
    return math.factorial(k) // deno

if __name__ == "__main__":

    t1 = time.time()

    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    n = 7
    count = 0
    for vec in itertools.combinations_with_replacement(digits, n):
        if square_digit_chain(vec) == 89:
            count += number_of_unique_permutations(n, vec)

    print(count)

    print("done under", time.time() - t1, "seconds")
