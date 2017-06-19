
import time

if __name__ == "__main__" :

    t1 = time.clock()

    print(sum(filter(lambda x: x%3 == 0 or x%5 == 0, range(1,1000))))
    print(time.clock() - t1, "seconds")
