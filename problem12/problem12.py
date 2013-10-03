#!/usr/bin/python

from math import *

def triang (n) :
	return n*(n+1)/2

# a list of all the divisors of n
def divisors (n) :
	i = 1
	tab = []
	while i < sqrt(n) :
		if n % i == 0 :
			tab.append(i)
			tab.append(n/i)
		i+=1
	return tab







if __name__ == "__main__" :

	#for i in range(100) :
	
	i = 2
	a = []
	while len(divisors(triang(i))) <= 500 :
		i += 1
	print triang(i)

