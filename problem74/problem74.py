
import collections
import math
import time

from collections import defaultdict
from math import factorial

def dynamic(f):
    cache = defaultdict(lambda: -1)
    def is_known(*args): 
        if cache[args] == -1:
            cache[args] = f(*args)
        return cache[args]
    return is_known

@dynamic
def next_fact(n):
    return sum(map(lambda x: factorial(x), map(int, str(n))))

if __name__ == "__main__":

    t1 = time.clock()

    chain = defaultdict(int)
    c = 0

    for n in range(1000000):
        curr_chain = [n]
        curr_ptr = next_fact(n)
        chain_size = 1
        while curr_ptr not in curr_chain:
            if chain[curr_ptr] != 0:
                chain_size += chain[curr_ptr]
                break
            curr_chain.append(curr_ptr)
            curr_ptr = next_fact(curr_ptr)
            chain_size += 1
        if chain_size == 60:
            c += 1
        chain[n] = chain_size
        #print(n, chain_size)

    print(c)
    print(time.clock() - t1, "seconds")
