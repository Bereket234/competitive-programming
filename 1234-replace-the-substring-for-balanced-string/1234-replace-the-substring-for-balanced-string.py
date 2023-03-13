class Solution:
    def isBalanced(self, cnt, k):
        for i, v in cnt.items():
            if v > k:
                return False
        return True
        
    
    def balancedString(self, s: str) -> int:
        counter= Counter(s)
        max_= len(s) // 4
        res= len(s) + 1
        l= 0
        if self.isBalanced(counter, max_):
            return 0
        for r in range(len(s)):
            counter[s[r]] -= 1
            while self.isBalanced(counter, max_) and l <= r:
                res= min(res, r - l + 1)
                counter[s[l]] += 1
                l+=1    
        return res