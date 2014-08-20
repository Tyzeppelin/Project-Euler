

import math
import time

def isTriangular(n):
    return 1/2.0*(math.sqrt(8*n+1)-1)%1 == 0.0

def isPentagonal(n):
    return 1/6.0*(math.sqrt(24*n+1)+1)%1 == 0.0



if __name__ == "__main__":

    t1 = time.clock()

    gotcha = False
    i = 144
    h = 0

    while not gotcha:
        h = i*(2*i-1)
        if isTriangular(h) and isPentagonal(h):
            gotcha = True
            res = h
        i += 1

    print res
    print "Done under", time.clock()-t1, "seconds"
