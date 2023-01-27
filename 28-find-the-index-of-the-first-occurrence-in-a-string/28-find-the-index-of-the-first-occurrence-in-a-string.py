class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        r=0
        for r in range(len(haystack)):
            if haystack[r: r+len(needle)] == needle:
                return r
        return -1