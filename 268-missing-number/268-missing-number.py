class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        prev= 0
        cnt= 0
        
        for i in range(len(nums)):
            prev ^= i+1
            cnt ^= nums[i]
        
        return prev ^ cnt