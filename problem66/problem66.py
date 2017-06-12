
import math
import time

from math import sqrt, floor

def gen_continued_fraction(n, k=10):
    a0 = int(sqrt(n))
    num = -a0
    den = 1 
    ak = [a0]
    #print(ak, num, den)

    for _ in range(k):
        an = int(den/(sqrt(n)+num))
        den = (n - num ** 2) / den
        num = - num - an * den

        ak.append(an)
        #print(ak, num, den)
    return ak 

def non_squared_generator(n):
    for n in range(2, n+1): 
        if sqrt(n) % 1.0 != 0.0:
            yield n

# solve pell equation
# http://mathworld.wolfram.com/PellEquation.html
#
def solve_quadratic_diophantine(D):
    ak = gen_continued_fraction(D, 1000)
    p = [ak[0]]
    q = [1]
    # p0, q0 -> even -> so return p1, q1
    if p[-1]**2 - D * q[-1]**2 == 1:
        return ak[0]*ak[1]+1, ak[1]
    p.append(ak[0]*ak[1] + 1)
    q.append(ak[1])

    i = 1
    while p[-1]**2 -D * q[-1]**2 != 1 :
        i+=1
        p.append(ak[i]*p[-1] + p[-2])
        q.append(ak[i]*q[-1] + q[-2])
    if i %2 == 1:
        return p[-1], q[-1]
    for _ in range(i+1):
        i += 1 
        p.append(ak[i]*p[-1] + p[-2])
        q.append(ak[i]*q[-1] + q[-2])
    return p[-1], q[-1]

if __name__ == "__main__":

    t1 = time.clock()

    max_p_q = (0,0)
    max_D = 0
    for D in non_squared_generator(1000):
        #print(D, "-", solve_quadratic_diophantine(D))
        p,q = solve_quadratic_diophantine(D)
        if p > max_p_q[0]:
            max_p_q = (p,q)
            max_D = D
    print(max_D, max_p_q)
    print(time.clock() - t1, "seconds")
