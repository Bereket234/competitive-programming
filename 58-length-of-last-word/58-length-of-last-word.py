class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s= s.strip()
        s= list(s.split(' '))
        return len(s[-1])