
import math
import time

def isPentagonal(n):
    return (1/6.0 * (1 + math.sqrt(24*n + 1)))%1 == 0.0


def Pentagonal(n):
    i = 1
    arr = []
    while i <= n:
        arr.append(i*(3*i-1)/2)
        i+=1
    return arr

if __name__ == "__main__":

    t1 = time.clock()

    base = Pentagonal(10000)
    dmin = 10**10

    for pj in base:
        for pk in base[base.index(pj)+1:]:
            #print pk, pj, pk+pj, pk-pj
            if isPentagonal(pj+pk) and isPentagonal(abs(pk-pj)):
                print "couple -> ", pk, pj, "diff ->", pk-pj
                dmin = min(dmin,abs(pk-pj))

    print dmin

    print "Done under", time.clock()-t1, "seconds."
