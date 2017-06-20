
import time
import sys


if __name__ == "__main__" :

    t1 = time.clock()

    with open(sys.argv[1], 'r') as f:
        lines = [[int(d) for d in e] for e in [a.split(" ") for a in f][:-1]]

    for i in range(len(lines)-1, 0, -1):
        lines[i-1] = [lines[i-1][j]+max(lines[i][j], lines[i][j+1]) for j in range(0, len(lines[i-1]))]
    
    print(lines[0][0])
    print(time.clock() - t1, "seconds")
