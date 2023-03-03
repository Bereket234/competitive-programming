class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(l, r):
            if l >= r:
                return
            reverse(l + 1, r - 1)
            s[r], s[l]= s[l], s[r]
            return 
        reverse(0, len(s)-1)
        
            