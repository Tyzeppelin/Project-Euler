
import time


def e_continued_fraction(n=100):
    yield 2
    for i in range(1,100/3+1):
        yield 1
        yield 2*i
        yield 1

if __name__ == "__main__":

    t1 = time.clock()

    r = []
    acc = []
    i = 0
    for e in e_continued_fraction(100):
        acc.append(e)
        num = acc[-1]
        den = 1
        for a in reversed(acc[:-1]):
            old_num = num
            num = a*num + den
            den = old_num
        r.append(sum(map(int, str(num))))   
        i+=1
    print(i, r[-1])

    print(time.clock()-t1, "seconds")
