#!/usr/bin/python

import time
from math import *

ALLDAPOWA = {}


class pandigital:
    """
    Class that create and
    the pandigital triplets
    """


    def __init__(self, a = 2, b = 2):
        self.op1 = a
        self.op2 = b
        self.res = self.op1 * self.op2
        self.sum = self.op1 + self.op2 + self.res


    def get_op1(self):
        return self.op1
    def set_op1(self, op):
        self.op1 = op
        self.set_res()
        self.set_sum()

    def get_op2(self):
        return self.op2
    def set_op2(self, op):
        self.op2 = op
        self.set_res()
        self.set_sum()

    def get_res(self):
        return self.res
    def set_res(self):
        self.res = self.op1 * self.op2
        self.set_sum()

    def get_sum(self):
        return self.sum
    def set_sum(self):
        self.sum = self.op1+self.op2+self.res

    # Ugly way.
    def isPandigital(self):
        s = str(self.op1)+str(self.op2)+str(self.res)
        b = list(s)
        b.sort()
        return b == ['1','2','3','4','5','6','7','8','9']

    def add (self):
 #       print self.get_sum(), ALLDAPOWA.keys() ,self.get_sum() not in ALLDAPOWA
        if self.get_sum() not in ALLDAPOWA:
            ALLDAPOWA[self.get_sum()] = self
            #print ALLDAPOWA
            return True
        else :
            return False

    def equal(self, pan):
        if type(pan) is int:
            return True
        else:
            return self.get_sum() == pan.get_sum()



def next(pandig):
    a = pandig.get_op1()
    b = pandig.get_op2()
    res = pandigital(a, b)
    booh = False
    while not booh:
        res.set_op1(a+1)
        a+=1
        while not res.isPandigital():
            if log10(a) > 3 :
                if log10(a)+log10(b) > 5:
                    print "No more."
                    return -1
                else:
                    b += 1
                    a = 2
            else:
                a += 1
            #print a, "*", b, "=", a*b
            res.set_op1(a)
            res.set_op2(b)
        booh = res.add()
#        print "new?", res.get_sum(), "in", ALLDAPOWA, booh, "\n"
    return res

def sumOfAll():
    res = 0
    for e in ALLDAPOWA:
        res += e
    return res

if __name__ == "__main__":

    t1 = time.clock()

    pan = pandigital()
    next_pan = next(pan)

    while not pan.equal(next_pan):
        pan = next_pan
        next_pan = next(next_pan)
        #print next_pan.get_op1(), "*", next_pan.get_op2(), "=", next_pan.get_res()

#print ALLDAPOWA

print sumOfAll()

print "exec in", time.clock()-t1, "seconds"

