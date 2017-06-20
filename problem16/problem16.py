
import math
import time

from math import *

def add (n) :
	
    i = 0
    j = int(log10(n))+1

    result = 0
    while i < j :
	result += n%10
        n/=10
        i+=1
    return result


if __name__ == "__main__" :

    t1 = time.clock()

    a = 2**1000
    print(add(a))
    print(time.clock() - t1, "seconds")
