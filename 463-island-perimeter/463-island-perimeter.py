class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        positions= [(0, -1), (-1, 0), (0, 1), (1, 0)]
        seen= [[1 for i in range(len(grid[j]))] for j in range(len(grid))]
        res= 0
        def inbound(i, j):
            return i >= 0 and j>=0 and i < len(grid) and j < len(grid[i])
        
        def dfs(i, j):
            nonlocal res
            if not seen[i][j]:
                return
            seen[i][j]= 0
            for position in positions:
                newi= i + position[0]
                newj= j + position[1]
                
                if inbound(newi, newj) and grid[newi][newj]:
                    dfs(newi, newj)
                else:
                    res += 1
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    dfs(i, j)
                    break
        return res