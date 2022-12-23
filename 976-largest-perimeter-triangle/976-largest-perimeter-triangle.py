class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n= len(nums)-3
        for i in range(n, -1,-1):
            s1, s2, s3= nums[i], nums[i+1], nums[i+2]
            
            if s1 + s2 > s3:
                return s1 + s2 + s3
        return 0