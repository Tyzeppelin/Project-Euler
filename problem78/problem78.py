
import math
import sys
import time

from collections import defaultdict
from math import sqrt

def dynamic(f):
    cache = defaultdict(lambda: -1)
    def is_known(*args):
        if cache[args] == -1:
            cache[args] = f(*args)
        return cache[args]
    return is_known

#@dynamic
#def part(n, k):
#    if n == 0 and k == 0:
#        return 1
#    if k == 0:
#        return 0
#    elif k > n:
#        return part(n, n)
#    else:
#        return part(n-k, k) + part(n, k-1)


@dynamic
def part(n):
    if n == 1 or n == 0:
        #print('hit')
        return 1
    
    s = 0
    k = 1
    p = (3*k**2-k)/2

    while p <= n:
        #print(n,k,p,s)
        if k % 2 == 0:
            s -= part(n - p)
            if (p + k) <= n:    
                s -= part(n - p - k)
        else:
            s += part(n - p)
            if (p + k) <= n:
                s += part(n - p - k)
        k += 1
        p = (3*k**2-k)/2
    return s


if __name__ == "__main__":

    t1 = time.clock()

    #r = []
    #t2 = time.clock()   
    #for i in range(1000):
    #    r.append(part(i,i))
    #print("part1 : ", time.clock() - t2, "seconds")

    #r = []
    #t2 = time.clock()
    #for i in range(1000):
    #    r.append(part2(i))
    #print("part2 : ", time.clock() - t2, "seconds")
    
    i = 1
    while part(i) % 1000000 != 0:
        i += 1
    print(i, part(i))

    print(time.clock() - t1, "seconds")
