class Solution:
    def reverseBits(self, n: int) -> int:
        res= 0
        i= 0
        
        while i < 32:
            curr= n & 1 << i
            if curr != 0:
                res |= (1 << (31-i))
            i+=1
            
            
        return res