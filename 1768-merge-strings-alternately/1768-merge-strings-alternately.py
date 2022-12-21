class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res= []
        i=0
        while i < len(word1) or i< len(word2):
            if i < len(word1) and i< len(word2):
                res.append(word1[i])
                res.append(word2[i])
            elif i < len(word1):
                res.append(word1[i])
            else:
                res.append(word2[i])
            i+=1
        return ''.join(res)