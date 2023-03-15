class Solution:
    def validate(self, s_cnt, t_cnt):
        for k in t_cnt:
            if s_cnt[k] < t_cnt[k]:
                return False
        return True
        
    def minWindow(self, s: str, t: str) -> str:
        s_cnt= defaultdict(int)
        t_cnt= Counter(t)
        res= [-1, len(s) + 2]
        diff= res[1] - res[0]
        l= 0
        for r in range(len(s)):
            if s[r] in t_cnt:
                s_cnt[s[r]] += 1
            
            while self.validate(s_cnt, t_cnt):
                if diff > r - l + 1:
                    diff= r - l + 1
                    res[0] = l
                    res[1]= r + 1
                if s[l] in t_cnt:
                    s_cnt[s[l]] -= 1
                l+=1
        return "".join(s[res[0]: res[1]]) if diff < len(s) + 2 else ""