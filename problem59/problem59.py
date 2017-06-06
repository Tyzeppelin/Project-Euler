
import itertools
import operator
import time

from itertools import product 
from operator import xor


if __name__ == "__main__":

    t1 = time.clock()

    f = open('cipher.txt', 'r')
    msg = f.readlines()[0].rstrip()
    cipher = [int(c) for c in msg.split(',')]

    #print(cipher)

    asc = range(97,123)

    g = open("res.txt", 'w')

    raw = []

    for k in product(asc, repeat=3):
        #print(chr(k[0]), chr(k[1]), chr(k[2]))
        res = []
        key = ([kx for kx in k] * 400)
        key.append(k[0])      
 
        #print(key) 
        res = [key[i] ^ cipher[i] for i in range(len(cipher))]

        txt = ''.join([chr(c) for c in res])

        if 'human' in txt:
            print(chr(k[0]), chr(k[1]), chr(k[2]))
            print(txt)
            print(sum(res))
            raw.append(txt)

    print(time.clock() - t1, "seconds")
