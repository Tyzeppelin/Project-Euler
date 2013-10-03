#!/usr/bin/python

# Designed by a unicorn

sumOfSquare =  0
squareOfSum = 0


for i in range(101) :
	squareOfSum += i
squareOfSum = pow(squareOfSum, 2)

for i in range(101) :
	sumOfSquare += (pow(i, 2))

result = squareOfSum - sumOfSquare
print(result)
