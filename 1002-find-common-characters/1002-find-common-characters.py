class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counter= []
        res= {}
        
        for i, word in enumerate(words):
            counter.append(Counter(word))
        
        for k in counter[0]:
            res[k] =counter[0][k]
            for j in range(1, len(counter)):
                res[k]= min(counter[j].get(k,0), res[k])
        print(res)
        return [letter for letter in res for j in range(res[letter])]