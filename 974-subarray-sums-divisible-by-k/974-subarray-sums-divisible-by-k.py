class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        visited= {0: 1}
        curr_sum= 0
        res= 0
        
        for num in nums:
            curr_sum += num
            if curr_sum % k in visited:
                res+= visited[curr_sum % k]
            visited[curr_sum % k]= 1 + visited.get(curr_sum % k, 0)
        return res