class Solution:
    def check_sum(self, x, y, grid):
        row= [0, 0, 0]
        col= [0, 0, 0]
        dig1= grid[x][y] + grid[x+1][y+1] +grid[x+2][y+2]
        dig2= grid[x][y+2] + grid[x+1][y+1] + grid[x+2][y]
        set_= set()
        for m in range(x, x+3):
            for n in range(y, y+3):
                val= grid[m][n]
                row[m-x] += val
                col[n-y] += val
                set_.add(val)
        print(set_)
        for num in set_:
            if 1 > num or num > 9:
                return False
        return row == col and dig1== dig2 == row[0] and len(set_) == 9
        
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        cnt= 0
        
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                if self.check_sum(i, j, grid):
                    cnt+=1
        return cnt