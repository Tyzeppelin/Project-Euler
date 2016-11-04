#!/usr/bin/python3

from math import log, sqrt

def is_tri(n):
    return (-1+sqrt(1+8*n))/2 % 1 == 0.0

def is_sqr(n):
    return sqrt(n)%1 == 0.0

def is_pen(n):
    return (1+sqrt(1+24*n))/6 % 1 == 0.0

def is_hex(n):
    return (1+sqrt(1+8*n))/4 % 1 == 0.0

def is_hep(n):
    return (3+sqrt(9+40*n))/10 % 1 == 0.0

def is_oct(n):
    return (1+sqrt(1+3*n))/3 %1 == 0.0

if __name__ == "__main__":


