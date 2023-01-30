class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h= 0, len(nums)-1
        
        while l <= h:
            mid= math.floor((l+h)/ 2)
            num= nums[mid]
            if target == num:
                return mid
            if target < num:
                h= mid-1
            else:
                l= mid+1
        return -1