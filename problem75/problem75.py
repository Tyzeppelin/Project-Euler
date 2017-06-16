
import collections
import numpy as np
import time

from collections import defaultdict

def gen_prim_pyth_tripl(limit): 
    U = np.asarray([[1,2,2], [-2,-1,-2], [2,2,3]])
    A = np.asarray([[1,2,2], [2,1,2], [2,2,3]])
    D = np.asarray([[-1,-2,-2], [2,1,2], [2,2,3]])

    uad = np.array([U,A,D])
    M = np.asarray([3,4,5])

    while M.size:
        M = M.reshape(-1, 3)
        if limit:
            M = M[M[:, 2] <= N]
        for e in M:
            yield e
        M = np.dot(M, uad)

# one really fast way to iterate over pythagorean triplets
def gen_pyth_tripl(limit):
    for prim in gen_prim_pyth_tripl(limit):
        i = prim
        for _ in range(limit//prim[2]):
            yield i
            i = i + prim

if __name__ == "__main__":

    t1 = time.clock()

    N = 1500000 
    r = defaultdict(int)

    # Heavy.
    # thx wolfram http://mathworld.wolfram.com/PythagoreanTriple.html
    for tripl in gen_pyth_tripl(N):
        if sum(tripl) <= N:
            r[sum(tripl)] += 1

    print(len([k for k,v in r.iteritems() if v == 1]))
    print(time.clock() - t1, "seconds")
