
import time
from functions import *

def to_list (PATH) :
    a = []

    #We read the file data_f and put it on a matrix
    #first: use readline fct to split lines of data_f
    #Then split numbers separate by " " (whitespace)

    data_f =  open(PATH, 'r')
    #data_s = data_f.read()
    #print data_s
    data_l = data_f.readlines()

    for l in data_l :
        a.append(l.split(" "))

    data_f.close()

    #transform a list of string
    #into a list of int
    tab = []
    i = 0
    j = 0
    while i < 20 :
        tab.append([])
        while j < 20 :
            tab[i].append(int(a[i][j]))
            j+=1
        j = 0
        i += 1

    return tab

# test function
def maxProduct (tab) :
	return max(hori_right(tab), (hori_left(tab)), (vert_up(tab)), (vert_down(tab)), (diag_up_left(tab)), (diag_up_right(tab)), (diag_down_right(tab)), (diag_down_left(tab)))



if __name__ == "__main__" :

    t1 = time.clock()       

    PATH = "problem11_data.txt"

    data = to_list(PATH)

    final = maxProduct(data)
    print(final)
    print(time.clock() - t1, "seconds")
