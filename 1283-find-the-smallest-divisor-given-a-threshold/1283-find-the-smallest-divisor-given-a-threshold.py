class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        max_diviser= max(nums)
        low= 1 
        high= max_diviser
        res= max_diviser
        while low <= high:
            mid= (low + high) // 2
            sum_= 0
            for num in nums:
                sum_ += (math.ceil(num / mid))
            if sum_ > threshold:
                low= mid + 1
            else:
                res= min(mid, res)
                high= mid - 1
        return res
                
            