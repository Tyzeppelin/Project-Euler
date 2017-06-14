
import itertools
import time

from itertools import permutations
from operator import itemgetter

# Solve 5 eq with 5 equality tests and 10 additions
#
# 5-gon ring -> numbers from 1 to 10
# 
#
# /
# | x_1 + x_6 = x_4 + x_5
# | x_2 + x_7 = x_0 + x_6
# | x_3 + x_8 = x_1 + x_7
# | x_4 + x_9 = x_2 + x_8
# | x_0 + x_5 = x_3 + x_9
# \
#
#Plus -> triplets have to be presented clockwise
#     -> summary str has to be 16 char long
def get_sol_10():
    ref = list(range(1, 11))

    for p in permutations(ref):
        if (p[1] + p[6]) != (p[4] + p[5]):
            continue
        if (p[2] + p[7]) != (p[0] + p[6]):
            continue
        if (p[3] + p[8]) != (p[1] + p[7]):
            continue
        if (p[4] + p[9]) != (p[2] + p[8]):
            continue
        if (p[0] + p[5]) != (p[3] + p[9]):
            continue

        so = [(p[6], p[0], p[1]), (p[7], p[1], p[2]), (p[8], p[2], p[3]), (p[9], p[3], p[4]), (p[5], p[4], p[0])]
        
        min_index, _ = min(enumerate(so), key=itemgetter(1))

        so = list(so[min_index:]) + list(so[:min_index])

        res = ''.join(map(str, [a for tu in so for a in tu]))
        
        if len(res) != 16:
            continue

        yield p[6] + p[0] + p[1], int(res)


if __name__ == "__main__":

    t1 = time.clock()

    print(max(get_sol_10(), key=itemgetter(1)))

    print(time.clock() - t1, "seconds")
