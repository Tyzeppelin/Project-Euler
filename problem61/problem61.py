#!/usr/bin/python3

from math import ceil, log, log10, sqrt

def tria(n):
    return n*(n + 1)/2
def is_tri(n):
    return (-1+sqrt(1+8*n))/2 % 1 == 0.0

def squa(n):
    return n**2
def is_sqr(n):
    return sqrt(n)%1 == 0.0

def pent(n):
    return n*(3*n - 1)/2
def is_pen(n):
    return (1+sqrt(1+24*n))/6 % 1 == 0.0

def hexa(n):
    return n*(2*n - 1)
def is_hex(n):
    return (1+sqrt(1+8*n))/4 % 1 == 0.0

def hept(n):
    return n*(5*n - 3)/2
def is_hep(n):
    return (3+sqrt(9+40*n))/10 % 1 == 0.0

def octo(n):
    return n*(3*n - 2)
def is_oct(n):
    return (1+sqrt(1+3*n))/3 %1 == 0.0

if __name__ == "__main__":

    o = [n for n in [octo(i) for i in range(1,200)] if ceil(log10(n)) == 4]
    h = [n for n in [hept(i) for i in range(1,200)] if ceil(log10(n)) == 4]
    x = [n for n in [hexa(i) for i in range(1,200)] if ceil(log10(n)) == 4]
    p = [n for n in [pent(i) for i in range(1,200)] if ceil(log10(n)) == 4]
    s = [n for n in [squa(i) for i in range(1,200)] if ceil(log10(n)) == 4]
    t = [n for n in [tria(i) for i in range(1,200)] if ceil(log10(n)) == 4]
    print(o, h, x, p, s, t)

    
