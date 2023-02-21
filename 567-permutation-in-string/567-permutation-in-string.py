class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt= Counter(s1)
        counter= {}
        l= 0
        n= len(s1)
        for r in range(len(s2)):
            counter[s2[r]]= 1 + counter.get(s2[r], 0)
            for k, v in cnt.items():
                if k not in counter or v != counter[k]:
                    break
            else:
                return True
            if r - l == n-1:
                counter[s2[l]] -= 1
                l+=1
        return False