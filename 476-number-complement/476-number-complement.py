class Solution:
    def findComplement(self, num: int) -> int:
        original= num
        i= 0
        while original >= (1 << i):
            num ^= (1 << i)
            i +=1
        return num