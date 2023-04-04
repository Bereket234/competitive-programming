class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b= a[::-1], b[::-1]
        carry= 0
        res= []
        
        for i in range(max(len(a), len(b))):
            bitA= int(a[i]) if i < len(a) else 0
            bitB= int(b[i]) if i < len(b) else 0
            
            sum_= bitA + bitB +carry
            res.append(str(sum_%2))
            carry= sum_ // 2
        if carry:
            res.append('1')
        res.reverse()
        
        
        return ''.join(res)