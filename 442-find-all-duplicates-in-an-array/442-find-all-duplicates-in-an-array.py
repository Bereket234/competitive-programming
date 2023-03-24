class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res= []
        
        i= 0
        while i < len(nums):
            if nums[i] != i+1 and nums[nums[i] -1] != nums[i]:
                temp= nums[i]-1
                nums[i], nums[temp]= nums[temp], nums[i]
                
            else:
                i += 1
        
        for i in range(len(nums)):
            if nums[i] != i +  1:
                res.append(nums[i])
        
        return res