#! /usr/bin/python

from time import *

t1 = clock()

optimus = [2]

b = True
i = 3
j = 1


while j < 10001 :
	b = True
	for e in optimus :
		if i%e == 0 :
			b = False
			break
	if b :
		optimus.append(i)
		j += 1
	i += 1
t2 = clock()

print optimus[-1], 'is the 10001st prime\nExecute in', t2-t1, 'seconds'

