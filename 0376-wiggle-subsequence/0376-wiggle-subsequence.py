class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        up = dn = 1
        
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                up = dn + 1
            elif nums[i] > nums[i+1]:
                dn = up + 1
        return max(up, dn)
            