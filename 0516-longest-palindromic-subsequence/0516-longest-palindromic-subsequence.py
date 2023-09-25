class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [0 for i in range(len(s) + 1)]
        prev= [0 for i in range(len(s) + 1)]
        s2= s[::-1]
        
        for i in range(len(s) - 1, -1, -1):
            prev= dp.copy()
            
            for j in range(len(s)-1, -1, -1):
                if s[i] == s2[j]:
                    dp[j]= 1 + prev[j+1]
                    
                else:
                    dp[j]= max(dp[j+1], prev[j])
        return dp[0]