import time



class Sudoku:

    def __init__(self):
        # grid is only one dimension I KNOW
        self.grid = [list(range(10))]*81
        #self.grid = [0]*81
        self.hits = [0]*81

    def load(self, mat):
        """
        suppose mat is trimmed
        """
        print(mat)
        self.print_grid
        for i in range(9):
            for j in range(9):
                v = mat[i][j]
                if v != "0":
                     print("++++++++++++")
                     self.insert(i, j, int(v))
                     self.print_grid()
                     print("++++++++++++")

    def insert(self, i, j, v):
        self.grid[i*9 + j] = [v]
        self.hits[i*9 + j] = -1000
        print("(", i, j, ")", "=", v)
        print([x*9 + j for x in range(9)])
        print([i*9 + x for x in range(9)])
        for x in range(9):
            # remove v on line i
            if x != i:
                try:
                    self.grid[x*9 + j].remove(v)
                except ValueError:
                    ...
            # remove v on column j
            if x != j:
                try:
                    self.grid[i*9 + x].remove(v)
                except ValueError:
                    ...

        # remove v on grid ?? x ??
        x = i // 3
        y = j // 3

        print([[3*t+1, 3*t+2, 3*t+3] for t in [3*x+y, 3*x+y+3, 3*x+y+6]])
        for t in [3*x + y, 3*x + y + 3, 3*x + y + 6]:
            if 3*t+1 != i*9+j:
                try:
                    self.grid[3*t+1].remove(v)
                except ValueError:
                    ...
            if 3*t+2 != i*9+j:
                try:
                    self.grid[3*t+2].remove(v)
                except ValueError:
                    ...
            if 3*t+3 != i*9+j:
                try:
                    self.grid[3*t+3].remove(v)
                except ValueError:
                    ...


    def print_grid(self):
        print("---------")
        for i in range(9):
            #print([sum(l) for l in self.grid][i*9:i*9+9])
            print([l for l in self.grid][i*9:i*9+9])
            #print([l for l in self.grid[i*9:i*9+9]])
        print("--------")



if __name__ == "__main__":
    
    t1 = time.time()

    with open("./0096_sudoku.txt", "r") as f:
        f_lines = f.readlines()
        assert len(f_lines) % 10 == 0
        for n in range(len(f_lines) // 10)[:1]:
            s = Sudoku()
            s.load([e.rstrip() for e in f_lines[n+1: n+10]])
            s.print_grid()

    print("done under", time.time() - t1, "seconds.")
