import time
from functools import cache
from collections import defaultdict



def extract_chain(chain, m):
    idx = chain.index(m)
    return chain[idx:], chain[:idx]


# I kept this as a reminder
# And because I liked this method
table = dict({1:1})
@cache
def sigma_1(n):
    """
    very inefficient
    """
    if n == 1:
        return 1
    acc = 0
    for i in range(1, n+1):
        s = (-1)**(i+1)
        t_1 = int(n - (3*i**2-i)/2)
        if t_1 < 0:
            s_t_1 = 0
        elif t_1 == 0:
            s_t_1 = n
        else:
            s_t_1 = table[t_1]
        t_2 = int(n - (3*i**2+i)/2)
        if t_2 < 0:
            s_t_2 = 0
        elif t_2 == 0:
            s_t_2 = n
        else:
            s_t_2 = table[t_2]
        acc += s * (s_t_1 + s_t_2)
    #print("n=",n, "sigma=", acc)
    table[n] = acc
    return acc


# I should have thought about this myself...
# I am getting old and dumb...
def gen_div_sums(max_n=1000000):
    div_sum = defaultdict(lambda: 1)

    for n in range(2, max_n+1//2):
        for i in range(n*2, max_n+1, n):
            div_sum[i] += n
    return div_sum

if __name__ == "__main__":
    
    t1 = time.time()

    part_of = set()
    excluded = set([1])
    chains = []

    max_chain = []
    max_N = 1000000
    div_sums = gen_div_sums(max_N)


    i_t = 0
    for n in range(2, max_N):
        if n in excluded or n in part_of:
            continue
        if div_sums[n] == n:
            excluded.add(n)
            continue
        chain = [n]
        m = n
        while m > 1 and m < max_N and (m not in excluded and m not in part_of):
            i_t += 1
            m = div_sums[m]
            if m in chain:
                amical_chain, other = extract_chain(chain, m)
                #print("found chain ->", amical_chain, other)
                part_of.update(amical_chain)
                excluded.update(other)
                if len(amical_chain) > len(max_chain):
                    max_chain = amical_chain
                chains.append(amical_chain)
                break
            chain.append(m)
        else:
            excluded.update(chain)
    

    print("iterations:", i_t)
    print("max_chain", max_chain, "(", div_sums[max_chain[-1]], ")")
    print("len", len(max_chain))
    print("done under", time.time() - t1, "seconds.")
