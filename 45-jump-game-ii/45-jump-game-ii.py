class Solution:
    def jump(self, nums: List[int]) -> int:
        res= 0
        r= l= 0
        while r < len(nums)-1:
            max_= 0
            
            for i in range(l, r+1):
                max_= max(max_, i + nums[i])
            
            l = r +1
            r= max_
            res +=1
        
        return res