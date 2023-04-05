class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        cnt= 0
        
        for i in range(len(nums)):
            g= nums[i]
            if g == k:
                cnt += 1
                
            for j in range(i + 1, len(nums)):
                g= gcd(nums[j], g)
                
                if g == k:
                    cnt += 1
        return cnt
            