class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp= [0] * len(triangle[-1])
        for i in range(len(triangle)-1, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] += triangle[i][j]
            for j in range(len(triangle[i])-1):
                dp[j] = min(dp[j], dp[j+1])
            
        return dp[0]