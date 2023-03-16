class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res= []
        def backtrack(i, perms):
            if len(perms) == len(nums):
                res.append(perms.copy())
                return
            
            for j in range(len(nums)):
                if nums[j] not in perms:
                    perms.append(nums[j])
                    backtrack(i+1, perms)
                    perms.pop()
            return
        backtrack(0, [])
            
        return res
            