
import time

def pascalTriangle (n) :
	a = [1, 1]
	i = 1
	while i < n :
		b = [1]
		#print a
		for j in range(len(a)-1):
			b.append(a[j]+a[j+1])
		b.append(1)
		a = b
		i += 1
	return a

def Lattice (n) :
	a = pascalTriangle(2*n)
	#print a
	return a[(len(a)-1)//2]

if __name__ == "__main__" :

    t1 = time.clock()

    n = int(input())
    print(n, Lattice(n))
    
    print(time.clock() - t1, "seconds")
