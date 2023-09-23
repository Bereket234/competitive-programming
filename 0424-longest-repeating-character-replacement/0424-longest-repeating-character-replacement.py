class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter= {}
        
        res= 0
        l= 0
        max_= 0
        for r in range(len(s)):
            counter[s[r]] = counter.get(s[r], 0) + 1
            max_= max(counter.values())
            while r-l + 1 - max_ > k:
                counter[s[l]] -= 1
                l+=1
            res= max(res, r-l +1)
        return res
            