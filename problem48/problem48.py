
import time

class numb:

    def __init__(self, n):
        self.short = str(n)[-10:]

    def add(self, n):
        self.short = str(int(float(self.short))+n)[-10:]

    def get_short(self):
        return int(float(self.short))

if __name__ == "__main__":

    t1 = time.clock()

    some = numb(1)
    i = 2
    while i <= 1000:
        some.add(i**i)
        i += 1

    print some.get_short()

    print "executed under", time.clock()-t1, "seconds."
