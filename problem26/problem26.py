#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time

# Find if a pattern patt is a reccuring pattern in s
def isRecCycle(s, patt):
    banana = s
    hamac = patt
    while len(banana) > 0:
        if banana[0] == hamac[0]:
            banana = banana[1:]
            hamac = hamac[1:] + hamac[0]
        else :
            return False
    return True

# find the number of substring patt is in s
def countSubStr (s, patt):
    return s.count(patt)



def reduceStr (s):
    wip = s
    while wip[-1] == '0':
        wip = wip[:-1]
    return wip


# Find the largest recurring cycle in a number n
# return -1 if none found
def recurringCycle(n):
    i = 0
    s = reduceStr(str(n))
    sz = len(s)
    patt = ''
    max = -1
    while i < sz/2:
        patt += s[i]
        if countSubStr(s, patt) == sz/(i+1):
            if isRecCycle(s, patt):
                return i+1
        i += 1
    return max


if __name__ == "__main__":

    t1 = time.clock()

    PUISSANCE = 8000
    num = pow(10, PUISSANCE)
    max = 1
    cycle = 0
    den = 1
    while den < 1000:

        n = num / den
        rec = recurringCycle(n)
        if rec > max:
            # print "den ->", den, "max cycle ->", rec
            max = den
            cycle = rec
        den += 1

    print("maximum recurring cycle -> max", max, " ; cycle", cycle)



    print("Execute in", time.clock()-t1, "seconds")
