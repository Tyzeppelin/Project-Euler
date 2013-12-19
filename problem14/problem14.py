#!/usr/bin/env/python

from math import *
import time

def suite (u0) :
	
	u = u0

	comp = 0
	while u != 1 :
		if u%2 == 0 :
			u = u/2
		else :
			u = 3*u+1
		comp += 1
	return comp


def nbEven (u0) :
	u = u0

	comp = 1 

	while u%2 != 0 :
		comp +=1
		u  = 3*u+1
	return comp



def longestCollatz (n) :
	
	a = (1, 1, 1) #de type (u0, nb de nombres impairs, nombre de termes)
	
	i = n/2 
	while i < n :
		w = nbEven(i)
		#print w
		if(nbEven(i) >= a[1]) :
			j = suite(i)
			#print j, k
			if(j > a[2] ) :
				a = (i, w, j)
		i+=1
	return a




if __name__ == "__main__" :
	print 'coucou'
	t1 = time.clock()
	b =  longestCollatz(1000000)
	t2 = time.clock()
	print b, ", exec under", t2-t1, "seconds"
