class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low= 0
        high= len(nums)-1
        res= [-1, -1]
        
        while low <= high:
            mid= (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid -1
        if low >= len(nums) or nums[low] != target:
            return res
        res= [low, -1]
        low= 0
        high= len(nums)-1
        while low <= high:
            mid= (low + high) // 2
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        res[1]= high
        return res