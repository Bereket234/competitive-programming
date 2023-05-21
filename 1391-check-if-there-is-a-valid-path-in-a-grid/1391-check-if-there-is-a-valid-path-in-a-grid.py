class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        if len(grid) == 1 and len(grid[0]) ==1 :
            return True
        paths= {
            1: [(0,-1),(0,1)],
            2: [(1,0),(-1,0)],
            3: [(0,-1),(1,0)],
            4: [(1,0), (0,1)],
            5: [(0,-1), (-1,0)],
            6: [(-1,0), (0,1)],
        }
        visited= set()
        def inbound(i, j):
            return i >= 0 and j >= 0 and i<len(grid) and j < len(grid[0])
        
        def dfs(x, y):
            p= grid[x][y]
            i1, j1= x + paths[p][0][0] , y + paths[p][0][1]
            i2, j2= x + paths[p][1][0] , y + paths[p][1][1]
            if (x == len(grid)-1 and y == len(grid[0])-1) and ((i1, j1)  in visited or (i2, j2)  in visited):
                return True
            
            if (((i1, j1) not in visited and (i2, j2) not in visited) or not inbound(i1, j1) or not inbound(i2, j2)) and ((x, y) != (0,0)):
                
                return False
            visited.add((x, y))
            res1= res2= False
            if (i1, j1) not in visited and inbound(i1, j1):
                res1= dfs(i1, j1)
            if (i2, j2) not in visited and inbound(i2, j2):
                res2= dfs(i2, j2)
            return res1 or res2
        return dfs(0, 0)