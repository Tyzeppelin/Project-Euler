#!/usr/bin/python

from math import *
from time import *

# create a list of all prime number minor than n
def genere (n) :

	primeArray = [2]	
	i = 3
	while  i < n :
		if div(i, primeArray) :
			primeArray.append(i)
			#print "add ", i
		i += 1
	print(primeArray)
	return primeArray


# return True if n is divisible by any elements
# in tab
def div (n, tab) :
	i = 0
	while i < sqrt(len(tab)) :
		if n % tab[i] == 0 :
			return False
		i += 1
	return True


# generate the sum of the prime minor than n
def sumOfPrime (n) :
	
	sum = 0

	tab = genere(n)
	for i in tab:
		sum += i

	print sum


if __name__ == "__main__" :

	#print sum(genere(2000000))

	t1 = clock()

	sumOfPrime(2000000) # ^ same ^
	
	t2 = clock()
	print "Execute in", t2-t1, "seconds."
