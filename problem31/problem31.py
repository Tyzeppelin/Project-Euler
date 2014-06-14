import time

# TODO : Regarder la fin du tp6 d'ocaml. Il y a un algo de partition


def insert(l, c):
#   print l, c
    if l == [[]] or l is None:
        return l
    arr = l
    for e in arr:
        e.append(c)
    return arr

# A modifier pour prendre en compte les valeurs de `currency`
#def part(n, k):
#    if n == 0 and k == 0:
#        return [[]]
#    elif k == 0:
#        return []
#    elif k > n:
#        return part(n, n)
#    else:
#        return insert(part(n-k, k), k).append(part(n, k-1))


if __name__ == "__main__":
    t1 = time.clock()

    #currency = [1, 2, 5, 10, 20, 50, 100, 200]

    a = [[], [1], [2,3,4]]
    print insert(a, 4)

    # print part(5, 5)

    print "Completed in", time.clock()-t1, "seconds"