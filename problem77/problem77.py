
import time
import random

from collections import defaultdict

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
 
    for i in range(5):
        a = random.randrange(2, n)
        if try_composite(a):
            return False
 
    return True # no base tested showed n as composite



@dynamic
def prev_prime(i):
    if i <= 2:
        return 0 
    n = i-1
    while not isPrime(n):
        n -= 1
    return n

@dynamic
def part(n, k):
    if n == 0 and k != 0:
        return 1
    if k == 0:
        return 0
    elif k > n:
        return part(n, prev_prime(k))
    else:
        return part(n-k, k) + part(n, prev_prime(k))


if __name__ == "__main__":

    t1 = time.clock()

    #print(part(10,7))
    i = 5
    while part(i, prev_prime(i)) <= 5000:
        i += 1
    
    print(i)

    print(time.clock() - t1, "seconds")
