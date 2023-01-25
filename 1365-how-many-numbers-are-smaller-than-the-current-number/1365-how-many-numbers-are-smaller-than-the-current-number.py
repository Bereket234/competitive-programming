class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        cntr= [0 for i in range(101)]
        res= [0 for i in range(len(nums))]
        for num in nums:
            cntr[num] +=1
        
        for i in range(1,len(cntr)):
            cntr[i]= cntr[i-1] + cntr[i]
        for i in range(len(nums)):
            if nums[i] > 0:
                res[i]= cntr[nums[i]-1]
            
        return res