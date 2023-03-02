class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        res= 0
        mod= 10**9 + 7
        range_cnt= [0 for _  in range(len(nums)+1)]
        
        for request in requests:
            start, end= request
            range_cnt[start] += 1
            range_cnt[end+1] -= 1
        for i in range(1, len(range_cnt)):
            range_cnt[i] += range_cnt[i-1]
        range_cnt.pop()
        range_cnt.sort()
        nums.sort()
        
        for i in range(len(nums)-1, -1, -1):
            res+= (nums[i] * range_cnt[i])
        
        return res % mod