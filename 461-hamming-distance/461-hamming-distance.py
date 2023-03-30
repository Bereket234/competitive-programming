class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        humm= x ^ y
        res= 0
        while humm > 0:
            res += humm & 1
            humm >>= 1
        return res