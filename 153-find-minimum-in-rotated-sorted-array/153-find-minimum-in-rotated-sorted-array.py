class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,h=0, len(nums)-1
        mid= (l + h)//2
        res= float("inf")
        
        while l <= h:
            if nums[l] < nums[h]:
                res= min(nums[l], res)
                return res
            mid= (l+h)//2
            res= min(nums[mid], res)
            if nums[mid] < nums[l]:
                h = mid-1
            else:
                l= mid+1
        return res