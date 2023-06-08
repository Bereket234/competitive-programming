class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pos= len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] + i >= pos:
                pos= i
        
        if pos:
            return False
        return True