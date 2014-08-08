
import math
import time


def stringToInt(s):
    sum = 0
    for e in s :
        sum += (ord(e) - 64)
    return sum


def isTriangular(n):
    ist = False
    try:
        index = -0.5+math.sqrt(0.25+2*n)
        if index%1 == 0.0:
            ist = True
    except ValueError:
        ist = False
    return ist


if __name__ == "__main__" :

    t1 = time.clock()

    f = open("words.txt", "r")
    l = [e[1:-1] for e in f.read().split(",")]

    ct = 0

    for s in l:
        if isTriangular(stringToInt(s.upper())):
            ct +=1
    print ct, """ triangulars words in the file "words.txt"."""
    print "execute under", time.clock()-t1, "seconds"
