class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(h):
            rob1, rob2= 0, 0
            
            for num in h:
                temp= max(rob1 + num, rob2)
                rob1= rob2
                rob2= temp
            return max(rob1, rob2)
        if len(nums) == 1:
            return nums[0]
        return max(helper(nums[0:len(nums)-1]), helper(nums[1: len(nums)]))
        