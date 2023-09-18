class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp= [{} for i in range(len(nums))]
        diffs= set()
        res= [0] * len(nums)        
        for i in range(1,len(nums)):
            diffs= set()
            for j in range(i-1, -1, -1):
                diff = nums[i] -nums[j]
                if diff not in diffs:
                    dp[i][diff] = dp[j].get(diff, 1) + 1
                    diffs.add(diff)
        for i in range(len(dp)):
            if dp[i]:
                res[i] = max(dp[i].values())
        return max(res)