
import itertools
import time

from collections import defaultdict

g = 0
ca = 0

def dynamic(f):
    cache = defaultdict(lambda:-1)
    def is_known(*args):
        global ca
        global g
        if cache[args] == -1:
            g += 1
            cache[args] = f(*args)
        else:
            ca += 1
        return cache[args]
    return is_known

@dynamic
def is_cube(n):
    n = int(''.join(n))
    c = int(n**(1./3))
    return c**3 == n or (c+1)**3 == n

if __name__ == "__main__":

    t1 = time.clock()

    #n = 345**3
    #print(int(''.join(['4','1','0','6','3','6','2','5']))**(1./3) % 1.0 == 0)
    #print([int(''.join(p))**(1./3)%1.0 == 0.0 for p in itertools.permutations(str(n))])

    #print(sum([is_cube(int(''.join(p))) for p in itertools.permutations(str(n))]))

    for i in range(10000):
        c = set()
        n = i ** 3
        for p in [u for u in itertools.permutations(str(n)) if u[0]!='0']:
            if is_cube(p):
                c.add(p)
        #print(i,"** 3", len(c), c)
        if len(c) == 5:
            print('==', i**3, "==")
            break
    print(ca, g)
    print(time.clock() - t1, "seconds")
