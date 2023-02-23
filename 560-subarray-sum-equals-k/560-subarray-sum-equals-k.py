class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        visited= {0:1}
        res= 0
        
        for i in range(1, len(nums)):
            nums[i]= nums[i] + nums[i-1]
        
        for num in nums:
            res += visited.get(num-k, 0)
            visited[num]= 1 + visited.get(num, 0)
        return res