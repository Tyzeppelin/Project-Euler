
import math
import time

from math import log10, ceil

if __name__ == "__main__":

    t1 = time.clock()

    c = 0
    for i in range(1, 50):
        cl = 0
        for n in range(1,10):
            if ceil(log10(n**i)) == i:
                print(i, n**i)
                c += 1
                cl += 1
        print(i, cl)

    print(c)
    print(time.clock() - t1, "seconds")
