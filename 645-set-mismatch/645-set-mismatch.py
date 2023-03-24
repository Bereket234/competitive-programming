class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i= 0
        res= []
        while i < len(nums):
            if nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]:
                temp= nums[i]
                nums[i], nums[temp-1]= nums[temp-1], nums[i]
            else:
                i += 1
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                res= [nums[i], i + 1]
        return res