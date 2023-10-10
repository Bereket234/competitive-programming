class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        initial= 2**32-1
        res= initial
        for num in nums:
            res &= num
        if res != 0:
            return 1
        res= initial
        cnt= 0
        for i, num in enumerate(nums):
            res &= num
            if res == 0:
                cnt += 1
                res= initial
        return cnt