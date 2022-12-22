class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        res= {}
        result=[[],[]]
        for match in matches:
            w=match[0]
            l=match[1]
            res[w]= [1+res.get(w, [0,0])[0], 1+res.get(w, [0,0])[1]]
            res[l]= [res.get(l, [0,0])[0], 1+res.get(l, [0,0])[1]]
        for r,v in res.items():
            if v[0] == v[1]:
                result[0].append(r)
            if v[0] +1 == v[1]:
                result[1].append(r)
        result[0].sort()
        result[1].sort()
        return result