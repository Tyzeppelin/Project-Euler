import time

from collections import defaultdict

def dynamic(f):
    cache = defaultdict(lambda:-1)
    def is_known(*args):
        if cache[args] == -1:
            cache[args] = f(*args)
        return cache[args]
    return is_known

def nextCurrency(c):
    curr_ptr = currency.index(c)
    if curr_ptr == 0 :
        return 0
    else :
        return currency[curr_ptr-1]

@dynamic
def part(n, k):
    if n == 0 and k == 0:
        return 1
    elif k == 0:
        return 0
    elif k > n:
        return part(n, n)
    else:
        return part(n-k, k) + part(n, nextCurrency(k))

if __name__ == "__main__":
    t1 = time.clock()

    currency = [1, 2, 5, 10, 20, 50, 100, 200]
    a = part(200, currency[-1])
    print(a)
    print("Completed in", time.clock()-t1, "seconds")
