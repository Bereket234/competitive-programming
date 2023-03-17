class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res= []
        candidates.sort()
        visited= set()
        
        def backtrack(i, sum_, combination):
            if sum_ ==  target:
                res.append(combination.copy())
                return
            if sum_ > target or i >= len(candidates):
                return
            sum_ += candidates[i]
            combination.append(candidates[i])
            c= tuple(combination)
            
            if c not in visited:
                backtrack(i + 1, sum_, combination)
            
            visited.add(c)
            combination.pop()
            sum_ -= candidates[i]
            backtrack(i + 1, sum_, combination)
            
        backtrack(0, 0, [])
        return res