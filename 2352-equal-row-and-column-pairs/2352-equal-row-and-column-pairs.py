class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counter= defaultdict(int)
        res=0
        
        for row in grid:
            counter[tuple(row)]+=1
        n= len(grid)
        
        for i in range(n):
            temp= []
            for j in range(n):
                temp.append(grid[j][i])
            res+= counter[tuple(temp)]
            
        
        return res