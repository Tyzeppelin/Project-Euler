
import math
import time


# not my standard generation. Tried a new thing (it's probably not good)
def primes_under(n):
    res = [2, 3]
    j = 1
    b = False
    for e in range(5, n, 2):
        if len([a for a in res[:j] if e%a == 0]) == 0:
            res.append(e)
            b = not b
            if b:
                j += 1
    return res

def power_of_primes(primes, limit=100):

    p2, p3, p4 = ([], [], [])

    for p in primes:
        if p**2 < limit:
            p2.append(p**2)
        else:
            break
        if p**3 < limit:
            p3.append(p**3)
        else:
            continue
        if p**4 < limit:
            p4.append(p**4)
    return p2, p3, p4

def solution(p2, p3, p4, limit=100):

    res = set()
    for e4 in p4:
        for e3 in p3:
            if e3+e4 > limit:
                break
            for e2 in p2:
                if e2+e3+e4 > limit:
                    break
                res.add(e2+e3+e4)

    return len(res)


if __name__ == "__main__":

    t1 = time.clock()

    K = 50000000

    OPTIMUS = primes_under(math.ceil(math.sqrt(K)))
    #print(OPTIMUS)
    print("primes generated", math.ceil(math.sqrt(K)), len(OPTIMUS))

    p2, p3, p4 = power_of_primes(OPTIMUS, limit=K)

    print(solution(p2, p3, p4, limit=K))

    print("Done under", time.clock() - t1, "seconds.")
