
import time

def reverse(n):
    return int(''.join(reversed([a for a in str(n)])))

def is_lychrel(n):
    i = 0
    while i < 50:
        n += reverse(n)
        if n == reverse(n):
            return False 
        i+=1
    return True

if __name__ == "__main__":

    t1 = time.clock()

    c = 0
    for x in range(0,10000):
        if is_lychrel(x):
            c += 1

    print(c)
    print(time.clock() - t1, "seconds")
