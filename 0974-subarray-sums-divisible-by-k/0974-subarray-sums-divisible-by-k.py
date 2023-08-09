class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prev_sum ={0: 1}
        res= 0
        sum_= 0
        
        for num in nums:
            sum_ += num
            res += prev_sum.get(sum_ % k, 0)
            
            prev_sum[sum_ % k] = 1 + prev_sum.get(sum_ % k, 0)
        
        return res
        