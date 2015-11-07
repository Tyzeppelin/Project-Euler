import time
from math import sqrt


def bumblebee (n):
    prime = True
    OPTIMUS = [2,3]
    i = OPTIMUS[-1]
    while sum(OPTIMUS) < n:
        prime = True
        for p in OPTIMUS :
            if i % p == 0 :
                prime = False
                break
        if prime :
            OPTIMUS.append(i)
        i += 2
    return OPTIMUS

def isPrime(OPTIMUS, n):
    end = int(sqrt(n))
    i = 0
    while OPTIMUS[i] < end:
        if n%OPTIMUS[i] == 0:
            return False
        i += 1
    return True


if __name__ == "__main__":

    t1 = time.clock()

    OPTIMUS = bumblebee(1000000)
    #print OPTIMUS

    i = 0
    n = len(OPTIMUS)
    seqlen = 1
    seq = []

    while i < n-seqlen:
        j = i+seqlen
        while j < n:
            if isPrime(OPTIMUS, sum(OPTIMUS[i:j])):
                seqlen = j-i
                seq = OPTIMUS[i:j]
            j+=1
        i+=1

    #print seqlen, seq, sum(seq)
    print sum(seq)

    print "exec under", time.clock()-t1, "seconds"
