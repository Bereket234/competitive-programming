class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a= ceil(sqrt(c))
        b=0
        while b <= a:
            if b**2 + a**2 == c:
                return True
            elif b**2 + a**2  < c:
                b+=1
            else:
                a-=1
        return False