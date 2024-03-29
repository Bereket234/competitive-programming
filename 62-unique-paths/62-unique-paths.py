class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp= [[0 for i in range(n)] for j in range(m)]
        
        dp[0][0] = 1
        
        for i in range(len(dp)):
            dp[i][0]= 1
        for i in range(len(dp[0])):
            dp[0][i] = 1
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j]= dp[i][j-1] + dp[i-1][j]
        
        return dp[m-1][n-1]