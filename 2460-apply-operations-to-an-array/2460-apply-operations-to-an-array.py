class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)- 1):
            if nums[i]==nums[i+1]:
                nums[i]= 2 * nums[i]
                nums[i+1] = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                j= i
                while j > 0 and nums[j-1] == 0:
                    nums[j], nums[j-1] = nums[j-1], nums[j]
                    j-=1
        return nums