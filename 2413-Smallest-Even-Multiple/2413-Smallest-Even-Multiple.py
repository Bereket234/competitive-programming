class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        for i in range(1, n+1):
            if i*2 % n == 0:
                return i*2