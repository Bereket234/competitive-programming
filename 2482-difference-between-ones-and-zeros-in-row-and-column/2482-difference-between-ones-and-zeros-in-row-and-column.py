class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        count= [[0 for i in range(len(grid))], [0 for i in range(len(grid[0]))]]
        m, n= len(grid), len(grid[0])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                count[0][i] += grid[i][j]
                count[1][j] += grid[i][j]
        print(count)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j]= count[0][i] + count[1][j] -(m - count[0][i]) - (n - count[1][j])
        return grid
                
                
        
        