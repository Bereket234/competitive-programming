class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        sum_= nums[0]
        max_= nums[0]
        
        for i in range(1, len(nums)):
            sum_ += nums[i]
            max_= max(max_, math.ceil(sum_ / (i +1)))
        return max_