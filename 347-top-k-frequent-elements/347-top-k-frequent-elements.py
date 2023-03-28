class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter= Counter(nums)
        nums= list(set(nums))       
        def quick_sort(start, end):   
            p= start
            w = start + 1
            for r in range(start+ 1, end):
                pivot= counter[nums[p]]
                read= counter[nums[r]]

                if pivot >= read:
                    nums[r], nums[w]= nums[w], nums[r]
                    w +=1
            nums[p], nums[w-1]= nums[w-1], nums[p]
            
            if len(nums) - k == w-1:
                return nums[w-1:]
            
            if len(nums) - k < w-1:
                res= quick_sort(start, w-1)
            
            if len(nums) - k > w-1:
                res= quick_sort(w,end)
            
            return res
                
        return quick_sort(0, len(nums))