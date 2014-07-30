
import math
import time

# Je lui file un tableau contenant les multiplicateurs (1, 2, ..., n), n>1, et le multiplie t.
# Il renvoie un resultat sous la forme d'un tableau (1*t, 2*t, ..., n*t)
# On boucle tant que le resultat fait au plus 9 chiffres.
# Lorsque le resultat fait plus de 9 chiffres on augmente n


def calcul(t, arr):
    res = []
    for mult in arr:
        res.append(t*mult)
    return res

def isPandigital(arr):
    num = toInt(arr)
    z = [int(i) for i in str(num)]
    z.sort()
    return z == [1,2,3,4,5,6,7,8,9]

def toInt(arr):
    res = arr[0]
    for e in arr[1:]:
        res = ((10**int(math.log10(e)+1))*res) + e
    return res

def sizeArr (arr):
    num = toInt(arr)
    if num == 0:
        return 1
    return int(math.log10(num)+1)

if __name__ == "__main__":

    t1 = time.clock()

    t = 5000
    arr = [1, 2]
    maxi = 0

    while len(arr) < 10:

        t = int(1000/10**len(arr))+1
        res = [0]
        while sizeArr(res) < 10:
            res = calcul(t, arr)
            if isPandigital(res) and toInt(res) > maxi:
                maxi = toInt(res)
            t += 1
            #print "\t", t, res
        arr.append(arr[-1]+1)
        #print arr

    print maxi, "waaaayyyyy too easy. Computation done under", time.clock() - t1, "seconds"
