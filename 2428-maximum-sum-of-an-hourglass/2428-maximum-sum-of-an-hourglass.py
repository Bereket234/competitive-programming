class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        prefix= [[0 for i in range(len(grid[0])+1)] for i in range(len(grid)+1)]
        res=0
        for i in range(1,len(prefix)):
            for j in range(1, len(prefix[0])):
                prefix[i][j]= grid[i-1][j-1]+prefix[i-1][j]+prefix[i][j-1] - prefix[i-1][j-1]
        

        for i in range(3, len(prefix)):
            for j in range(3, len(prefix[0])):
                res= max(res, prefix[i][j] - prefix[i][j-3] + prefix[i-3][j-3] - prefix[i-3][j]- grid[i-2][j-1]-grid[i-2][j-3])

        return res