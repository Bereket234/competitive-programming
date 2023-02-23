class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        r,l= 0,0
        sum_, res= 0, len(nums) + 1
        for r in range(len(nums)):
            sum_+= nums[r]
            while target <= sum_:
                res= min(r-l+1, res)
                sum_-= nums[l]
                l+=1
                
           
        return 0 if res > len(nums) else res