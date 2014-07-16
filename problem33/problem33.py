#!/usr/bin/python

from __future__ import division
from math import *
import time

def simplifiable(a, b, c, d):
    ref = (10*a+b)/(10*c+d)
    if ref == 1:
        return False
    if a==c :
        return ref == b/d
    elif a==d:
        return ref == b/c
    elif b==c:
        return ref == a/d
    elif b==d:
        return ref == a/c
    else :
        return False


if __name__ == "__main__":

    t1 = time.clock()

    a = 1
    b = 1

    c = 1
    d = 1

    ct = 0

    num = 1
    den = 1

    while ct != 4 :
        c = a
        d = b
        while 10*c+d < 99 :
            if simplifiable(a, b, c, d):
                #print 10*a+b,"/",10*c+d, "is simplifiable"
                ct += 1
                num *= 10*a+b
                den *= 10*c+d
            if c == 9 and d == 9:
                break
            elif d == 9:
                c += 1
                d = 1
            else:
                d += 1
        if a == 9 and b == 9:
            print a, b, c, d, 'dafuq'
            break
        elif b == 9:
            a += 1
            b = 1
        else:
            b += 1

pp = fmod(num, den)

print "yata!", num, "/", den, "=", num/den
print "-->", den/pp
print "exec time:", time.clock()-t1
