class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        reps= [i for i in range(26)]
        res= []
        
        def find_rep(node):
            while node != reps[node]:
                node= reps[node]
            return node
        
        for i in range(len(s1)):
            rep1= find_rep(ord(s1[i]) - 97)
            rep2= find_rep (ord(s2[i]) - 97)
            
            if rep1 < rep2:
                reps[rep2] = rep1
            else:
                reps[rep1] = rep2
            
        for c in baseStr:
            repc= find_rep(ord(c)-97)
            res.append(chr(97 + repc))
        
        return ''.join(res)
        