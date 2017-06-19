
import time


if __name__ == "__main__":

    t1 = time.clock()

    optimus = [2]
    
    b = True
    i = 3
    j = 1
    
    
    while j < 10001 :
        b = True
        for e in optimus :
            if i%e == 0 :
                b = False
                break
        if b :
            optimus.append(i)
            j += 1
        i += 2
    
    print(optimus[-1])
    print(time.clock() - t1 , 'seconds')
    
