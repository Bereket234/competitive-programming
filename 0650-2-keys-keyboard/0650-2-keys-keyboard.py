class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        dp= [float('inf') for i in range(n+1)]
        dp[1]= 0
        dp[0]=0
        
        for i in range(2,len(dp)):
            for j in range(1, i):
                if i % j == 0:
                    dp[i] = min(dp[j] + 1 + i//j - 1, dp[i])
        return dp[n]