class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_ptr, neg_ptr= 0, 0
        n= len(nums)
        index= 0
        res= []
        
        while pos_ptr < n or neg_ptr < n:
            if index % 2 == 0 and pos_ptr < n:
                while pos_ptr < n and nums[pos_ptr] < 0:
                    pos_ptr+=1
                if pos_ptr < n:
                    res.append(nums[pos_ptr])
                    pos_ptr+=1
            else:
                while neg_ptr < n and nums[neg_ptr] > 0:
                    neg_ptr+=1
                if neg_ptr < n:
                    res.append(nums[neg_ptr])
                    neg_ptr+=1
            index+=1
        return res