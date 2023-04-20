class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        cnt = 0
        paths= [(-1, 0), (0, -1), (1, 0), (0, 1)]
        
        def inbound(i, j):
            return i >= 0 and j >= 0 and i < len(grid1) and j < len(grid1[i])
        res= True
        def dfs(i, j):
            nonlocal res
            grid2[i][j] = 0
            
            for path in paths:
                newi= i + path[0]
                newj= j + path[1]
                
                if inbound(newi, newj) and grid2[newi][newj]:
                    if (not grid1[newi][newj]):
                        res= False
                    dfs(newi, newj)
            
            
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid2[i][j] and grid1[i][j]:
                    res = True
                    dfs(i, j)
                    if res:
                        cnt+= 1
        return cnt