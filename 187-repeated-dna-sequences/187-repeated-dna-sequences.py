class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        counter= {}
        l=0
        for r in range(len(s)):
            if r >= 9:
                counter[s[l:r+1]]=1 + counter.get(s[l:r+1], 0)
                l+=1
        
        return [k for k,v in counter.items() if v > 1] 