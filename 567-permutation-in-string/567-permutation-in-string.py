class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1= Counter(s1)
        c2= Counter(s2[:len(s1)-1])
        l=0
        
        for i in range(len(s1)-1, len(s2)):
            c2[s2[i]]= 1 + c2.get(s2[i], 0)
            if c1 == c2:
                return True
            
            c2[s2[l]] -= 1
            if c2[s2[l]] == 0:
                c2.pop(s2[l])
            l+=1
        return False