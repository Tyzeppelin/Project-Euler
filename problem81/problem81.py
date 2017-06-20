
import numpy as np
import time

# As ye auld sayin' goes: "If it's a tree, it's easy" 

def go_up(s):
    r = set()
    for t in s:
        if t[0] != 0:
            r.add((t[0]-1, t[1]))
        if t[1] != 0:
            r.add((t[0], t[1]-1))
    return r


if __name__ == '__main__':

    t1 = time.clock()

    with open("matrix.txt", 'r') as f:
        matrix = [[int(v) for v in l.rstrip().split(',')] for l in f.readlines()]

    line = set([(79,79)])
   
    while len(line) != 0:
        line = go_up(line)
        if len(line) == 1:
            matrix[0][0] += min(matrix[0][1], matrix[1][0])
            break
        for n in line:
            if n[0] == 79:
                matrix[n[0]][n[1]] += matrix[n[0]][n[1]+1]
            elif n[1] == 79:
                matrix[n[0]][n[1]] += matrix[n[0]+1][n[1]]
            else:
                matrix[n[0]][n[1]] += min(matrix[n[0]+1][n[1]], matrix[n[0]][n[1]+1])
    print(matrix[0][0])
    print(time.clock() - t1, "seconds")
