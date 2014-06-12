#! /usr/bin/python



def isMultipleOf3Or5 (n):
	if n%3 == 0 or n%5 == 0 :
		return True
	else :
		return False



if __name__ == "__main__" :

	i = 3
	sumOfMultiple = 0

	while i < 1000 :
		if isMultipleOf3Or5(i) :
			sumOfMultiple += i
		
		i+=1

	print sumOfMultiple,' yolo'
