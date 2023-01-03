class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic= defaultdict(list)
        res=[]
        
        for i, s in enumerate(strs):
            tmp=list(s)
            tmp.sort()
            tmp=''.join(tmp)
            dic[tmp].append(i)
        print(dic)
        
        for i, v in dic.items():
            tmp=[]
            for j in v:
                tmp.append(strs[j])
            res.append(tmp)
        return res
            
            