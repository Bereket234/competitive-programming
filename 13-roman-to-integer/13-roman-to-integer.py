class Solution:
    def romanToInt(self, s: str) -> int:
        mem= {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        prev= mem[s[-1]]
        res= mem[s[-1]]
        for i in range(len(s) -2, -1, -1):
            c= s[i]
            if mem[c] < prev:
                res -= mem[c]
            else:
                res += mem[c]
            prev= mem[c]
        
        
        return res