#!/usr/bin/env/python

import sys
import time

if __name__ == "__main__" :

    t1 = time.clock()

    with open(sys.argv[1], 'r') as f:
        lines = [[int(d) for d in e] for e in [a.split(" ") for a in f][:-1]]

    l = len(lines)

    for i in range(l-1, 0, -1):
        lines[i-1] = [lines[i-1][j]+max(lines[i][j], lines[i][j+1]) for j in range(len(lines[i-1]))]
        #print(lines[i-1]) 
    print(lines[:3])
    print(time.clock() - t1, "seconds")
