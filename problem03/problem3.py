
import time

from math import sqrt

LARGE_NUMBER = 600851475143

def isPrime (n) :
	
    k = int(sqrt(n))
    res = True
    while k > 3 :
        if n%k == 0 :
            return False
        k -= 1 
    return True


if __name__ == "__main__" :

    t1 = time.clock()

    i = int(sqrt(LARGE_NUMBER))
    while i > 2 :
        if (LARGE_NUMBER%i == 0) and isPrime(i) :
            break
        i -= 1 
    print(i)
    print(time.clock() - t1, "seconds")
