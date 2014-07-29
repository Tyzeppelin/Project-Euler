
from math import *
import time

OPTIMUS = [2]

#Remove digits from left to right
def testLeft(n):
    t = n
    while t >= 1:
        if not isPrime(t):
            return False
        t = int(t%(10**int(log10(t))))
    return True

#Remove digits from right to left
def testRight(n):
    t = n
    while t >= 1:
        if not isPrime(t):
            return False
        t = int(t/10)
    return True


def isPrime (n):
    if n < 2:
        return False
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
    n = 11

    while ct < 11 :
        if isPrime(n):
            if testLeft(n) and testRight(n):
                ct += 1
                tab.append(n)
        n += 1


    print ct, tab, sum(tab)
    print "Prime generation + computation under", time.clock()-time1, "seconds"
