class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res= 0
        odds= deque()
        cnt= l= 0
        for r in range(len(nums)):
            if nums[r] % 2 != 0:
                cnt+=1
                odds. append(r)
            while cnt > k:
                if nums[l] % 2 != 0:
                    cnt-=1
                    odds.popleft()
                l+=1
            if cnt == k:
                res+= odds[0] - l + 1
            
            
        return res