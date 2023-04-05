class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_= 0
        for num in nums:
            max_ |= num
        res = 0
        def backtrack(i, prev):
            nonlocal res
            nonlocal max_
            if i == len(nums):
                if prev == max_:
                    res += 1
                return
            
            backtrack(i + 1, prev | nums[i])
            backtrack(i + 1, prev)
        
        backtrack(0, 0)
        return res