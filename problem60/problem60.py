
import collections
import copy
import random
import time

from collections import defaultdict

# from rosetta code
# http://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python
def isPrime(n):
    assert n >= 2
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)
 
    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite
 
    for i in range(10):
        a = random.randrange(2, n)
        if try_composite(a):
            return False
 
    return True # no base tested showed n as composite

def prime_iterator():
    yield 2
    i = 3
    while True:
        if isPrime(i):
            yield i
        i+=2

def get_5_conn(graph):

    if len(graph.keys()) < 5:
        return False, None
    g = copy.deepcopy(graph)
    conn = {k:len(v) for (k,v) in g.iteritems()}

    if reduce(lambda it, x: it+(x>4), conn.values()) < 5:
        return False, None

    while reduce(lambda it, x: it+(x>4), conn.values()) > 5:
        disc = min(conn, key=conn.get)
        g.pop(disc)
        for v in g.values():
            v.discard(disc)

        conn = {k:len(v) for (k,v) in g.iteritems()}
    if len(conn) == 5 and sum(conn.values()) == 20:
        return True, g
    return False, None
       


if __name__ == "__main__":

    t1 = time.clock()

    OPTIMUS = []
    graph = defaultdict(set)
    c = 0
    for e in prime_iterator():
        #print(e)
        for p in OPTIMUS:
            if isPrime(int(str(e)+str(p))) and isPrime(int(str(p)+str(e))):
                #print(int(str(e)+str(p)),int(str(p)+str(e)),"----> graph["+str(e)+"]->",graph[e], "graph["+str(p)+"]->", graph[p])
                graph[e].add(p)
                graph[p].add(e)
        if c % 10 == 0:
            #print(e)
            isok, scc = get_5_conn(graph)
            if isok:
                print(e, scc)
                break
        c += 1
        OPTIMUS.append(e)
    print([sum(v)+k for (k,v) in scc.iteritems()])
    print(time.clock() - t1, "seconds")
