
import time


# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows
# bn              cn
#   21 22 23 24 25
#   20  7  8  9 10
#   19  6  1  2 11
#   18  5  4  3 12
# an              dn
# We can empirically find that the diagonals follows arithmetic progressions
#
# an = (2*n)^2 + 1
# bn = (2*n)^2 + 2*n + 1
# cn = (2*n + 1)^2
# dn = (2*n + 1)^2 - 6*n
#

def an(n):
    res = []
    i = 1
    while i <= n:
        res.append((2*i)**2 + 1)
        i += 1
#   print res
    return res


def bn(n):
    res = []
    i = 1
    while i <= n:
        res.append((2*i)**2 + 2*i + 1)
        i += 1
#   print res
    return res


def cn(n):
    res = []
    i = 1
    while i <= n:
        res.append((2*i + 1)**2)
        i += 1
#   print res
    return res


def dn(n):
    res = []
    i = 1
    while i <= n:
        res.append((2*i + 1)**2 - 6*i)
        i += 1
#   print res
    return res


def sumoffour(sz):
    n = sz/2
    return sum(an(n)) + sum(bn(n)) + sum(cn(n)) + sum(dn(n)) + 1


if __name__ == "__main__":
    t1 = time.clock()

    n = 1001

#   print sumoffour(n)
    print "The sum of the numbers on the diagonals in a", n, " by", n, "spiral formed in the way described above is :", sumoffour(n)
    print "Completed in", time.clock()-t1, "seconds"