class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr_sum= 0
        for i in nums:
            arr_sum+=i
        n= len(nums)
        range_sum= (n*(1 + n))//2
        return range_sum - arr_sum
            
        