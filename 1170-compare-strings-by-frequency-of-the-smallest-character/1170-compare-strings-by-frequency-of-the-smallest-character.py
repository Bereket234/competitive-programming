class Solution:
    def min_cnt(self, s):
        counter= Counter(s)
        min_= s[0]
        for c in s:
            min_= min(min_, c)
        
        return counter[min_]
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        for i in range(len(queries)):
            queries[i]= self.min_cnt(queries[i])
            
        for i in range(len(words)):
            words[i]= self.min_cnt(words[i])
        words.sort()
        res=[]
        for query in queries:
            low= 0
            high= len(words)-1
            
            while low <= high:
                mid= (low + high) // 2
                if words[mid] < query+1:
                    low= mid + 1
                else:
                    high= mid - 1
            res.append(len(words) - low)
        return res