class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count= 0
        
        l, r= 0, len(nums)-1
        
        while l < r:
            sum_=nums[l] + nums[r]
            if sum_  == k:
                count+=1
                l+=1
                r-=1
            elif sum_ < k:
                l+=1
            elif sum_ > k:
                r-=1
        return count