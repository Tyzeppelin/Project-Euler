
import time

from collections import defaultdict
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


die = [1,2,3,4,5,6]

double_roll = list(product(die, die))


def comb():
    r = defaultdict(lambda: 0)
    for (d1, d2) in double_roll:
        roll1 = d1+d2
        if roll1 in CC:
            r[00] += 1/16
            r[10] += 1/16
            r[roll1] += 14/16
        elif roll1 in CH:
            r[00] += 1/16
            r[10] += 1/16
            r[11] += 1/16
            r[24] += 1/16
            r[39] += 1/16
            r[5] += 1/16
            r[next_R(roll1)] += 2/16
            r[next_U(roll1)] += 1/16
            r[roll1-3] += 1/16
            r[roll1] += 6/16
        else:
            pass
        if d1 != d2:
            r[roll1] += 1
        else:
            for (d3, d4) in double_roll:
                roll2 = roll1 + d3 + d4
                if roll2 in CC:
                    r[00] += 1/36/16
                    r[10] += 1/36/16
                    r[roll2] += 14/36/16
                elif roll2 in CH:
                    r[00] += 1/36/16
                    r[10] += 1/36/16
                    r[11] += 1/36/16
                    r[24] += 1/36/16
                    r[39] += 1/36/16
                    r[5] += 1/36/16
                    r[next_R(roll2)] += 2/36/16
                    r[next_U(roll2)] += 1/36/16
                    r[roll2-3] += 1/36/16
                    r[roll2] += 6/36/16
                else:
                    pass
                if d3 != d4:
                    r[roll2] += 1/36
                else:
                    for (d5, d6) in double_roll:
                        roll3 = roll2 + d5 + d6
                        if d5 == d6:
                            r[10] += 1/36/36
                        if roll3 == 30:
                            r[10] += 1/36/36
                        elif roll3 in CC:
                            r[00] += 1/36/36/16
                            r[10] += 1/36/36/16
                            r[roll3] += 14/36/36/16
                        elif roll3 in CH:
                            r[00] += 1/36/36/16
                            r[10] += 1/36/36/16
                            r[11] += 1/36/36/16
                            r[24] += 1/36/36/16
                            r[39] += 1/36/36/16
                            r[5] += 1/36/36/16
                            r[next_R(roll3)] += 2/36/36/16
                            r[next_U(roll3)] += 1/36/36/16
                            r[roll3-3] += 1/36/36/16
                            r[roll3] += 6/36/36/16
                        else :
                            r[roll3] += 1/36/36
    return r

if __name__ == "__main__":

    t1 = time.process_time()

    ll = comb()

    res = {k: v for k,v in sorted(ll.items(), key=lambda x: x[1], reverse=True)}

    for (k,v) in res.items():
        print(k,v)

    print(sum(ll.values()))

    print(time.process_time() - t1, "seconds")
