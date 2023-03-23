class Solution:
    def findKthLargest(self, nums: List[int], k: int, start=None, end= None) -> int:
        start = 0 if not start else start
        end= len(nums) if not end else end
        if start >= end:
            return -1
        w= start + 1
        for r in range(start + 1, end):
            if nums[r] < nums[start]:
                nums[r], nums[w]= nums[w], nums[r]
                w += 1
        
        nums[w - 1], nums[start] =  nums[start], nums[w-1]
        
        if w - 1 == len(nums) - k:
            return nums[w-1]
        
        if len(nums) - k < w -1:
            return self.findKthLargest(nums, k, start, w-1)
        else:
            return self.findKthLargest(nums, k, w, end)