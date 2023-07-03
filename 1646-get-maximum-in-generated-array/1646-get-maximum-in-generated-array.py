class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        res= [0, 1]
        
        if n == 0:
            return 0
        
        for i in range(2, n+1):
            if i % 2 == 0:
                res.append(res[i //2])
            else:
                res.append(res[(i//2)+1] + res[(i//2)])
        return max(res)