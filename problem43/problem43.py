
import math
import time

# Conditions :
# On a un nombre 0-n pandigital tel qu'il soit de la forme a1a2a3a4a5a6a7a8a9a10
# One a :
#
# a2a3a4 div 2
# a3a4a5 div 3
# a4a5a6 div 5
# a5a6a7 div 7
# a6a7a8 div 11
# a7a8a9 div 13
# a8a9a10 div 17


#
# d1 = ?
# d2 = ?
# d3 = -2d7 + k
# d4 = 0, 2, 4, 6, 8
# d5 = 2d7 + k
# d6 = 0, 5
# d7 = 0...9
# d8 = d7 + k
# d9 = 1/2d7 + k
# d10 = 9/20d7 + k
#
#

def isPandigital(n):
    arr = n
    arr.sort()
    return arr == range(10)

def get_d1():
    return 0

def get_d2():
    return 0

def get_d3(d4, d5):
    d3 = -0.1
    i = 1
    k = 0
    while d3%1 != 0.0 or d3 < 0:
        d3 = 3*k - d4 - d5
        if d3 > 9:
            i = -1
            k = 0
        k += i
#        print d3, d4, d5, k, i
    return int(d3)

def get_d4():
    return [0, 2, 4, 6, 8]

def get_d5(d6, d7):
    d5 = -0.1
    i = 1
    k = 0
    while d5%1 != 0.0 or d5 < 0:
        d5 = (2*d7-d6+7*k)/10.0
#        print d5, d6, d7, k, i
        k += i
    return int(d5)

def get_d6():
    return [0, 5]

def get_d8(d6, d7):
    d8 = -0.1
    i = -1
    if d7-d6 < 11:
        i = 1
    k = 0
    while d8%1 != 0.0 or d8 < 0:
        d8 = d7-d6+11.0*k
 #       print d8, d6, d7, k, i
        k += i
    return int(d8)

def get_d9(d7, d8):
    d9 = -0.1
    i = 1
    k = 0
    while d9%1 != 0.0 or d9 < 0:
        d9 = (13*k-10*d7-d8)/4.0
        k += i
    return int(d9)

def get_d10(d8, d9):
    d10 = -0.1
    i = -1
    if (10*d8+d9) < 17:
        i = 1
    k = 0
    while d10%1 != 0.0 or d10 < 0:
        d10 = (-17*k+10*d8+d9)/5.0
#        print d10, d8, d9, k, i
        k += i
    return int(d10)

def getRemains(arr):
    ref = range(10)
    for e in arr:
        ref.pop(e)
    return ref

def toInt(arr):
    res = arr[0]
    for e in arr[1:]:
        res = ((10**int(math.log10(e)+1))*res) + e
    return res

if __name__ == "__main__":

    t1 = time.clock()

    arr = []

    arr_d4 = [0, 2, 4, 6, 8]
    arr_d6 = [0, 5]


    for d7 in range(10):
        for d4 in arr_d4:
            for d6 in arr_d6:
                d5 = get_d5(d6, d7)
                d3 = get_d3(d4, d5)
                d8 = get_d8(d6, d7)
                d9 = get_d9(d7, d8)
                d10 = get_d10(d8, d9)
                num = [d3, d4, d5, d6, d7, d8, d9, d10]
                try :
                    r = getRemains(num)
                    num = r+num
                    if isPandigital(num):
                        arr.append(toInt(num))
                    r.reverse()
                    num = r+num
                    if (isPandigital(num)):
                        arr.append(toInt(num))
                except IndexError:
                    print "not a pandig", num
        print arr
    print(arr)


    print isPandigital(123456789)
