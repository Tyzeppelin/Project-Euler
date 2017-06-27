#!/usr/bin/python


alphabet = ['"', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
PATH = "problem22_data.txt"

def toListSorted (PATH) :

	data_f = open(PATH, 'r')
	data_l = data_f.read()
	data_f.close()

	foo = data_l.split('","')
	foo[0] = (foo[0].split('"'))[1]
	foo.sort()
	return foo



def valueOfAName (name) :
	n = name.lower()
	res = 0
	for e in n :
		#print e
		res += alphabet.index(e)
	return res


def valueOfAList (l) :
	res_l = []
	res_i = 0
	for e in l :
		res_l.append(valueOfAName(e))
	i = 1
	for e in res_l :
		res_i += e*i
		i+=1
	return res_i



if  __name__ == "__main__" :

	a = toListSorted(PATH)
	b = valueOfAList(a)
	print(b)
