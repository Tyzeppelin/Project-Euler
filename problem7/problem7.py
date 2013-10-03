#! /usr/bin/python


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

print j, optimus[-1]

