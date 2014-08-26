#!/usr/bin/env/python


PATH = "problem18_data.txt"

def data_cfg (PATH):

	data_f = open(PATH, 'r')
	a = data_f.readlines()

	tab = []
	for l in a :
		tab.append(l.split(" "))
  	#print tab
	data_f.close()

	res = []
	i = 0
	for l in tab :
		res.append([])
		for e in l :
			res[i].append(int(e))
		i+=1

	#for l in res :
	#	print l

	return res


def reduceALine (l) :
	res = []

	i = 0

	while i < len(l)-1 :
		try :
			res.append(max(l[i], l[i+1]))
		except IndexError :
			print "pwoblem cap'tain"
		i+=1
	return res


def sumTwoLines(l1, l2) :
	res = []
	i = 0

	a = reduceALine(l1)

	while i < len(l2) :
		try :
			res.append(a[i] + l2[i])
		except IndexError :
			print "pwoblem cap'tain"
			break
		i += 1
	return res


def searchAndSum (mat) :
	"""
	partir du bas de la matrice
	sommer avec l'accessible le plus grand
	"""

	b = mat[-1]
	i = len(mat) -1

	while i > 0 :
		b = sumTwoLines(b, mat[i-1])
		#print b, i
		i-=1
	return b


if __name__ == "__main__" :


	mat = data_cfg(PATH)

	#print mat[-1], len(mat[-1])
	#b =  reduceALine(mat[-1])
	#print b, len(b)
	#c = sumTwoLines(b, mat[-2])
	#print c
	#print francis(mat)

	print searchAndSum(mat)

