import time

if __name__ == "__main__" :
    t1 = time.time()
    print(pow(2, 7830457, 10**10))
    print("done under", time.time() - t1, "seconds") 
