
import time

from fractions import gcd

if __name__ == "__main__":

    t1 = time.clock()

    c = 0

    min_f = 1.0/3
    max_f = 1.0/2

    for d in range(4, 12001):
        for n in range(int(d/3.0), int(d/2.0+1)):
            if gcd(n,d) == 1:
                if float(n) / d < max_f and float(n) / d > min_f:
                    c += 1
    print(c)
    print(time.clock() - t1, "seconds")
