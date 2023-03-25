class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        res= 0
        def helper(transfer, i, cnt):
            nonlocal res
            if i == len(requests):
                return 
            transfer[requests[i][0]] += 1
            transfer[requests[i][1]] -= 1
            
            if all( x == 0 for x in transfer):
                res= max(res, cnt + 1)
            
            helper(transfer, i + 1, cnt + 1)
            
            transfer[requests[i][0]] -= 1
            transfer[requests[i][1]] += 1
            
            if all( x == 0 for x in transfer):
                res= max(res, cnt)
            
            helper(transfer, i + 1, cnt)
            
        helper([0] * n, 0, 0)
        return res
        
        