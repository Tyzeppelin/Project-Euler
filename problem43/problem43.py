
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

def isPandig(n):
    arr = toArr(n)
    arr.sort()
    base = range[10]
    return arr == base

def mbPandig(n):
    arr = toArr(n)
    arr.sort()
    base = range(10)
    try :
        for v in arr:
            base.remove(v)
    except ValueError :
        return False
    return len(base) == 2

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

def toArr(n):
    res = []
    a = n
    while a >= 1:
        res.append(a%10)
        a = a/10
    if int(math.log10(n)+1) == 7:
        res.append(0)
    return res[::-1]

def cond(n):
    arr = toArr(n)
    #print arr
    if (arr[1]) % 2 != 0:
        #print "!%2"
        return False
    if (arr[0]+arr[1]+arr[2]) % 3 != 0:
        #print "!%3"
        return False
    if (arr[3]) % 5 != 0:
        #print "!%5"
        return False
    if (10*arr[2]+arr[3]-2*arr[4]) % 7 != 0:
        #print "!%7"
        return False
    if abs(arr[3]-arr[4]+arr[5]) % 11 != 0:
        #print "!%11"
        return False
    if (10*arr[4]+arr[5]+4*arr[6]) % 13 != 0:
        #print "!%13"
        return False
    if (10*arr[5]+arr[6]-5*arr[7]) % 17 != 0:
        #print "!%17"
        return False
    return True

if __name__ == "__main__":

    t1 = time.clock()

    arr = []

    #print cond(6357289)

    #time.sleep(10)

    i = 1324567

    while i <= 98765432 :
        if mbPandig(i):
            if cond(i):
                print i
        i += 1

    # way too long -> 16695334890
