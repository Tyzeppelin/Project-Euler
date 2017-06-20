
import time

digits  = (0, 3, 3, 5, 4, 4, 3, 5, 5, 4)
tenth   = (0, 0, 6, 6, 5, 5, 5, 7, 6, 6) 
hundred = (0, 10, 10, 12, 11, 11, 10, 12, 12, 11) 
excep   = (3, 6, 6, 8, 8, 7, 7, 9, 8, 8)


def myModulo (a, b) :
    if (a < b) : return 0
    else : return a%b


def nb_letters (n) :
    if n%100/10 == 1 :
	if n/100 >0 :
	    result = hundred[n/100]+3+excep[n%10]
	else :
	    result = hundred[n/100] + excep[n%10]
	#print "passage 1"
    elif n%100 == 0 :
	result = hundred[n/100]
	#print "passage 2"
    else :
	if n/100>0 :
	    result = hundred[n/100] + tenth[n%100/10] + digits[n%10] + 3
	    print "passage 3-1"
	else :
	    result = tenth[n%100/10] + digits[n%10]
	    print "passage 3-2"
    return result


def watchTower (n) :
    i = 1
    result = 0
    while i <= n :
        if i%100/10 == 1 :
	    if i/100 >0 :
		result += hundred[i/100] + 3 + excep[i%10]
	    else :
		result += hundred[i/100] + excep[i%10]
	elif i%100 == 0 :
	    result += hundred[i/100]
	
        else :
	    if i/100>0 :
	        result += hundred[i/100] + tenth[i%100/10] + digits[i%10] + 3
	    else :
                result += tenth[i%100/10] + digits[i%10]

        i+=1
		
    return result

if __name__ == "__main__" :

    t1 = time.clock()
	
    # while True :
    # a = input("quel nombre :")
    # print a, "possede", nb_letters(a), "lettres"

    print(watchTower(999)+11)
    print(time.clock() - t1, "seconds")

