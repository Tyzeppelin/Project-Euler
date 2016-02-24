#!/usr/bin/python

from math import *
from collections import defaultdict
import time


def bumblebee(n):
    prime = True
    OPTIMUS = [2, 3]
    i = OPTIMUS[-1]
    while OPTIMUS[-1] < n:
        prime = True
        for p in OPTIMUS:
            if i % p == 0:
                prime = False
                break
        if prime:
            OPTIMUS.append(i)
        i += 2
    #return [[int(x) for x in str(m)] for m in OPTIMUS]
    return [p for p in OPTIMUS if  p > 10000]

def isPrime(primes, n):
    end = int(sqrt(n))
    i = 0
    while primes[i] < end:
        if n%primes[i] == 0:
            return False
        i += 1
    return True


def mask(n):
    return [1] * n


def allMasks(m, i):
    if i == 0:
        return []
    else :
        m0 = m[:]
        m0[i-1] = 0
        return [m0]+allMasks(m0, i-1)+allMasks(m[:], i-1)


def family(n, mask, domain):
    fam = 0
    w = zip([int(x) for x in str(n)], mask)
    for e in range(10):
        maybe = [n if m == 1 else e for m, n in w]
        if int(''.join(map(str, maybe))) in domain:
            fam += 1
    return fam


def match(n, mask):
    same = [e for e, m in zip([int(x) for x in str(n)], mask) if m == 0]
    return all(same[0] == e for e in same)


def unmask(n, mask):
    return int(''.join(map(str, [e for e, m in zip([int(x) for x in str(n)], mask) if m == 1])))

if __name__ == "__main__":
    t1 = time.clock()

    optimus = bumblebee(99990)
    print len(optimus), "primes from", optimus[0], "to", optimus[-1], "generated under", time.clock()-t1, "seconds"
    families = defaultdict(lambda: 0)
    currMasks = [am for am in allMasks(mask(5), 5) if am.count(0) == 2 or am.count(0) == 3]
    print len(currMasks), currMasks

    print "==========="

    matches = defaultdict(lambda: [])
    i = 0
    op = 0
    for m in currMasks:
        matches[i] = defaultdict(lambda: 0)
        for p in optimus:
            if match(p, m):
                matches[i][unmask(p, m)] += 1
            op += 1
        for k, v in matches.items():
            if v == 8:
                print "8 ->", k, "mask ->", k
        i += 1
    print "==========="
    for index in matches.keys():
        print currMasks[index], matches[index]
    print "==========="
    print op, "operations"

    # for p in optimus:
    #     for mm in currMasks:
    #         if p == 56003:
    #             print p, mm, family(p, mm, optimus)
    #         f = family(p, mm, optimus)
    #         families[f] += 1
    #         if f == 8:
    #             print p, mm
    #             break
    #     else:
    #         continue
    #     break

    print families

    print "executed under", time.clock() - t1, "seconds"
