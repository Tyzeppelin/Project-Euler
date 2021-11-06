
import collections
import math
import time


def primes(n):
    res = [2, 3]
    j = 2
    b = True
    for e in range(5, n, 2):
        if len([a for a in res[:j] if e%a == 0]) == 0:
            res.append(e)
            j += 1 if b else 0
            b = not b
    return res


def generator(n, ps):

    cache_2 = []
    cache_3 = []
    cache_4 = []
    
    for i in ps:
        a2 = i**2
        a3 = i**3
        a4 = i**4
        if a2 <= n:
            cache_2.append(a2)
        if a3 <= n:
            cache_3.append(a3)
        if a4 <= n:
            cache_4.append(a4)
        i += 1
    return cache_2, cache_3, cache_4


if __name__ == "__main__":


    K = 50000000

    print("Caching every prime under:", math.ceil(math.sqrt(K)), '...')
    t3 = time.clock()
    OPTIMUS = primes(math.ceil(math.sqrt(K)))
    #print(OPTIMUS)
    print("Generated under", "{:.5f}".format(time.clock()-t3), "seconds")

    print("Caching square, third and fourth power of primes under", math.ceil(math.sqrt(K)), "...")
    t2 = time.clock()
    cache_2, cache_3, cache_4 = generator(K, OPTIMUS)
    print("Generated", (len(cache_2), len(cache_3), len(cache_4)), "->", len(cache_2)+len(cache_3)+len(cache_4), "elements under", "{:.5f}".format(time.clock()-t2), "seconds.")

    t1 = time.clock()

    res = set()
    for a2 in cache_4:
        for a3 in cache_3:
            if a2 + a3 > K:
                break
            for a4 in cache_2:
                if a2+a3+a4 <= K:
                    res.add(a2+a3+a4)
                else:
                    break

    #print(len(cache_2)*len(cache_3)*len(cache_4))
    print("->", len(res))
    print("Executed under", time.clock(), "seconds")
