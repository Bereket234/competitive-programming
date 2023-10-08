class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp= [0] * (len(nums1) + 1)
        
        prev= dp.copy()
        
        for i in range(len(nums2) - 1, -1, -1):
            for j in range(len(nums1) - 1, -1, -1):
                if nums1[j] == nums2[i]:
                    dp[j] = prev[j+1] + 1
                else:
                    dp[j]= max(prev[j], dp[j+1])
            prev= dp.copy()
        return dp[0]