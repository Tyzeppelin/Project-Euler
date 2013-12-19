#!/usr/bin/env/python


# Formalism 
# 
# Days (int in List): 
# 1->Monday/Mon; 2->Tuesday/Tue ; 3->Wednesday/Wed; 4->Thursday/Thu; 
# 5->Friday/Fri; 6->Saturday/Sat; 7->Sunday/Sun
#
# Months (index in List):
# 0->January/Jan  ; 1->February/Feb; 2->March/Mar    ; 3->April/Apr    ;  
# 4->May/May      ; 5->June/Jun    ; 6->July/Jul     ; 7->August/Aug   ; 
# 8->September/Sep; 9->October/Oct ; 10->Novelber/Nov; 11->December/Dec;
#
#


Y1901 = [2, 5, 5, 1, 3, 6, 1, 4, 7, 2, 5, 7]

Y1902 = [3, 6, 6, 2, 4, 7, 2, 5, 1, 3, 6, 1]

Y1903 = [4, 7, 7, 3, 5, 1, 3, 6, 2, 4, 7, 2]

Y1904 = [5, 1, 2, 5, 7, 3, 5, 1, 4, 6, 2, 4]

Y1905 = [7, 3, 3, 6, 1, 4, 6, 2, 5, 7, 3, 5]





def HappyNewYear (year) :

	nextYear = []
	
	for e in year :
		if e+1 == 7 :
			nextYear.append(e+1)
		else :
			nextYear.append((e+1)%7)
	return nextYear



def HappyNewLeapYear (year) :
	
	nextYear = []
	i = 0
	while i < 2 :
		e = year[i]
		if e+1 == 7 :
			nextYear.append(e+1)
		else :
			nextYear.append((e+1)%7)
		i+=1
	while i < len(year) :
		e = year[i]
		if e+2 == 7 :
			nextYear.append(e+2)
		else :
			nextYear.append((e+2)%7)
		i+=1
	return nextYear

def HappyNewYearNextLeap (year) :
	
	nextYear = []
	i = 0
	while i < 2 :
		e = year[i]
		if e+2 == 7 :
			nextYear.append(e+2)
		else :
			nextYear.append((e+2)%7)
		i+=1
	while i < len(year) :
		e = year[i]
		if e+1 == 7 :
			nextYear.append(e+1)
		else :
			nextYear.append((e+1)%7)
		i+=1
	return nextYear
	

		

def howMuch (day, toY) :
	"""
	day as an int from 1 to 7
	toY as an int from 1901 to n
	"""

	res = 0 
	year = Y1901

	i = 1902
	

	nextLeap = False

	print i-1, year, nextLeap, res

	while i <= toY :
		
		res += year.count(day)
		if (i%4 == 0 and i%100 !=0)or i%400  == 0 :
			year = HappyNewLeapYear(year)	
			nextLeap = True
		elif nextLeap :
			year = HappyNewYearNextLeap(year)
			nextLeap = False
		else :
			year = HappyNewYear(year)
		print i, year, nextLeap, res
		i+=1
	
	return res + year.count(day)
	


if __name__ == "__main__" :
	
	#Y1 = HappyNewYear(Y1901)
	#Y2 = HappyNewLeapYear(Y1903)
	#Y3 = HappyNewYearNextLeap(Y1904)

	#print Y1901, "\n", Y1, "\n", Y1902, Y1902 == Y1,"\n--------"
	#print Y1903, "\n", Y2, "\n", Y1904, Y1904 == Y2,"\n--------"
	#print Y1904, "\n", Y3, "\n", Y1905, Y1905 == Y3,"\n--------"

	a = howMuch(7, 2000)
	print a

