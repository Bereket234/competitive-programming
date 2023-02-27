class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        grid= [[0 for _ in range(n+1)] for _ in range(n+1)]
        
        for query in queries:
            r1, c1, r2, c2= query
            r1, c1, r2, c2=r1+1, c1+1, r2+1, c2+1
            grid[r1][c1] += 1
            if r2 + 1 <= n:
                grid[r2+1][c1] -= 1
            if c2 +1 <= n:
                grid[r1][c2+1] -= 1
            if c2 +1 <= n and r2 + 1 <= n:
                grid[r2+1][c2+1] += 1
        
        for i in range(1,len(grid)):
            for j  in range(1,len(grid)):
                grid[i][j]= grid[i-1][j] + grid[i][j-1] + grid[i][j] -grid[i-1][j-1]
        return [[grid[i][j] for j in range(1, len(grid))] for i in range(1, len(grid))]