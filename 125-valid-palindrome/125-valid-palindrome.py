class Solution:
    def isPalindrome(self, s: str) -> bool:
        string= ''.join(e.lower() for e in s if e.isalnum() )
        reverse= string[::-1]
        
        if string == reverse:
            return True
        return False