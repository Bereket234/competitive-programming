class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        deq1= deque()
        deq2= deque()
        cnt=l= 0
        
        
        for r in range(len(nums)):
            while deq1 and deq1[-1] < nums[r]:
                deq1.pop()
            deq1.append(nums[r])
            
            while deq2  and deq2[-1] > nums[r]:
                deq2.pop()
            deq2.append(nums[r])
            
            while deq1 and deq2 and abs(deq1[0] - deq2[0]) > limit:
                if deq1[0] == nums[l]:
                    deq1.popleft()
                if deq2[0] == nums[l]:
                    deq2.popleft()
                l+=1
            cnt= max(cnt, r - l +1)
        
        return cnt 