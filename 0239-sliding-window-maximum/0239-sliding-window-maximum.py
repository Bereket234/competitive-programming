class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que= deque([])
        l= 0
        
        for i in range(k):
            while que and que[-1] < nums[i]:
                que.pop()
            que.append(nums[i])
        res= []
        res.append(que[0])
        for r in range(k, len(nums)):
            while que and que[-1] < nums[r]:
                que.pop()
            que.append(nums[r])
            if nums[l] == que[0]:
                que.popleft()
            res.append(que[0])
            l+=1
        return res