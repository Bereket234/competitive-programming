class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_cnt= Counter(s[: len(p)])
        p_cnt= Counter(p)
        res= []
        left= 0
        if s_cnt == p_cnt:
            res.append(0)
        for right in range(len(p), len(s)):
            s_cnt[s[right]]= s_cnt.get(s[right], 0) + 1
            s_cnt[s[left]]-=1
            if s_cnt[s[left]] == 0:
                del s_cnt[s[left]]
            left+=1
            if s_cnt == p_cnt:
                res.append(left)
        return res
            