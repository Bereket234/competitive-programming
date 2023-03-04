class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        visited= {0: 1}
        sum_= 0
        res= 0
        for i in range(len(nums)):
            sum_+= nums[i]
            res += visited.get(sum_- goal, 0)
            visited[sum_]= 1 + visited.get(sum_, 0)
        return res