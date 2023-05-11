class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt= Counter(words)
        
        cnt= list(cnt.items())
        cnt.sort()
        cnt= sorted(cnt, key= lambda x: x[1], reverse= True)
        res= []
        for i in range(k):
            res.append(cnt[i][0])
        return res