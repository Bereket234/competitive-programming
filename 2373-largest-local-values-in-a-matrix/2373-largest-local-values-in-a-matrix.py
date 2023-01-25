class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        def find_local(x, y, grid):
            max_= grid[x][y]
            
            for m in range(x, x+3):
                for n in range(y, y+3):
                    max_= max(max_, grid[m][n])
            return max_
        
        
        res= [[0 for _ in range(len(grid)-2)] for _ in range(len(grid)-2)]
        for i in range(len(grid)-2):
            for j in range(len(grid)-2):
                res[i][j]= find_local(i, j, grid)
        return res