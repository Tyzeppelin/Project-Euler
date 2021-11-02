import time

from collections import defaultdict
from math import fabs, inf, sqrt

# The sum of rectangles in an n*m grid σ_n_m
# is given by :
# σ_n_m = σ_n_1 * σ_1_m
# with σ_1_m = σ_n_1 = n * (n+1) / 2

def sigma_n_1(n):
    return n * (n+1) / 2

def sigma_1_m(m):
    return sigma_n_1(m)

def sigma_n_m(n, m):
    return sigma_n_1(n) * sigma_1_m(m)

if __name__ == "__main__":

    t1 = time.time()

    mat = defaultdict(lambda: [])

    target = 2000000
    max_n = int(sqrt(target))

    distance = inf
    closest = 0
    closest_n = 0
    closest_m = 0

    for n in range(1, max_n):
        for m in range(1, max_n):
            sigma = sigma_n_m(n, m)
            if sigma > target + distance:
                break
            if fabs(target - sigma) < distance:
                distance = fabs(target - sigma)
                closest = sigma
                closest_n = n
                closest_m = m

            mat[n].append(sigma_n_m(n, m))


    print("closest to ", target, " is (", closest_n, ", ", closest_m, ") -> ", closest, "; with a distance of ", distance)
    print("the area of the rectangle is -> ", closest_n * closest_m)
    print("done in: ", time.time() - t1, " seconds.")
