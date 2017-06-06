
import time
import math

if __name__ == "__main__":

    t1 = time.clock()

    #continued fraction of sqrt(2) is 1+(2+1/(2+1/(2+1/(...))))
    frac = (1,1)

    # we can compute numerator and denominator like:
    #  * num(t+1) = 2*den(t) + num(t)
    #  * den(t+1) = num(t) + den(t)

    c = 0
    for _ in range(1000):
        if math.ceil(math.log10(frac[0])) > math.ceil(math.log10(frac[1])):
            c += 1
        frac = (2*frac[1] + frac[0], frac[0] + frac[1])

    print(c)
    print(time.clock() - t1, "seconds")
