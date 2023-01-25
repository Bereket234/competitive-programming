class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        cnt= [0, 0, 0]
        
        res= [0] * len(nums)
        
        for num in nums:
            if num < pivot:
                cnt[0] += 1
            elif num > pivot:
                cnt[2] += 1
            else:
                cnt[1] += 1
        idx= [0, cnt[0], cnt[1]+ cnt[0]]
        
        for num in nums:
            if num < pivot:
                res[idx[0]]= num
                idx[0] +=1
            elif num > pivot:
                res[idx[2]]= num
                idx[2] += 1
            elif num == pivot:
                res[idx[1]]= num
                idx[1] +=1
        return res