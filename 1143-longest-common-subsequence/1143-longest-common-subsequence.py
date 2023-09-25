class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp= [0 for i in range(len(text1) + 1)]
        prev= [0 for i in range(len(text1) + 1)]
        for i in range(len(text2)- 1, -1, -1):
            prev= dp.copy()
            for j in range(len(dp) - 2, -1, -1):
                if text2[i] == text1[j]:
                    dp[j]= 1 + prev[j+1]
                else:
                    dp[j]= max(prev[j], dp[j+1])
        return dp[0]