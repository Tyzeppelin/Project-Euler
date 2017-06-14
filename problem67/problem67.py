
import time


if __name__ == "__main__":

    t1 = time.clock()

    with open("triangle.txt", 'r') as f:
        triangle = [map(int, s.split(" ")) for s in f.readlines()]

    for i in reversed(range(1, len(triangle), 1)):
        triangle[i-1] = [triangle[i-1][j] + max(triangle[i][j], triangle[i][j+1]) for j in range(0,len(triangle[i-1]))] 

    print(triangle[0][0])
    print(time.clock() - t1, "seconds")
