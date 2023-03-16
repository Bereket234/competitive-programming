class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res= set()
        combs= []
        sum_= 0
        def backtrack(i, sum_):
            if sum_ == target:
                res.add(' '.join(combs))
                return
            if sum_ > target or i >= len(candidates):
                return
            sum_ += candidates[i]
            combs.append(str(candidates[i]))
            backtrack(i, sum_)
            sum_ -= candidates[i]
            combs.pop()
            backtrack(i + 1, sum_)
        
        
        for i in range(len(candidates)-1):
            backtrack(i, 0)
        ans= []
        for i, num in enumerate(res):
            ans.append(list(map(int, num.split())))
            
        return ans