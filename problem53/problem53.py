
import math
import time
import itertools

from itertools import combinations_with_replacement as combin
from math import factorial as fact

if __name__ == "__main__":
    
    t1 = time.clock()
    c = 0
    for n in range(1,101):
        for r in range(1,n+1):
            if fact(n)/(fact(r)*fact(n-r)) > 1000000:
                c += 1
    print(c)
    print(time.clock()-t1, "seconds")
