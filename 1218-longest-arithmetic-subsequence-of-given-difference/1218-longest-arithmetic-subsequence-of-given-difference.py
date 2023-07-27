class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        cnt = {}
        
        for num in arr:
            curr= 1
            if num - difference in cnt:
                curr= cnt[num - difference] + 1
            cnt[num]= curr
        return max(cnt.values())