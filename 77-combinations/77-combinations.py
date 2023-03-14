class Solution:
    #problem backtracking by considering and evaluating each case
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans= []
        combinations= []
        
        #recursive function to backtrack and append each possible answer
        def backtrack(start):
            # case when we find a valid lengh of numbers whick equals k
            if len(combinations) == k:
                copy= combinations.copy()
                ans. append(copy)
                return
            
            for i in range(start, n+1):
                combinations.append(i)
                backtrack(i + 1)
                combinations.pop()
        backtrack(1)
        return ans
        
            