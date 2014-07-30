
import math
import time
import collections

if __name__ == "__main__":

    t1 = time.clock()

    a = 1
    b = 1
    c = 1
    res = {}

    while a < 500:
        b = 1

        while b <= a:
            c = math.sqrt(a**2 + b**2)
            #print a, b, c
            if c%1 == 0 and a+b+c <= 1000:
                p = int(a+b+c)
                try :
                    res[p] += 1
                except KeyError:
                    res[p] = 1
                #print a, b, int(c), p, res[p]
            b += 1
        a += 1

    maxV = 0
    maxP = 0

    iterRes = collections.OrderedDict(sorted(res.items()))
    for k, v in iterRes.iteritems():
        #print k, v
        if v > maxV:
            maxV = v
            maxP = k

    print "Perimeter ->", maxP, "hit", maxV, "times." , "Done under", time.clock()-t1, "seconds"



