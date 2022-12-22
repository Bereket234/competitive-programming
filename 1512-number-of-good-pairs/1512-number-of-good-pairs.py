from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt= Counter(nums)
        res=0
        
        for i,v in cnt.items():
            if v>1:
                n= v-1
                res+= ((n)*(1+n)//2)
        return res