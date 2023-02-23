class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix= [0 for _ in range(len(s)+1)]
        s= list(s)
        
        for shift in shifts:
            st, e, d= shift
            if d == 0:
                prefix[st] -= 1
                prefix[e+1] += 1
            else:
                prefix[st] += 1
                prefix[e+1] -= 1
        for i in range(1, len(prefix)):
            prefix[i] = prefix[i] + prefix[i-1]
        
        for i, c in enumerate(s):
            
            c= ord(c)
            c= c + prefix[i] -97
            c %= 26
            c+=97
            s[i]= chr(c)
        return "".join(s)
            
            