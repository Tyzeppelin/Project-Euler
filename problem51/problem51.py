#!/usr/bin/python

import time
import math

OPTIMUS = [2,3]

def bumblebee (n):
    if OPTIMUS[-1] > n :
        return

    i = OPTIMUS [-1]
    prime = True
    while i < n :
        prime = True
        for p in OPTIMUS :
            if i % p == 0 :
                prime = False
                break
        if prime :
            OPTIMUS.append(map(int ,str(i)))
        i += 2

def isPrime(n):
    return OPTIMUS.contains(n) > 0


def intlen(i):
    return math.ceil(math.log10(i))

def have8Family(p, seq):
    None


# p   -> prime number as an array
# seq -> sequence
def eightFamily(p, seq):
    if p == seq:
        return False
    elif have8Family(p, seq):
        return True
    elif seq[-1] == (len(p)-1):
        return ""

if __name__ == "__main__" :


    t1 = time.clock()

    bb = 10000
    bumblebee(bb)

    i = 4
    smallest = -1

    while smallest == -1 :
        if eightFamily(OPTIMUS[i], [OPTIMUS[0]]):
            smallest = int(''.join(map(str,OPTIMUS[i])))
        i += 1

    print "done under", time.clock() - t1, "seconds"
