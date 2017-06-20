#!/usr/bin/python

from math import factorial, floor
import time

if __name__ == "__main__" :

    t1 = time.clock()

    digits = range(10)

    target = 1000002.0

    res = []

    i = 0

    while len(digits) > 1:
        #print "==="
        #print digits
        #print "i =", target, "/", factorial(len(digits)-1)
        i = floor(target/factorial(len(digits)-1))
        target = target%factorial(len(digits)-1)

        # lil' hack. If (by any chance) the target is a multiple of (len(digits)-1)!
        # we don't get screwed. The target would be one digit ahead due to the "-1" operation before the factorial
        # I can probably afford this monstruosity by bypassing the "-1" and the floor() call.
        if target == 0.0 :
            i -= 1

        res.append(digits[int(i)])
        digits.remove(digits[int(i)])
        #print "i:", i
        #print "new target:", target
        #print res, digits
    res.append(digits[0])

    print(int(''.join(map(str, res))))
    print(time.clock()-t1, "seconds")
