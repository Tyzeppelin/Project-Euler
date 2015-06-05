
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

# We suppose that Ironhide is the envoy of Optimus
# Return the prime factors of a integer
def ironhide(n):
    res = []
    m = n
    i = 0
    while m > 1:
        e = OPTIMUS[i]
        if m%e == 0:
            res.append(e)
            m /= e
        else:
            i+=1
    #print n, len(group(res)), "\t", group(res)
    return group(res)

def group(arr):
    res = {}
    for e in arr:
        if e in res:
            res[e] += 1
        else:
            res[e] = 1
    return [k ** v for k,v in res.items()]


if __name__ == "__main__":

    t1 = time.clock()
    matrixOfLeadership(30000000000)
    print "prime ->", OPTIMUS[-1],"->", time.clock()-t1, "seconds"

    t2 = time.clock()

    n1 = 11
    n2 = 12
    n3 = 13
    n4 = 14

    k = 1

    three = False
    while not three:

        n1 += k
        n2 += k
        n3 += k
        n4 += k

        if len(ironhide(n4)) < 4:
            k = 4
        elif len(ironhide(n3)) < 4:
            k = 3
        elif len(ironhide(n2)) < 4:
            k = 2
        elif len(ironhide(n1)) < 4:
            k = 1
        else :
            three = True

    print n1, n2, n3, n4, " in ", time.clock() - t2, "seconds"
