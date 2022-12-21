class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_cnt= {}
        t_cnt= {}
        for c in s:
            s_cnt[c]= 1+ s_cnt.get(c, 0)
        for c in t:
            t_cnt[c]= 1+ t_cnt.get(c, 0)
        
        for c,v in t_cnt.items():
            if c not in s_cnt or s_cnt[c] != v:
                return c