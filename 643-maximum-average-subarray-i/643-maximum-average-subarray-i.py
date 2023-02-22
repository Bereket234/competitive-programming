class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left= 0
        res= float('-inf')
        sum_= 0
        
        for right in range(len(nums)):
            sum_ += nums[right]
            if right - left + 1 == k:
                res= max(res, sum_/k)
                sum_-= nums[left]
                left+=1
                
            
        return res