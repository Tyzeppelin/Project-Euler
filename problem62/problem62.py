
import itertools
import math
import time

from collections import defaultdict
from math import log10

def is_cube(n):
    c = int(n**(1./3))
    return c**3 == n or (c+1)**3 == n

walmart = defaultdict(set)

def store(x):
    c = defaultdict(int)
    for i in map(int, str(x)):
        c[i] += 1
    h = 0
    for k,v in c.iteritems():
        h+=(v*10**k)
    walmart[h].add(x)
    if len(walmart[h]) == 5:
        return True, walmart[h]
    return False, None


if __name__ == "__main__":

    t1 = time.clock()

    for i in range(1000, 10000):
        if is_cube(i**3):
            b,s =  store(i**3)
            if b:
                print('==', s, "==")
                print(min(s))
                break
    print(time.clock() - t1, "seconds")
