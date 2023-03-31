class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        t= (n & 1) == 1
        
        while n > 0:
            if t != n & 1:
                return False
            n >>= 1
            t= not t
        return True