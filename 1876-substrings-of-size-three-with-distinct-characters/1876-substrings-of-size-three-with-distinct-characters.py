class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0
        seen= Counter(s[:3])
        
        res= 1 if len(seen) == 3 else 0
        
        for i in range(3, len(s)):
            seen[s[i]] += 1
            seen[s[i-3]] -= 1
            if max(seen.values()) == 1:
                res += 1
        return res
                
            