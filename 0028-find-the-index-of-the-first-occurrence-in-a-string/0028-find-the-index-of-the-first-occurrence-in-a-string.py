class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        power= [1]
        mod= 10 **9 +7
        for i in range(1, len(needle)):
            power.append(power[i-1] * 26)
        
        j= len(needle)-1
        n= 0
        for i in range(len(needle)):
            n = (n + (ord(needle[i]) - 96) * power[j])% mod
            j-=1
        
        
        res= 0
        l=0
        
        for i in range(len(haystack)):
            res = ((res*26) + (ord(haystack[i])-96))%mod
            
            if i-l +1 < len(needle):
                continue
            
            print(i, n, res)
            if n == res:
                return l
            
            res-= ((ord(haystack[l])-96) * power[i-l])%mod
            l+=1
        return -1