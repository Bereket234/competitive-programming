class Solution:
    def isPalindrome(self, x: int) -> bool:
        ls= str(x)
        l,r=0,len(ls)-1
        
        while l<r:
            if ls[l] != ls[r]:
                return False
            l+=1
            r-=1
        return True