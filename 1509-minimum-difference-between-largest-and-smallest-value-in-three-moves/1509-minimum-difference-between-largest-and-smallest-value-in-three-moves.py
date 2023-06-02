class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) <= 4:
            return 0
        
        j = -4
        diff= nums[j] - nums[0]
        for i in range(4):
            diff= min(diff, nums[j] - nums[i])
            j+=1
        return diff
            
            