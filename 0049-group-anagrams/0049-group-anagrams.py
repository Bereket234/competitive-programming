class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group= defaultdict(list)
        res=[]
        
        for s in strs:
            s_= sorted(s)
            group[''.join(s_)].append(s)
        
        for k, v in group.items():
            res.append(v)
        
        return res