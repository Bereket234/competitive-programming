class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len, left= 0, 0
        elts= set()
        
        for right in range(len(s)):
            while s[right] in elts:
                elts.remove(s[left])
                left+=1
            elts.add(s[right])
            max_len= max(max_len, right-left+1)
        return max_len
            
                