
import decimal
import time

from decimal import Decimal
from math import sqrt

def non_squared_generator(n):
    for n in range(2, n+1): 
        if sqrt(n) % 1.0 != 0.0:
            yield n

if __name__ == "__main__":

    decimal.getcontext().prec = 102

    t1 = time.clock()

    n = 0
    for a in non_squared_generator(99):
        sq = Decimal(a).sqrt()
        sm =  sum(map(int, str(sq)[:101].split('.')[1]))
        n += sm + int(sqrt(a))
        #print(a, str(sq)[:101], sm + int(sqrt(a)))
        
    
    print(n)
    print(time.clock() - t1, "seconds")
