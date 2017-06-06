#!/usr/bin/python

from math import ceil, log10, sqrt
from collections import defaultdict

import itertools
import random
import time
 

# from rosetta code
# http://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python
def isPrime(n):
    assert n >= 2
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)
 
    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite
 
    for i in range(5):
        a = random.randrange(2, n)
        if try_composite(a):
            return False
 
    return True # no base tested showed n as composite



def iterator():
    i = 123
    while True:
        if isPrime(i):
            yield i
        i += 2

tavg = []
def hate_family(s):
    t1 = time.clock()
    c = 0
    for i in range(1,10):
        if isPrime(int(s.replace('*', str(i)))):
            c += 1
    tavg.append(time.clock()-t1)
    return c == 8

# one liner, but slower :/
#def hate_lambda(s):
#    return sum([isPrime(int(s.replace('*', str(i)))) for i in range(1,10)]) == 8

if __name__ == "__main__":
    t1 = time.clock()

    for e in iterator():
        for x in range(10):
            if str(x) in str(e) and hate_family(str(e).replace(str(x), '*')):
                print e
                break
        else:
            continue
        print 'tada'
        break
    print(time.clock() - t1, "seconds")

    #print(sum(tavg) / len(tavg), "avg time family")
