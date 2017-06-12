
import math
import re
import time

from math import sqrt

def gen_continued_fraction(n, k=10):
    a0 = int(sqrt(n))
    num = -a0
    den = 1 
    ak = []
    #print(ak, num, den)

    for _ in range(k):
        an = int(den/(sqrt(n)+num))
        den = (n - num ** 2) / den
        num = - num - an * den

        ak.append(an)
        #print(ak, num, den)
    return a0, ak 

def non_squared_generator(n):
    for n in range(2, n+1): 
        if sqrt(n) % 1.0 != 0.0:
            yield n

def isCycle(s, sub):
    for e in range(0, len(s)-len(sub), len(sub)):
        if s[e:e+len(sub)] != sub:
            return False
    return True

if __name__ == "__main__":

    t1 = time.clock()

    #print(gen_continued_fraction(23, 20))

    c = 0
    for n in non_squared_generator(10000):
        a0, ak = gen_continued_fraction(n, 1000)
        for i in range(1, len(ak)/2):
            if isCycle(ak, ak[:i]): 
                if i%2 != 0:
                    #print(ak, ak[:i], n, i)
                    c += 1
                break

    print(c)
    print(time.clock() - t1, "seconds")
