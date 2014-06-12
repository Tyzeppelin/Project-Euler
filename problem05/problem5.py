#!/usr/bin/python

##########################
###### Written by ########
##### Tyzeppelin #########
##########################

n = 1000
print(n)

def test (n) :
	if (n%2 == 0) and (n%3 == 0) and (n%5 == 0) and (n%7 == 0) and (n%9 == 0) and (n%11 == 0) and (n%13 == 0) and (n%15 == 0) and (n%16 == 0) and (n%17 == 0) and (n%18 == 0) and (n%19 == 0) and (n%20 == 0):
		return True 
	return False


while not test(n) :
	n += 1

print(n)
