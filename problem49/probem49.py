
import time

OPTIMUS = [2,3]

def bumblebee (n):
    if OPTIMUS[-1] > n :
        return

    i = OPTIMUS [-1]
    prime = True
    while i < n:
        prime = True
        for p in OPTIMUS :
            if i % p == 0:
                prime = False
                break
        if prime :
            OPTIMUS.append(i)
        i += 2
    return [p for p in OPTIMUS if p > 1000]

def isPermut(n, m):
    a = map(int, str(n))
    a.sort()
    b = map(int, str(m))
    b.sort()
    return a == b and n != m

def isSequence(arr):
    i = 1
    n = len(arr)-1
    last = arr[1]-arr[0]
    while i < n:
        if arr[i+1]-arr[i] != last:
            return False
        i+=1
    return True

if __name__ == "__main__":

    t1 = time.clock()

    prime = bumblebee(10000)
    #print prime, len(prime)

    t2 = time.clock()
    acc = [[]]
    i = 1
    for p in prime:
        for q in prime[i:]:
            if isPermut(p, q):
                acc[-1].append(q)
        acc.append([])
        i+=1
    acc = [arr for arr in acc if len(arr)>=3 and isSequence(arr)]
    print acc

    print "exec under", time.clock()-t1, "seconds"
