class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1: return 0
        parent= self.kthGrammar(n-1, k % 2 + k // 2)
        is_odd= k % 2 != 0
        
        if parent == 0:
            return 0 if is_odd else 1
        else:
            return 1 if is_odd else 0
        