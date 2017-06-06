
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
 
    for i in range(10):
        a = random.randrange(2, n)
        if try_composite(a):
            return False
 
    return True # no base tested showed n as composite

if __name__ == "__main__":

    t1 = time.clock()

    n = 1

    total = 1.0
    primes = 0
    ratio = primes / total
    inc = 0
    #for _ in range(3):
    while True:
        inc += 2
        #print(inc)
        for _ in range(4):
            n += inc
            total += 1
            if isPrime(n):
                primes +=1
            #print(n, isPrime(n), primes, total)
        ratio = primes / total
        #print(ratio)
        if ratio < 0.1:
            break
    # +1 ffs
    print(inc+1)
    print(time.clock() - t1, "seconds")
