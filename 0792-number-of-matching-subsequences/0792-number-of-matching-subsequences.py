class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        mem= defaultdict(list)
        temp= words.copy()
        res= 0
        for c in s:
            for word in words:
                mem[word[0]].append(word)
            words= []
            for word in mem[c]:
                if len(word) == 1:
                    res +=1
                else:
                    words.append(word[1:])
            mem.pop(c)
        return res
        
        