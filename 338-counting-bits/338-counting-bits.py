class Solution:
    def countBits(self, n: int) -> List[int]:
        res= [0]
        offset= 1
        for i in range(1, n+1):
            if 2 * offset == i:
                offset = i
            
            res.append(1 + res[i - offset])
        return res