
import time


if __name__ == "__main__":
    t1 = time.clock()

    amin = 2
    amax = 100

    bmin = 2
    bmax = 100

    i = amin
    res = []

    while i <= amax:
        j = bmin
        while j <= bmax:
            if not i**j in res:
                res.append(i**j)
            j += 1
        i += 1

#   res.sort()
#   print res

    print "The number of distincts terms int the sequence geenrated by a^b for 2 <= a <= 100 and 2 <= b <= 100 is:", len(res)

    print "Completed in", time.clock()-t1, "seconds"