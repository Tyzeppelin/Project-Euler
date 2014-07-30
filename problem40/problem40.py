
import math
import time

def get(a, n):
    t = [int(i) for i in str(a)]
    return int(t[n-1])

if __name__ == "__main__":

    t1 = time.clock()
    sz = 1
    i = 2
    product = 1
    index = [10, 100, 1000, 10000, 100000, 1000000]

    while index != [] :

        sz += int(math.log10(i))+1

        #print i, sz, product, index[0], sz-int(math.log10(i)+1)

        if sz > index[0] and sz - int(math.log10(i)+1) < index[0] :
            diff = int(math.log10(i)+1) - sz + index[0]
            product *= get(i, diff)
            index = index[1:]
            #print i, sz, "=>", product, index
        i += 1

    print "for the  Champernowne's constant, d10 * d100 * d1000 * d10000 * d100000 * d1000000 =", product, "Job done under", time.clock()-t1, "seconds."
