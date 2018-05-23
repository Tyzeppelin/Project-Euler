
import numpy as np
import time

from collections import defaultdict
from functools import reduce
from math import sqrt

# As ye auld sayin' goes: "If it's a tree, it's easy"
# But this time, the problem is no tree

def neigh(p, sz_mat):
    #up-left
    if p == 0:
        return [1, sz_mat]
    #down-right
    if p == sz_mat**2-1:
        return []
    #up-right
    if p == sz_mat-1:
        return [p-1, p+sz_mat]
    #up row
    if p < sz_mat:
        return [p-1, p+1, p+sz_mat]
    #down-left
    if p == sz_mat*(sz_mat-1):
        return [p-sz_mat, p+1]
    #left column
    if p%sz_mat == 0:
        return [p-sz_mat, p+1, p+sz_mat]
    #right column
    if p%sz_mat == sz_mat-1:
        return [p-1, p-sz_mat, p+sz_mat]
    #down row
    if p > sz_mat*(sz_mat-1):
        return [p-sz_mat, p-1, p+1]
    else:
        return [p-1, p+1, p-sz_mat, p+sz_mat]


def dijkstra(src, coef):

    #print(coef, coef.size)

    sz_mat = int(sqrt(coef.size))

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
        coef = matrix.flatten()

    #print(matrix)
    #print(coef)
    #print(np.min(matrix), np.max(matrix))
    res_d, res_p = dijkstra(0, coef)
    #don't forget to add the first coef.
    print(res_d[coef.size-1]+coef[0])
    #print(res_p)

    print(time.clock() - t1, "seconds")
