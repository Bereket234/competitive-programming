class Solution(object):
    def kthLargestNumber(self, nums, k):
        for i in range(0, len(nums), 1):
            nums[i]=int(nums[i])
        nums.sort()
        nums.reverse()
        return str(nums[k-1])
        
        