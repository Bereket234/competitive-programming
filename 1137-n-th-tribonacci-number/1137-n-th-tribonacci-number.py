class Solution:
    def tribonacci(self, n: int) -> int:
        res= [0, 1, 1]
        
        for i in range(3, n+1):
            res.append(res[i-1] + res[i-2] + res[i-3])
            
        return res[n]