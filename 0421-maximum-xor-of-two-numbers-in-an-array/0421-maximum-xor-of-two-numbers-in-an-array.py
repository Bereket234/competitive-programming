class Solution:
    def __init__(self):
        self.root= {0: None, 1: None}
        self.max_len= 0
    
    def search(self, bits):
        curr= self.root
        res= []

        for i in range(len(bits)):
            if curr[(1 - bits[i])]:
                res.append("1")
                curr= curr[1 - bits[i]]

            else:
                res.append("0")
                curr= curr[bits[i]]
        res= int("".join(res), 2)
        return res
        
        

    def add(self, bits):
        curr= self.root
        
        for i in range(len(bits)):
            if not curr[bits[i]]:
                curr[bits[i]]= {0: None, 1: None}
            curr= curr[bits[i]]
        

    def findMaximumXOR(self, nums: List[int]) -> int:
        res= 0
        self.max_len= len(bin(max(nums))) - 2
        
        for i, num in enumerate(nums):
            bits= []
            while num > 0:
                bits.append(num%2)
                num//=2
            while len(bits) < self.max_len:
                bits.append(0)
            bits.reverse()
            nums[i]= bits.copy()
            
        for i in range(len(nums)):
            self.add(nums[i])
            
        for i in range(len(nums)):
            temp= self.search(nums[i])
            res= max(res, temp)
            
        return res
    
    