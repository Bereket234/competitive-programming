class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res= []
        visited= set()
        subset= []
        
        def backtrack(i):
            if i >= len(nums):
                subset.sort()
                res.append(subset.copy())
                return 
            
            
            subset.append(nums[i])
            if tuple(subset) not in visited:
                backtrack(i + 1)
            visited.add(tuple(subset))
            subset.pop()
            backtrack(i + 1)
        nums.sort()
        backtrack(0)
        return res