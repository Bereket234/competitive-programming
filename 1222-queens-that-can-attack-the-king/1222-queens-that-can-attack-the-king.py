class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        res=[]
        visited= [[False for _ in range(8)] for _ in range(8)]
        
        for queen in queens:
            [x, y]= queen
            visited[x][y]= True
        direction= [-1, 0, 1]
        
        for dx in direction:
            for dy in direction:
                if dx==0  and dy==0:
                    continue
                x= king[0]
                y= king[1]
                while x+dx >= 0 and x+dx < 8 and y+dy >= 0 and y+dy < 8:
                    x+= dx
                    y+= dy
                    if visited[x][y]:
                        res.append([x, y])
                        break
                    
        return res