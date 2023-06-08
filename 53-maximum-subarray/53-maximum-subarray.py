class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum= 0
        max_= nums[0]
        for i in range(len(nums)):
            curr_sum += nums[i]
            max_= max(curr_sum, max_)
            if curr_sum < 0:
                curr_sum= 0
            
        return max_
            
            
            