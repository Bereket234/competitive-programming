class Solution:
    def countArrangement(self, n: int) -> int:
        res= 0
        def backtrack(i, arr):
            nonlocal res
            if i and (not (arr[-1] % i == 0 or i % arr[-1] == 0)):
                return 
            if i == n:
                res +=1
                return
            for j in range(1, n+1):
                if j not in arr:
                    arr.append(j)
                    backtrack(i + 1, arr)
                    arr.pop()
        backtrack(0, [])
        return res
        