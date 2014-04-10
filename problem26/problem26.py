#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time

def countSubStr(s, patt):
    return s.count(patt)


# Find the largest reccuring cycle in a number n
# return -1 if none found
def reccuringCycle(n):
    i = 0
    s = str(n)
    sz = len(s)
    patt = ''
    max = -1
    while (i < sz/2):

        patt += s[i]
        nbSus = countSubStr(s, patt)

        if nbSus == sz/(i+1):
            return len(patt)
        i += 1
    return max


if __name__ == "__main__":

    t1 = time.clock()

    PRECISION = 8000
    num = pow(10, PRECISION)
    max = 1
    cycle = 0
    den = 1
    while den < 1000:

        n = num / den
        rec = reccuringCycle(n)
        if rec > max:
            print "den ->", den, "max cycle ->", rec
            max = den
            cycle = rec
        den += 1

    print "maximum reccuring cycle -> max", max, " ; cycle", cycle
    print "Execute in", time.clock()-t1, "seconds"
