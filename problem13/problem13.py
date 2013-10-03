# /usr/bin/python


def nToList (PATH, n) :
	
	data_f = open(PATH, 'r')
	data_l = data_f.readlines()

	result = []
	
	for t in data_l :
		result.append(int(t)/10**(50-n))

	return result


def sumNNumber (PATH , n) :
	
	result = 0
	i = 5
	while len(str(result)) < n+5 :
		result = 0
		tab = nToList(PATH, i)
		for k in tab :
			result += k
		i += 1

	return result / 10**5

if __name__ == "__main__" :

	PATH = "problem13_data"
	n =  10
	poza = sumNNumber(PATH, 10)
	print poza
