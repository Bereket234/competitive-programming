class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1: return False
        power= round(math.log(n, 3))
        return n == 3**power