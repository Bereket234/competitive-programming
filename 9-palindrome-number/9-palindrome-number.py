class Solution:
    def isPalindrome(self, x: int) -> bool:
        ls= str(x)
        l,r=0,len(ls)-1
        
        
        return ls[::-1] == ls