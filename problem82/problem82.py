
import numpy as np
import collections
import time

from collections import defaultdict

# As ye auld sayin' goes: "If it's a tree, it's easy" 
# But this time, the problem is no tree

def neigh(n):
    if n[0] == 0:
        yield (n[0]+1, n[1])
    elif n[0] == 79:
        if n[1] == 0:
            yield (79,1)
        elif n[1] == 79:
            yield (79,78)
        else:
            yield (79, n[1]-1)
            yield (79, n[1]+1)
    elif n[1] == 0:
        yield (n[0],n[1]+1)
        yield (n[0]+1,n[1])
    elif n[1] == 79: 
        yield (n[0]+1, n[1])
        yield (n[0], n[1]-1)
    else:
        yield (n[0]+1, n[1])
        yield (n[0], n[1]+1)
        yield (n[0], n[1]-1)

def dijkstra(src, mat):

    Q = []
    dist = defaultdict(lambda: float('inf'))
    prev = defaultdict(lambda: None)
    
    for i in range(80):
        for j in range(80):
            Q.append((i,j))
                
    dist[src] = mat[src[0]][src[1]]

    while len(Q) != 0:
        u = reduce(lambda m, x: m if dist[m] < dist[x] else x, Q)
        Q.remove(u)

        for v in neigh(u):
            alt = dist[u] + mat[v[0]][v[1]]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    return dist, prev
            


if __name__ == '__main__':

    t1 = time.clock()

    with open("matrix.txt", 'r') as f:
        matrix = [[int(v) for v in l.rstrip().split(',')] for l in f.readlines()]

    print(np.asarray(matrix))
    print(np.min(matrix), np.max(matrix))
    #res_d, res_p = dijkstra((0,0), matrix)
    
    #print({k:v for k,v in res_d.iteritems() if k[0] == 79})
    #print(min([v for k,v in res_d.iteritems() if k[0] == 79]))

    print(time.clock() - t1, "seconds")
