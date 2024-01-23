#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections
import math
import time

# max N = 36481
OPTIMUS = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191,)


def dynamic(f):
    cache = collections.defaultdict(lambda: [])
    def is_known(*args):
        key = "".join(map(str, args))
        if cache[key] == []:
            cache[key] = f(*args)
        return cache[key]
    return is_known



@dynamic
def divisors(n):
    a = math.ceil(math.sqrt(n))

    ret = []

    if n%2==0:
        ret += [list([2, n//2])]
        if n//2 not in OPTIMUS:
            divs = divisors(n//2)
            z = [ds+[2] for ds in divs]
            ret += z

    for p in range(3, a+1):
        if p>a:
            break
        if n%p == 0:
            ret += [list([p, n//p])]
            if n//p not in OPTIMUS:
                divs = divisors(n//p)
                z = [ds+[p] for ds in divs]
                ret += z
    return ret


def is_product_sum(n, k):
    divs = divisors(n)
    for ds in divs:
        if len(ds) <= k:
            if sum(ds) + k - len(ds) == n:
                return True
    return False


if __name__ == "__main__":
    t1 = time.time()

    k = 2
    n = 4

    MAX_K = 12000
    MAX_N = 36481

    r = []

    while k <= MAX_K and n < MAX_N:
        n = k
        while n < MAX_N:
            if is_product_sum(n, k):
                r.append(n)
                k += 1
                break
            else:
                n += 1
    
    print("len", len(set(r)))
    print("sum", sum(set(r)))

    print("done under", time.time() - t1, "seconds")
