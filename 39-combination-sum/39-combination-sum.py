class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res= []
        combs= []
        sum_= 0
        def backtrack(i, sum_):
            if sum_ == target:
                res.append(combs.copy())
                return
            if sum_ > target or i >= len(candidates):
                return
            sum_ += candidates[i]
            combs.append(candidates[i])
            backtrack(i, sum_)
            sum_ -= candidates[i]
            combs.pop()
            backtrack(i + 1, sum_)
        
        backtrack(0, 0)
            
        return res