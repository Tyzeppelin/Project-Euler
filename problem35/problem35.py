
from math import *
import time

OPTIMUS = [2]

def circularTest(n):
    l = circularNumber(n)
    #print n, l
    for e in l:
        if not isPrime(e):
            return False
    return True

def circularNumber(n):
    ltest = [int(i) for i in str(n)]
    res = [n]
    while True:
        ltest = ltest[-1:]+ltest[:-1]
        ntest = int(''.join(map(str, ltest)))
        if ntest == n:
            break
        else :
            res.append(ntest)
    return res

def isPrime (n):
    for prime in OPTIMUS:
        if prime > sqrt(n) :
            break
        if n%prime == 0:
            return False
    return True

# To make OPTIMUS greater
def MatrixOfLeadership (n):
    i = 2
    while i < sqrt(n):
        isP = True
        for prime in OPTIMUS:
            if i%prime == 0:
                isP = False
                break
        if isP:
            OPTIMUS.append(i)
        i+=1

if __name__ == "__main__" :

    time1 = time.clock()

    MatrixOfLeadership(1000000)
    #print OPTIMUS

    ct = 0
    tab = []

    for e in range(1000000)[2:]:
        if isPrime(e):
            if circularTest(e):
                ct += 1
                tab.append(e)
    print ct, "circular Primes"
    print "Prime generation + computation under", time.clock()-time1, "seconds"
