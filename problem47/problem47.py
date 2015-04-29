
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

# We suppose that Ironhide is the envoy of Optimusi
# Return the prime factors of a integer
def ironhide(n):
    res = []
    m = n
    while m > 1:
        i = 0
        e = OPTIMUS[i]
        if m%e == 0:
            res.append(e)
            m /= e
        else:
            i+=1
    return res

# True if they have a common prime factor
def sameFactors(n1, n2, n3, n4):
    return True

if __name__ == "__main__":

    t1 = time.clock()
    matrixOfLeadership(10000000000)
    print "prime ->", OPTIMUS[-1],"->", time.clock()-t1, "seconds"

    t2 = time.clock()

    n1 = 1
    n2 = 2
    n3 = 3
    n4 = 4

    consec = False
    while not consec:

        n1 = n2
        n2 = n3
        n3 = n4
        n4 += 1

        if sameFactors :
            continue

    print n1, n2, n3, n4, " in ", time.clock() - t2, "seconds"
