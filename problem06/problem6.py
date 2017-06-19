
import time

if __name__ == "__main__":

    t1 = time.clock()

    print(sum([x for x in range(101)])**2 - sum([x**2 for x in range(101)]))
    print(time.clock() - t1, "seconds")
