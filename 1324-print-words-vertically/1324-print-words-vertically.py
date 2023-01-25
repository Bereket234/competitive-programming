class Solution:
    def printVertically(self, s: str) -> List[str]:
        s= s.split()
        max_len= len(max(s, key= lambda c:len(c)))
        res= [[' ' for i in range(len(s))] for j in range(max_len)]
        for i in range(max_len):
            for j in range(len(s)):
                if len(s[j]) > i:
                    res[i][j]= s[j][i]
        for i, s in enumerate(res):
            res[i]= ''.join(s).rstrip(' ')
        return res