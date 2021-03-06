
import time
import math

OPTIMUS = [2]

def isPrime(n):
    if n < 2:
        return False
    for prime in OPTIMUS :
        if prime > math.sqrt(n):
            break
        if n % prime == 0:
            return False
    return True


#We need the matrix of Leadership to make Optimus stronger
def matrixOfLeadership(n):
    i = OPTIMUS[-1]
    while i < math.sqrt(n):
        isP = True
        for prime in OPTIMUS:
            if i%prime == 0:
                isP = False
                break
        if isP:
            OPTIMUS.append(i)
        i += 1

if __name__ == "__main__":

    t1 = time.clock()
    matrixOfLeadership(10000000000)
    print "prime ->", OPTIMUS[-1],"->", time.clock()-t1, "seconds"

    t2 = time.clock()
    n = 9
    while n < 1000000:
        conj = False
        for e in OPTIMUS:
            if OPTIMUS.count(n) == 1:
                conj = True
                break
            rem = n - e
            if rem <= 0:
                break
            elif math.sqrt(rem/2.0)%1 == 0.0:
                conj = True
                break
        if not conj:
            break
        n += 2

print n, "isn't satisfying goldbach, you bastard.", time.clock() - t2, "seconds"
