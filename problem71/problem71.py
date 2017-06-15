
import time

from fractions import gcd

def simplify(n,d):
    g = gcd(n,d)
    return n/g, d/g

if __name__ == "__main__":

    t1 = time.clock()


    ref = 3.0/7
    m = 2.0/7
    max_n = 2
    for d in range(2, 1000000):
        for n in range(int(ref*d+1), int(m*d), -1):
            if float(n)/d > m and float(n)/d < ref:
                m = float(n)/d
                max_n = simplify(n, d)[0]
                break
    print(max_n) 

    print(time.clock() - t1, "seconds")
