class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        diff = sum_//2
        
        if sum_ / 2 != sum_ // 2:
            return False
        
        sums= set([0])
        for num in nums:
            new= set()
            for c in sums:
                if num + c == diff:
                    return True
                new.add(c)
                new.add(c+ num)
            sums= new
        return False
        