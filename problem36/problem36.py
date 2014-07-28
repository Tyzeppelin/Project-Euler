
import time

def isPalindromic(n):
    if len(n)%2 == 0:
        return n[:len(n)/2] == n[len(n)/2:][::-1]
    else :
        return n[:len(n)/2] == n[len(n)/2+1:][::-1]

def condition(n):
    base10 = str(n)
    base2  = '{0:b}'.format(n)
    return isPalindromic(base10) and isPalindromic(base2)

if __name__ == "__main__":

    t1 = time.clock()

    s = 0
    for e in range(1000000):
        if condition(e):
            s += e
    print """The sum of all "double-base palindrome" below one million is ->""", s
    print "The magic operate under", time.clock()-t1, "seconds"
