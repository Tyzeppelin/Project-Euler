import time

# TODO : Regarder la fin du tp6 d'ocaml. Il y a un algo de partition


def insert(l, c):
#   print l, c
    if l == [[]] or l is None:
        return [c]
    arr = l
    for e in arr:
        e.append(c)
    return arr

# A modifier pour prendre en compte les valeurs de `currency`
def part(n, k):
    if n == 0 and k == 0:
        return case1()
    elif k == 0:
        return case2()
    elif k > n:
        return case3(n)
    else:
        n = case4(n-k, k)
        m = case4(n, k-1)
        return insert(n, k).append(m)


def case1():
    return [[]]

def case2():
    return []

def case3(n):
    return part(n, n)

def case4(k, n):
    if k == 0 and n == 0:
        return case1()
    elif k ==0:
        return case2()
    elif k > n:
        return case3(n)
    else:
        return part(k, n)



if __name__ == "__main__":
    t1 = time.clock()

    currency = [1, 2, 5, 10, 20, 50, 100, 200]

    a = [[], [1], [2,3,4]]
    print insert(a, 4)

    print part(5, 5)

    print "Completed in", time.clock()-t1, "seconds"
