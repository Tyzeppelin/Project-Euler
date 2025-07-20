#import math
import gmpy2 
import time


# (n + 1) * sqrt((n - 1)(3n + 1)) / 4
# generate n so that (n-1)(3n+1) = t², t ∈ ℤ
def sqrt_positive():
    sqrt3 = gmpy2.sqrt(3)
    for mp in range(1, 10):
         yield gmpy2.mpz(((7 - 4*sqrt3)**mp + (7 + 4*sqrt3)**mp + 1) / 3)

# (n - 1) * sqrt((n + 1)(3n - 1)) / 4
# generate n so that (n+1)(3n-1) = t², t ∈ ℤ
def sqrt_negative():
    sqrt3 = gmpy2.sqrt(3)
    for mn in range(2, 10):
        yield gmpy2.mpz((2*(7 - 4*sqrt3)**mn + sqrt3*(7-4*sqrt3)**mn + 2*(7+4*sqrt3)**mn - sqrt3*(7+4*sqrt3)**mn - 1) / 3)


# Too slow for the solution
# Good for testing purposes though
#def gen_squares(max_N=100000000):
#    for n in range(3, max_N, 2):
#        pos = (n-1)*(3*n+1)
#        neg = (n+1)*(3*n-1)
#        yield (n, pos if gmpy2.is_square(pos) else -1, neg if gmpy2.is_square(neg) else -1)

if __name__ == "__main__":

    t1 = time.time()

    MAX_PERIM = 10**9

    pos = set()
    neg = set()

    for np in sqrt_positive():
        if 3*np+1 > MAX_PERIM:
            break
        pos.add(np)

    for nn in sqrt_negative():
        if 3*nn-1 > MAX_PERIM:
            break
        neg.add(nn)

    print([gmpy2.digits(e) for e in sorted(pos)], sum([3*n+1 for n in pos]))
    print([gmpy2.digits(e) for e in sorted(neg)], sum([3*n-1 for n in neg]))
    print("=>", sum([3*n+1 for n in pos]) + sum([3*n-1 for n in neg]))

    # For testing/checking results
#    ref_pos = set()
#    ref_neg = set()
#    print("\n\nsolution")
#    for n, pos, neg in gen_squares():
        # should be divisible by 16 ?
#        if pos > 0:
#            num = gmpy2.mul((n+1), gmpy2.isqrt(pos))
#            ref_pos.add(n)
        # should be divisible by 4 ?
#        if neg > 0:
#            num = gmpy2.mul((n-1), gmpy2.isqrt(neg))
#            ref_neg.add(n)
#    print(sorted(ref_pos))
#    print(sorted(ref_neg))
    
    print("done under", time.time() - t1, "sconds.")
