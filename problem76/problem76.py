
import time

from collections import defaultdict

def dynamic(f):
    cache = defaultdict(lambda: -1)
    def is_known(*args):
        if cache[args] == -1:
            cache[args] = f(*args)
        return cache[args]
    return is_known


@dynamic
def part(n, k):
    if n == 0 and k == 0:
        return 1
    elif k == 0:
        return 0
    elif k > n:
        return part(n, n)
    else:
        return part(n-k, k) + part(n, k-1)


if __name__ == "__main__":

    t1 = time.clock()

    print(part(12002,99))

    print(time.clock() - t1, "seconds")
