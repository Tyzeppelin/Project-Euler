#!/usr/bin/env

from math import *


NUMBERS  = []
DIVISORS = []


def divisors (n) :
	i = 1
	tab = []
	while i < sqrt(n) :
		if n%i == 0 :
			tab.append(i)
			tab.append(n/i)
		i+=1
	return tab


def sumOfDivisors (n) :
	t = divisors(n)
	NUMBERS.append(n)
	DIVISORS.append(sum(t)-n)
	return sum(t) - n


def isFriendly (n, m) :
	
	if n > m :
		return False

	try :
		a = NUMBERS.index(m)
	except ValueError :
		sumOfDivisors(m)
		a = NUMBERS.index(m)
	if DIVISORS[a] == n and DIVISORS[a] !=m :
		return True
	else :
		return False


def FriendlyNumbers (n) :
	Friendly = []	
	i = 2

	while i < n :

		if isFriendly(i, sumOfDivisors(i)) and i < sumOfDivisors(n) :
			Friendly.append((i, sumOfDivisors(i)))
			print "<3", Friendly
		#print i, Friendly, NUMBERS, DIVISORS
		i+=1
	return Friendly 

def sumOfFriends (FriendList) :
	res = 0
	for guest in FriendList :
		res += guest[0]+guest[1]
	return res



if __name__ == "__main__" :
	
	#print sumOfDivisors(220)
	
	n = 10000
	res = FriendlyNumbers(n)
	
	print res
	print sumOfFriends(res)


