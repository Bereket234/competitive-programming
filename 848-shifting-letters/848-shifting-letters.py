class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        s= list(s)
        
        for i in range(len(s)-2,-1, -1):
            shifts[i] += shifts[i+1]
        for i, c in enumerate(s):
            c = ord(c)
            c+= shifts[i] - 97
            c %= 26
            c+= 97
            s[i]= chr(c)
        return "".join(s)