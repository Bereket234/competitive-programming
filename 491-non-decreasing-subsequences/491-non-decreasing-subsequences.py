class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res= set()
        
        def backtrack(i, arr):
            if len(arr) > 1 and arr[-1] < arr[-2]:
                return
            
            if len(arr) >= 2:
                res.add(tuple(arr))
                
            if i >= len(nums):
                return
            
            
            arr.append(nums[i])
            backtrack(i + 1, arr)
            arr.pop()
            backtrack(i + 1, arr)
        backtrack(0, [])
        return res