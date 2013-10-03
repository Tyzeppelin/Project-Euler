#! /usr/bin/python

from math import *

LARGE_NUMBER = 600851475143


def isPrime (n) :
	
	k = int(sqrt(n))
	res = True
	while k > 3 :
		if n%k == 0 :
			res = False
			break
		k -= 1 
	return res


if __name__ == "__main__" :

	i = int(sqrt(LARGE_NUMBER))

	while i > 2 :
		if (LARGE_NUMBER%i == 0) and isPrime(i) :
			break
		i -= 1 
	print i
