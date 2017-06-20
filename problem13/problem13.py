
import time

# transform a file into an array of the first
# n digits of each line
def nToList (PATH, n) :

    data_f = open(PATH, 'r')
    data_l = data_f.readlines()
    result = []
    for t in data_l :
        result.append(int(t)/10**(50-n))
    return result

# sum the first n digits of each lines of a file
# named PATH
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

    t1 = time.clock()

    PATH = "problem13_data.txt"
    # I chose to take the first 10 numbers of
    # each lines to make sure that i take the first
    # 10 numbers of the sum of each lines
    n =  10
    poza = sumNNumber(PATH, 10)

    print(poza)
    print(time.clock() - t1, "seconds")

