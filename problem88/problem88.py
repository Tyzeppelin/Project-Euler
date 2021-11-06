
import collections
import functools
import itertools
import time

def dynamic(f):
    cache = collections.defaultdict(lambda: [])
    def is_known(*args):
        key = "".join(map(str, args))
        if cache[key] == []:
            cache[key] = f(*args)
        return cache[key]
    return is_known


@dynamic
def divisors(n, k):
    res = []
    for e in range(2, max(n, n//4+1)):
        if n%e == 0:
            if (e <= k):
                res.append(e)
            if (n/e <= k):
                res.append(n/e)
    return res

#@dynamic
def combinations_with_limit(divs, r, limit):
    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    pool = tuple(divs)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        for i in range(r, 0, -1):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        if functools.reduce(lambda x, a: x*a, (pool[i] for i in indices)) == limit:
            yield tuple(pool[i] for i in indices)

@dynamic
def dyn_combinations(n, r):
    return itertools.combinations_with_replacement(n, r)


def is_product_sum(n, k):
    div = divisors(n, k+1)
    #print("n", n, "div", div)

    for j in range(2, k+1):
        if (len(div) < j):
            break
        #cs = combinations_with_limit(div, j, n)
        cs = dyn_combinations(div, j)
        #print("j cs", j, list(cs))
        for comb in cs:
            s = sum(comb)
            # print("comb j s k", comb, j, s, k)
            #if s + k-j == n and functools.reduce(lambda x, a: x*a, comb) == n:
            if s + k-j - functools.reduce(lambda x, a: x*a, comb) == 0:
            #if s + k-j == n:
                #print(n, div, comb, k, j)
                return True
    return False


def smallest_product_sum(k):
    k = 2
    for e in range(4, 30):
        #
        pass


if __name__ == "__main__":

    t1 = time.perf_counter()

    TEST_BREAK = 100

    k = 2
    n = 4

    test_res = [0, 0, 4, 6, 8, 8, 12, 12, 12, 15, 16, 16, 16, 18, 20, 24, 24, 24, 24, 24, 28, 27, 32, 30, 48, 32]

    while k <= len(test_res)  and n < TEST_BREAK:
        while n < TEST_BREAK:
            if is_product_sum(n, k):
                print("===k:", k, "; n:", n, "; divsize", len(divisors(n, k+1)))
                n = min(k,n)
                print("new n", n)#, "test n", test_res[n])
                k += 1
            else:
                #print("nope ->", n, "; divsize", len(divisors(n)))
                n += 1

    print("Done under", time.perf_counter() - t1, "seconds")
