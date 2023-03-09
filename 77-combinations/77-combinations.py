class Solution:
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        stack=[]
        def backtrack(start, end):
            if len(stack) == k:
                arr= [i for i in stack]
                ans.append(arr)
                return
            if start > end:
                return
            
            for i in range(start, end):
                stack.append(i)
                backtrack(i + 1, end)
                stack.pop()
        backtrack(1, n+1)
        return ans
            