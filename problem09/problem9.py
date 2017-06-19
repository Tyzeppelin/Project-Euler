
import time

def test (a, b, c) :
    """
    just test if abc is a Pythagorean triplet 
    """

    if ((a**2+ b**2) == c**2) :
        return True
    else :
        return False


if __name__ == "__main__" :

    t1 = time.clock()

    a = 1
    b = 0
    c = 0 # hyoptenuse 
	
    done = False

    # 0<a<500
    while a < 500 :
        # a is fixed, we know that a+b+c = 1000
        # so we can calculate the value of b and c 
	# for each a fixed.
	c = (-a**2 + 1000*a - 500000)/(a-1000)
	b = 1000-a-c
        if test(a, b, c) :
            break	
        a+=1	
	
    print(a, b, c, a*b*c)
    print(time.clock() - t1, "seconds")
