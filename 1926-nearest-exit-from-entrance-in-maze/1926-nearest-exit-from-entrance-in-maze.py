class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        paths= [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        deq= deque([[entrance[0], entrance[1], 0]])
        visited=[[1 for i in range(len(maze[0]))] for j in range(len(maze))]
        def inbound(i, j):
            return i>= 0 and j >= 0 and i< len(maze) and j <len(maze[0])
        
        while deq:
            i, j, d= deq.popleft()
            
            for x, y in paths:
                newx, newy= x + i, y + j
                
                if inbound(newx, newy) and visited[newx][newy] and maze[newx][newy] == '.':
                    visited[newx][newy]= 0
                    deq.append([newx, newy, d + 1])
                    
                if i == entrance[0] and j == entrance[1]:
                    continue
                if not inbound(newx, newy):
                    return d
        return -1