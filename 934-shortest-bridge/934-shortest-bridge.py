class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        paths= [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        root= []
        def inbound(i, j):
            return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0])
        
        
        def findRoot():
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j]:
                        return (i, j)
                        
        root= findRoot()
                        
        seen=set()
        
        deq= deque([(root[0], root[1], 0)])
        
        def dfs(i, j):
            if (i, j) in seen:
                return 
            
            seen.add((i, j))
            
            for dx, dy in paths:
                x, y= i+ dx, j + dy
                if inbound(x, y) and grid[x][y] and (x, y) not in seen:
                    deq.append((x, y, 0))
                    dfs(x, y)
        dfs(root[0], root[1])
        while deq:
            i, j, d= deq.popleft()
            for dx, dy in paths:
                x, y= i+ dx, j+ dy
                if inbound(x, y) and (x, y) not in seen and grid[x][y]:
                    return d
                if inbound(x, y) and (x, y) not in seen and not grid[x][y]:
                    deq.append((x, y, d+1))
                    seen.add((x, y))