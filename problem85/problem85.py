
import time

from math import inf,sqrt

if __name__ == "__main__":

    t1 = time.perf_counter()

    target = 2000000

    nb_rect_line = lambda n: n*(n+1)/2

    distance = inf
    surface = 0

    for i in range(int(sqrt(target)))[1:]:
        for j in range(int(sqrt(target)))[1:]:
            n = nb_rect_line(i)
            m = nb_rect_line(j)
            if n*m > target:
                break
            if target - n*m < distance:
                distance = target - n*m
                surface = i*j
                #print(i, j, n, m, n*m, distance)

    print(surface)
    print(time.perf_counter() - t1, "seconds")
