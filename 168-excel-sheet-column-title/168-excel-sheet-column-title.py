class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res= []
        i=columnNumber
        while i > 0:
            char= chr(65 + ((i-1) % 26))
            res.append(char)
            i = (i-1)//26
        res.reverse()
        return ''.join(res)
            
        
        