
import collections
import math
import numpy
import time

# https://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples#Pythagorean_triples_by_use_of_matrices_and_linear_transformations
# Found this implem on stackoverflow, lost the url sadly :/
def gen_prim_pyth_tripl(limit):
    U = numpy.asarray([[1,2,2],[-2,-1,-2],[2,2,3]])
    A = numpy.asarray([[1,2,2],[2,1,2],[2,2,3]])
    D = numpy.asarray([[-1,-2,-2],[2,1,2],[2,2,3]])

    uad = numpy.asarray([U,A,D])
    M = numpy.asarray([3,4,5])

    while M.size:
        M = M.reshape(-1, 3)
        if limit:
            M = M[M[:, 2] <= limit]
        for e in M:
            yield e
        M = numpy.dot(M, uad)

# generate every pythagorean triple under value 'limit'
def gen_pyth_tripl(limit):
    for prim in gen_prim_pyth_tripl(limit):
        i = prim
        for _ in range(limit//prim[2]):
            yield i
            i = i + prim

t_cache = time.clock()
# We don't *need* values higher than 2000 but my generator is fast :3
cache = collections.defaultdict(lambda: [])
for (a,b,_) in gen_pyth_tripl(100000):
    cache[a].append(b)
    cache[b].append(a)
print("cache populated in", time.clock() - t_cache, "seconds.")

# n(log_2(n)) - à vue de pif
# we compute how many differents (i, j, k) can generate
# the Pythagorean triple (a,b,_) whith a:=i and b:=j+k and i >= j >= k
def solution(n, max_k=100, cache=cache):
    l = 0
    for i in range(3, max_k):
        # for every pythagorean triple (i, b, _)
        for b in [b for b in cache[i] if b < 2*i]:
            if i > b:
                l += b//2
            else:
                l += (2*i-b)//2 + 1
        if l >= n:
            return i, l
    return l

if __name__ == '__main__':

    t1 = time.clock()

    TARGET=1000000

    # 2000 seemed like a good upper bound, lucky guess.
    print(solution(TARGET, max_k=2000))

    print("Done under", time.clock() - t1, "seconds")
