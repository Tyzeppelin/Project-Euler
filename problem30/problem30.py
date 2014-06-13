
import time

# I used a empiric method. I test if every numbers below 9 999 999
# can be written as the sum of fifth powers of their digits

POWA = 5


def sumofdigit(n):
    a = n
    som = 0
    while a > 0:
        som += (a % 10)**POWA
        a /= 10
    return som


# Cause Magus got the power of black magic.
# Chrono TriggerSymphony is awesome. Real.
def magus(m):
    i = 2
    res = []
    while i < m:
        if sumofdigit(i) == i:
            res.append(i)
        i += 1
    return res

if __name__ == "__main__":
    t1 = time.clock()

#   print magus(9999999)
#   -> [4150, 4151, 54748, 92727, 93084, 194979]

    print "The sum of all the numbers that can be written as the sum of fifth powers of their digits is:", sum(magus(9999999))

    print "Completed in", time.clock()-t1, "seconds"