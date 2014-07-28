


def tailFacto(n, r):
    if n == 0:
        return r
    else :
        return tailFacto(n-1, r*n)


def factorial (n):
    if n == -1:
        return 0
    return tailFacto(n, 1)

def cond (a):
    num = int(''.join(map(str,a)))
    res = 0
    for e in a:
        res += factorial(e)
    return num == res

def formula (l):
    l.reverse()
    exp = 0
    res = 0
    for e in l:
        res += (10**exp)*e
        exp += 1

if __name__ == "__main__":

    #print factorial(500)

    a = 0
    b = 0
    c = 0
    d = 1

    res = 0

    # for e in range -> split -> factorial -> bam

    # I iterate only until 100000.
    for e in range (100000):
        num = [int(i) for i in str(e)]
        if cond(num):
            print 'yata -> ', e
            res += e

print res
