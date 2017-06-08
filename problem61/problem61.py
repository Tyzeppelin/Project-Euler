#!/usr/bin/python3

import time

from collections import defaultdict
from math import ceil, log, log10, sqrt

def tria(n):
    return n*(n + 1)/2
def is_tri(n):
    return (-1+sqrt(1+8*n))/2 % 1 == 0.0

def squa(n):
    return n**2
def is_sqr(n):
    return sqrt(n)%1 == 0.0

def pent(n):
    return n*(3*n - 1)/2
def is_pen(n):
    return (1+sqrt(1+24*n))/6 % 1 == 0.0

def hexa(n):
    return n*(2*n - 1)
def is_hex(n):
    return (1+sqrt(1+8*n))/4 % 1 == 0.0

def hept(n):
    return n*(5*n - 3)/2
def is_hep(n):
    return (3+sqrt(9+40*n))/10 % 1 == 0.0

def octo(n):
    return n*(3*n - 2)
def is_oct(n):
    return (1+sqrt(1+3*n))/3 %1 == 0.0


   
if __name__ == "__main__":

    t1 = time.clock()

    o = [(n/100, n%100) for n in [octo(i) for i in range(1,800)] if ceil(log10(n)) == 4]
    h = [(n/100, n%100) for n in [hept(i) for i in range(1,800)] if ceil(log10(n)) == 4]
    x = [(n/100, n%100) for n in [hexa(i) for i in range(1,800)] if ceil(log10(n)) == 4]
    p = [(n/100, n%100) for n in [pent(i) for i in range(1,800)] if ceil(log10(n)) == 4]
    s = [(n/100, n%100) for n in [squa(i) for i in range(1,800)] if ceil(log10(n)) == 4]
    t = [(n/100, n%100) for n in [tria(i) for i in range(1,800)] if ceil(log10(n)) == 4]
    
    #print(len(o),len(h),len(x),len(p),len(s),len(t))

    sets = {0:o, 1:h, 2:x, 3:p, 4:s, 5:t}
    nums = [(item, key) for (key, itemlist) in sets.iteritems() for item in itemlist]
    where = []

    def next(v):
        return [a for a in nums if a[1] not in where and v[0][1] == a[0][0] and a != v]

    def dfs(v, depth, acc):
        #print(depth, len(where), acc, "--", where)
        if depth == 6:
            if acc[0][0][0] == acc[-1][0][1]:
                print(acc, sum([100*a[0]+a[1] for a,_ in acc]))
        else:
            for w in next(v):
                where.append(w[1])
                dfs(w, depth+1, acc+[w])
                where.pop()
    
    for x in nums:
        where.append(x[1])
        dfs(x, 1, [x])
        where.pop()
    
    print(time.clock() - t1, "seconds")
