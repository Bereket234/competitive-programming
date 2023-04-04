class Solution:
    def reverse(self, x: int) -> int:
        Max= 2147483647
        Min= -2147483648
        
        res= 0
        
        while x:
            rem= int(math.fmod(x, 10)) #in python -1 % 10 is 9 
            x= int(x / 10) # in pyrhon -1 // 10 is -1
            if (res > Max//10) or (res == Max//10 and rem >= Max % 10):
                return 0
            if (res < Min// 10) or (res == Min//10 and rem <= Min % 10):
                return 0
            res= (10 * res) + rem
        return res