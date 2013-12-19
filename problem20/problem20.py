#!/usr/bin/env/python

from math import *

def sumOfDigits (n) :
	
	num = n
	res = 0
	
	length = log10(n)+1
	i = 0
	while i < length :
		res += num%10
		num /= 10
		i += 1
	return res


if __name__ == "__main__" :

	a = factorial(100)
	print a
	print sumOfDigits(a)
	
