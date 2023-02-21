class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums= set(nums)
        res= 0
        
        for num in nums:
            i=num
            if not num -1 in nums:
                i= num
                while i in nums:
                    i += 1
            res= max(res, i-num)
        return res