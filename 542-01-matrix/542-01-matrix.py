class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        res= [[0 for i in range(len(mat[0]))] for j in range(len(mat))]
        
        deq= deque([])
        path= [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited= [[1 for i in range(len(mat[0]))] for j in range(len(mat))]
        
        def inbound(i, j):
            return i>= 0 and j >= 0 and i< len(mat) and j< len(mat[0])
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if not mat[i][j]:
                    deq.append((i, j))
        
        while deq:
            i, j= deq.popleft()
            visited[i][j] = 0
            for x, y in path:
                newx, newy= i+ x, j + y
                if inbound(newx, newy) and visited[newx][newy] and mat[newx][newy]:
                    if res[newx][newy]:
                        res[newx][newy]= min(res[newx][newy], res[i][j] + 1)
                        deq.append((newx, newy))
                        continue
                    res[newx][newy]= res[i][j] + 1
                    deq.append((newx, newy))
        return res
                
            
            