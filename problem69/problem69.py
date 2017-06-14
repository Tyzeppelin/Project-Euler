
import collections
import fractions
import math
import random
import time

from collections import defaultdict
from fractions import gcd
from math import sqrt

def dynamic(f):
    cache = defaultdict(lambda: -1)
    def is_known(*args):
        if cache[args] == -1:
            cache[args] = f(*args)
        return cache[args]
    return is_known

# from rosetta code
# http://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python
@dynamic
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
 
    for i in range(10):
        a = random.randrange(2, n)
        if try_composite(a):
            return False
 
    return True # no base tested showed n as composite

#@dynamic
def prime_iterator(n):
    yield 2
    i = 3
    while i < n:
        if isPrime(i):
            yield i
        i+=2

@dynamic
def totient(n):
    if isPrime(n):
        return n-1
    if n%2 == 0:
        return 2*totient(n/2) if (n/2 % 2) != 1 else totient(n/2)
    for p in prime_iterator(n/2+1):
        if n % p == 0:
            g = gcd(p, n/p)
            if g == 1:
                return totient(p)*totient(n/p)
            else:
                return totient(p)*totient(n/p)*g/totient(g)



if __name__ == "__main__":

    t1 = time.clock()

    m = 2.0
    for n in range(2, 1000001):
        t = totient(n)
        #print(n, t, n/t)
        if float(n)/t > m/totient(m):
            m = float(n)

    print(m, totient(m), m/totient(m))
    print(time.clock() - t1, "seconds")
