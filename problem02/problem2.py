
import time

if __name__ == "__main__" :

    t1 = time.clock()

    res = 0

    F  = 1
    F1 = 1
    F2 = 1 

    while F2 < 4000000 :
        F2 = F+F1
	if F2%2 == 0 :
	    res += F2
	F = F1
	F1 = F2

    print(res)
    print(time.clock() - t1, "seconds")
