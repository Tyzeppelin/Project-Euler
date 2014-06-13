
import time

# Because there was many primes a long ago, and Optimus is the last of them.
OPTIMUS = [2]


def isprime(n):
    if n < 0:
#       print "OMG"
        return False
    expand(n)
    if n in OPTIMUS:
        return True
    else:
        return False


def expand(n):
    i = OPTIMUS[-1]
    b = True
    while i <= n:
        for prime in OPTIMUS:
            if i % prime == 0:
                b = False
                break
        if b:
            OPTIMUS.append(i)
        b = True
        i += 1


# The number of prime you can get with the formula
def autobots(a, b):
    i = 0
    while isprime(i**2 + a*i + b):
        i+=1
    return i-1


def autobotsinrange(amin, amax, bmin, bmax):
    i = amin
    res = 0
    couple = (0,0)

    while i <= amax:
        j = bmin
        while j < bmax:
            tmp = autobots(i, j)
            if tmp > res:
                res = max(res, tmp)
                couple = (i,j)
            j += 1
        i += 1
    return couple

if __name__ == "__main__":

    t1 = time.clock()

    amin = -1000
    amax = 1000

    bmin = -1000
    bmax = 1000

    res = autobotsinrange(amin, amax, bmin, bmax)

    print "The biggest couple (a,b) that gives the most number of consecutive prime from the formula n^2 + a*b + b, for n in N is :(%d,%d)." % res

    print "Completed in", time.clock()-t1, "seconds"