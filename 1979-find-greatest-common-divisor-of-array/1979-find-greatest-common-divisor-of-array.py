class Solution:
    def findGCD(self, nums: List[int]) -> int:
        max_= max(nums)
        min_= min(nums)
        
        j= 2
        res= 1
        
        while min_ > 1 and j <= min_:
            if min_//j == min_/j and max_//j == max_/j:
                res *= j
                min_ //= j
                max_ //= j
            else:
                j+=1
        return res