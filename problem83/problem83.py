
import collections
import decimal
import heapq
import itertools
import operator
import time

from collections import defaultdict
from decimal import Decimal
from operator import itemgetter
from itertools import product



CC = [2,17,33]
CH = [7,22,36]
JA = [10,30]
R = [5,15,25,35]
U = [12,28]

def next_R(n):
    return next((r for r in R if r > n), 5 )
def next_U(n):
    return next((u for u in U if u > n), 12)

def roll_CC(sq):
    return {00: 1, 10: 1, sq: 14} 
def roll_CH(sq):
    return {0: 1, 10:1, 11:1, 24:1, 39:1, 5:1, next_R(sq):2, next_U(sq):1, (sq-3)%40:1, sq:6}


if __name__ == "__main__":

    t1 = time.clock()

    decimal.getcontext().prec = 20

    acc = defaultdict(int)


    d4 = [1,2,3,4]
    nbP = len(d4)**2.0
    acc = defaultdict(int)
    for a in product(d4,d4):
        acc[sum(a)] += 1
    prob_t1 = defaultdict(lambda: Decimal(0))
    for k,v in acc.iteritems():
        if k in CC:
            for k1, v1 in roll_CC(k).iteritems():
                prob_t1[k1] += Decimal(v)*Decimal(v1)/(Decimal(nbP)*Decimal(16))
        elif k in CH:
            for k1, v1 in roll_CH(k).iteritems():
                prob_t1[k1] += Decimal(v)*Decimal(v1)/(Decimal(nbP)*Decimal(16))
        elif k in JA:
            prob_t1[10] += Decimal(v)/Decimal(nbP)
        else: 
            prob_t1[k] = Decimal(v)/Decimal(nbP)
 
    print(prob_t1, sum(prob_t1.values()))
    print(max(prob_t1, key=prob_t1.get))

    #print(list(product(product(d4,d4), prob_t1.keys())))

    prob_t2 = defaultdict(lambda: Decimal(0))
    for sq, d in product(prob_t1.keys(), product(d4,d4)):
        if sq+sum(d) in CC:
            for k1, v1 in roll_CC(sq+sum(d)).iteritems():
                prob_t2[k1] += prob_t1[sq]*Decimal(v1)/(Decimal(nbP)*Decimal(16))
        elif sq+sum(d) in CH:
            for k1, v1 in roll_CH(sq+sum(d)).iteritems():
                prob_t2[k1] += prob_t1[sq]*Decimal(v1)/(Decimal(nbP)*Decimal(16))
        elif sq+sum(d) in JA:
            prob_t2[10] += prob_t1[sq]/(Decimal(nbP))
        else:
            prob_t2[sq+sum(d)] += prob_t1[sq]/Decimal(nbP)

    print(prob_t2)
    print(sum(prob_t2.values()), max(prob_t2, key=prob_t2.get))

    prob_t3 = defaultdict(lambda: Decimal(0))
    for sq, d in product(prob_t2.keys(), product(d4,d4)):
        if sq+sum(d) in CC:
            for k1, v1 in roll_CC(sq+sum(d)).iteritems():
                prob_t3[k1] += prob_t2[sq]*Decimal(v1)/(Decimal(nbP)*Decimal(16))
        elif sq+sum(d) in CH:
            for k1, v1 in roll_CH(sq+sum(d)).iteritems():
                prob_t3[k1] += prob_t2[sq]*Decimal(v1)/(Decimal(nbP)*Decimal(16))
        elif sq+sum(d) in JA:
            prob_t3[10] += prob_t2[sq]/(Decimal(nbP))
        else:
            prob_t3[sq+sum(d)] += prob_t2[sq]/Decimal(nbP)

    print(prob_t3)
    print(sum(prob_t3.values()), max(prob_t3, key=prob_t3.get))

    probs = defaultdict(lambda: Decimal(0))
    for (s1,p1),(s2,p2),(s3,p3) in zip(prob_t1.iteritems(), prob_t2.iteritems(), prob_t3.iteritems()):
        probs[s1] += p1
        probs[s2] += p2
        probs[s3] += p3

    print(probs, max(probs, key=probs.get))
    print(sorted(probs.iteritems(), key=itemgetter(1)))
    print(sum(probs.values()))

    print('\n\n\n\n\n')

    doubles = list(product(((1,1), (2,2), (3,3), (4,4), (5,5), (6,6)), repeat=3))
    print(set(map(lambda l: sum(l[0])+sum(l[1])+sum(l[2]), doubles)))


    print(time.clock() - t1, "seconds")
