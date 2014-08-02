
import time
import math


OPTIMUS = [2]


def isPandigital(n):
    arr = [int(i) for i in str(n)]
    arr.sort()
    base = range(int(math.log10(n)+2))[1:]
    return arr == base


def nextPrime(n):
    if math.sqrt(n) > OPTIMUS[-1]:
        MatrixOfLeadership(n)
    i = n+1
    while not isPrime(i):
        i += 1
    return i


def isPrime (n):
    if n < 2:
        return False
    for prime in OPTIMUS:
        if prime > math.sqrt(n) :
            break
        if n%prime == 0:
            return False
    return True


# To make OPTIMUS greater
def MatrixOfLeadership (n):
    print "Make OPTIMUS stronger"
    i = OPTIMUS[-1]
    while i < math.sqrt(n):
        isP = True
        for prime in OPTIMUS:
            if i%prime == 0:
                isP = False
                break
        if isP:
            OPTIMUS.append(i)
        i+=1


if __name__ == "__main__":

    t1 = time.clock()

    MatrixOfLeadership(987654321)
    print OPTIMUS

    bumblebee = OPTIMUS[0]
    sentinel = 0

    print "wadifuck"

    # I started with 7654321 cause all the 1-8 and 1-9 pandigital
    # are multiple of 9 (their sums equals a multiple of 9)
    i = 7654321
    done = False

    while not done:
        if isPandigital(i):
            if isPrime(i):
                print i
                sentinel = i
                done = True
        i -= 2

    print "sentinel (", sentinel, ")generate way more power than 1.21 Gigowatt ->", time.clock()-t1, "seconds"
