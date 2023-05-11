class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bits= [0] * 32
        
        for num in nums:
            i= 0
            if num < 0:
                bits[31] += 1
                num= abs(num)
                
            while num > 0:
                bits[i] += num & 1
                num >>= 1
                i+=1
        res = 0
        
        for i in range(len(bits)-1):
            bit = bits[i]
            if bit % 3 != 0:
                res += (2 ** i)
        if bits[31] % 3:
            if bits[31] % 3 == 2:
                return -2147483648
            res *= -1
        return res