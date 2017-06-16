
import time

from fractions import gcd

def simplify(n,d):
    g = gcd(n,d)
    return n/g, d/g

def totient_sieve(n):

    r = range(n)
    for n in range(2, n):
        if r[n] == n:
            r[n::n] = (i * (n-1)/n for i in r[n::n])
    return r

if __name__ == "__main__":

    t1 = time.clock()

    totients = totient_sieve(1000001)
    print(totients[:8])

    # We can show that each denominator can only form totient(d)
    # proper fractions because every other non proper n/d has
    # already been seen

    c = 0
    for d in range(2, 1000001):
        c += totients[d]
    print(c) 

    print(time.clock() - t1, "seconds")
