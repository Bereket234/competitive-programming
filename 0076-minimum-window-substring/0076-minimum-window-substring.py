class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_cnt= Counter(t)
        s_cnt= Counter()
        l= 0
        total= len(t)
        res_cnt= float('inf')
        res= ''
        for r in range(len(s)):
            s_cnt[s[r]]= s_cnt.get(s[r], 0) + 1
            
            if s_cnt[s[r]] <= t_cnt[s[r]]:
                total -= 1
                
            while total == 0:
                if r - l + 1 < res_cnt:
                    res_cnt = r-l+1
                    res= s[l:r+1]
                s_cnt[s[l]] -= 1
                if s_cnt[s[l]] < t_cnt[s[l]]:
                    total += 1
                l+=1
        return res
                