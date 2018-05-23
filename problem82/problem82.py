
import numpy as np
import time

from collections import defaultdict
from functools import reduce
from math import sqrt

# As ye auld sayin' goes: "If it's a tree, it's easy"
# But this time, the problem is no tree

def neigh(p, sz_mat):
    if p == 0:
        return [sz_mat*i+1 for i in range(sz_mat)]
    if p == sz_mat**2+1:
        return []
    if p in [sz_mat*i for i in range(sz_mat+1)[1:]]:
        return [sz_mat**2+1]
    if p in range(sz_mat):
        return [p+1, p+sz_mat]
    if p in range(sz_mat**2)[-sz_mat+1:]:
        return [p+1, p-sz_mat]
    else:
        return [p+1, p+sz_mat, p-sz_mat]

def dijkstra(src, coef):

    #print(coef, coef.size)

    sz_mat = int(sqrt(coef.size-1))

    Q = list(range(coef.size))
    dist = defaultdict(lambda: float('inf'))
    prev = defaultdict(lambda: None)

    dist[src] = 0

    while len(Q) != 0:
        u = reduce(lambda m, x: m if dist[m] < dist[x] else x, Q)
        Q.remove(u)

        for v in neigh(u, sz_mat):
            #print("## ", u, v)
            alt = dist[u] + coef[v]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    return dist, prev



if __name__ == '__main__':

    t1 = time.clock()

    with open("matrix.txt", 'r') as f:
        matrix = np.asarray([[int(v) for v in l.rstrip().split(',')] for l in f.readlines()])
        coef = np.concatenate(([0], matrix.flatten(), [0]))

    #print(matrix)
    #print(coef)
    #print(np.min(matrix), np.max(matrix))
    res_d, res_p = dijkstra(0, coef)
    print(res_d[coef.size-1])
    #print(res_p)

    print(time.clock() - t1, "seconds")
