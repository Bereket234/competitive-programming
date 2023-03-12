class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n= len(grid[0])
        prefix1, prefix2= grid[0], grid[1]
        
        for i in range(1, n):
            prefix1[i] += prefix1[i - 1]
            prefix2[i] += prefix2[i - 1]
        
        res= float('inf')
        for i in range(n):
            top= prefix1[-1] - prefix1[i]
            bottom= prefix2[i - 1] if i > 0 else 0
            second_max= max(top, bottom)
            res= min(res, second_max)
        
        return res